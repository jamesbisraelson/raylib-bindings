from typing import List, Optional, Iterable, Union, Dict
import json
import re
from .schema import *
from .utils import *
from .templates import *

class Output:
    def __init__(self, pyi: List[str], cpp: List[str], metadata: Dict, messages: List[str]):
        self.pyi = pyi
        self.cpp = cpp
        self.metadata = metadata
        self.messages = messages

    def save(self, pyi_path: str, cpp_path: str):
        pyi = '\n'.join(self.pyi)
        cpp = '\n'.join(self.cpp)
        with open(pyi_path, 'w') as f:
            f.write(pyi)
        with open(cpp_path, 'w') as f:
            f.write(cpp)
        for msg in self.messages:
            print(msg)
    
def generate(json_file: Union[str, dict, Header], /, 
             module_name: str,
             headers: List[str],
             ignored_functions: Optional[Iterable[str]]=None,
             vector_pattern: Optional[str]=None,
             opaque_structs: Optional[Iterable[str]]=None,
             use_fat_pointer: bool=False,   # attach fields info to pointer type
             ) -> Output:
    ignored_functions = set(ignored_functions or [])
    opaque_structs = set(opaque_structs or [])

    metadata: dict = None
    if isinstance(json_file, str):
        with open(json_file) as f:
            metadata = json.load(f)
            api = header_from_dict(metadata)
    elif isinstance(json_file, dict):
        metadata = json_file
        api = header_from_dict(json_file)
    elif isinstance(json_file, Header):
        api = json_file

    # remove opaque structs
    api.structs = [s for s in api.structs if s.name not in opaque_structs]

    ptype = lambda x: ptype_ex(x, vector_pattern, opaque_structs)

    pyi = get_pyi_header()
    cpp = get_cpp_header(headers)
    messages: List[str] = []

    # %%
    # gen struct
    for struct in api.structs:
        if vector_pattern and re.match(vector_pattern, struct.name):
            template = r'''
PyObject* py_var(VM* vm, %T0 v){
    return py_var(vm, _struct_cast<%T0, %T1>(v));
}
template<>
%T0 py_cast<%T0>(VM* vm, PyObject* obj){
    %T1 v = py_cast<%T1>(vm, obj);
    return _struct_cast<%T1, %T0>(v);
}
template<>
%T0 _py_cast<%T0>(VM* vm, PyObject* obj){
    %T1 v = _py_cast<%T1>(vm, obj);
    return _struct_cast<%T1, %T0>(v);
}
'''.lstrip()
            builtin_name = struct.name.replace('Vector', 'Vec')
            cpp.append(template.replace('%T0', struct.name).replace('%T1', builtin_name))
            continue

        wrapped_name = f'wrapped__{struct.name}'
        wrapped_base_name = f'_wrapped__{struct.name}'
        init_args = ['self']
        pyi.append(f'class _wrapped__{struct.name}:')
        for field in struct.fields:
            kv = f'{field.name}: {ptype(field.type)}'
            init_args.append(kv)
            kv = ('    '+kv).ljust(40)
            if field.description:
                kv += f'# `{field.type}`: {field.description}'
            pyi.append(kv)

        pyi.extend([
            '',
            f'class {struct.name}(_StructLike[{struct.name}], {wrapped_base_name}):',
            f'    """{struct.description}"""',
            '    @overload',
            '    def __init__(self): ...',
            '    @overload',
            f'    def __init__({", ".join(init_args)}): ...',
            '',
        ])

        if use_fat_pointer:
            pyi.extend([
                f'class {struct.name}_p(Pointer[{struct.name}], {wrapped_base_name}):',
                f'    """Wraps `{struct.name} *`"""',
                '',
            ])
        else:
            pyi.extend([
                f'class {struct.name}_p(Pointer[{struct.name}]):',
                f'    """Wraps `{struct.name} *`"""',
                '',
            ])

        cpp.append('/*************** ' + struct.name + ' ***************/')
        cpp.append(f'struct {wrapped_name}' + '{')
        cpp.append(f'    PY_CLASS({wrapped_name}, {module_name}, {struct.name})')
        cpp.append( '')
        cpp.append(f'    {struct.name} _value;')
        cpp.append(f'    {struct.name}* _()' + ' { return &_value; }')
        cpp.append(f'    {wrapped_name}() = default;')
        cpp.append(f'    {wrapped_name}(const wrapped__{struct.name}& other) = default;')
        cpp.append( '')
        cpp.append(f'    {wrapped_name}(const {struct.name}& other)' + '{')
        cpp.append(f'        memcpy(&_value, &other, sizeof({struct.name}));')
        cpp.append( '    }')
        cpp.append( '    bool operator==(const ' + wrapped_name + '& other) const' + '{')
        cpp.append( '        return memcmp(&_value, &other._value, sizeof(' + struct.name + ')) == 0;')
        cpp.append( '    }')
        cpp.append( '')
        cpp.append( '    static void _register(VM* vm, PyObject* mod, PyObject* type)' + '{')
        # set _fields_
        _fields_ = ', '.join([f'"{field.name}"' for field in struct.fields])
        _fields_ = '{' + _fields_ + '}'
        cpp.extend([
            '        vm->bind_method<-1>(type, "__init__", [](VM* vm, ArgsView args){',
           f'            static const StrName _fields_[] = {_fields_};',
            '            if(args.size()==1) return vm->None;',
           f'            if(args.size()-1 != {len(struct.fields)}) vm->TypeError(fmt("expected {len(struct.fields)} arguments, got ", args.size()-1));',
            '            for(int i=1; i<args.size(); i++){',
            '                vm->setattr(args[0], _fields_[i-1], args[i]);',
            '            }',
            '            return vm->None;',
            '        });',
        ])
        cpp.append(f'        PY_STRUCT_LIKE({wrapped_name})')
        for field in struct.fields:
            if '[' in field.type and ']' in field.type:
                cpp.append(f'        PY_READONLY_FIELD({wrapped_name}, "{field.name}", _, {field.name})')
            else:
                cpp.append(f'        PY_FIELD({wrapped_name}, "{field.name}", _, {field.name})')
        cpp.append( '    }')
        cpp.append( '};\n')

        cpp.append(f'PyObject* py_var(VM* vm, {struct.name} v)' + '{')
        cpp.append(f'    return VAR_T({wrapped_name}, v);')
        cpp.append( '}')
        cpp.append( 'template<>')
        cpp.append(f'{struct.name} py_cast<{struct.name}>(VM* vm, PyObject* obj)' + '{')
        cpp.append(f'    return *py_cast<{wrapped_name}&>(vm, obj)._();')
        cpp.append( '}')
        cpp.append( 'template<>')
        cpp.append(f'{struct.name} _py_cast<{struct.name}>(VM* vm, PyObject* obj)' + '{')
        cpp.append(f'    return *_py_cast<{wrapped_name}&>(vm, obj)._();')
        cpp.append( '}')
        cpp.append(f'PyObject* py_var(VM* vm, const {struct.name}* v)' + '{')
        cpp.append(f'    const static std::pair<StrName, StrName> P("{module_name}", "{struct.name}_p");')
        cpp.append(f'    PyObject* type = vm->_modules[P.first]->attr(P.second);')
        cpp.append(f'    return vm->heap.gcnew<VoidP>(PK_OBJ_GET(Type, type), v);')
        cpp.append( '}')
    # %%
    # gen functions
    cpp.extend([
        '/' * 40,
        ''
        'void add_module_raylib(VM* vm){',
       f'    PyObject* mod = vm->new_module("{module_name}");',
        ''
    ])

    cpp.append('    // defines')
    for define in api.defines:
        if define.type == "INT":
            pyi.append(f'{define.name}: int = {int(define.value)}')
            cpp.append(f'    mod->attr().set("{define.name}", py_var(vm, {int(define.value)}));')
        elif define.type == "STRING":
            pyi.append(f'{define.name}: str = "{define.value}"')
            cpp.append(f'    mod->attr().set("{define.name}", py_var(vm, "{define.value}"));')
        elif define.type == "FLOAT":
            pyi.append(f'{define.name}: float = {float(define.value)}')
            cpp.append(f'    mod->attr().set("{define.name}", py_var(vm, {define.value}));')
        else:
            pass        # unrecognized type
    
    pyi.append('')

    for enum in api.enums:
        cpp.append(f'    // {enum.name}')
        _enum_values = ', '.join([f'{{"{v.name}", {v.value}}}' for v in enum.values])
        _enum_values = '{' + _enum_values + '}'
        cpp.append(f'    _bind_enums(vm, mod, {_enum_values});')

        pyi.append(f'########## {enum.name} ##########')
        pyi.append(f'# {enum.description}')
        for v in enum.values:
            kv = f'{v.name} = {v.value}'
            pyi.append(f'{kv:48}# {v.description}')
        pyi.append('')

    cpp.append('')

    for struct in api.structs:
        if vector_pattern and re.match(vector_pattern, struct.name):
            continue
        cpp.append(f'    wrapped__{struct.name}::register_class(vm, mod);')
        # generate its corresponding pointer type
        cpp.append( '    {')
        cpp.append(f'        PyObject* type = vm->new_type_object(mod, "{struct.name}_p", VoidP::_type(vm));')
        cpp.append(f'        mod->attr().set("{struct.name}_p", type);')
        cpp.append(f'        PY_POINTER_SETGETITEM({struct.name})')

        if use_fat_pointer:
            for field in struct.fields:
                if '[' in field.type and ']' in field.type:
                    cpp.append(f'        PY_READONLY_FIELD_P({struct.name}, "{field.name}", {field.name})')
                else:
                    cpp.append(f'        PY_FIELD_P({struct.name}, "{field.name}", {field.name})')

        cpp.append( '    }')

    cpp.append('')

    for func in api.functions:
        if func.name in ignored_functions:
            continue
        sigc = f'{func.return_type} {func.name}({", ".join([p.type+" "+p.name for p in (func.params or [])])})'
        has_vargs = func.params and func.params[-1].type == '...'
        parameters = ', '.join([f'{p.name}: {ptype(p.type)}' for p in (func.params or [])])
        sigpy = f'{func.name}({parameters}) -> {ptype(func.return_type)}'
        tmp = f'def {sigpy}:\n'
        tmp += f'    """{func.description}\n\n'
        tmp += f'    Wraps: `{sigc}`\n'
        tmp += f'    """\n'
        if has_vargs:
            messages.append(f'WARNING: {sigc} is a variadic function, skipped')
            continue
        pyi.append(tmp)
        cpp.append(f'    _bind(vm, mod, "{sigpy}", &{func.name});')

    cpp.append('')
    cpp.append('    CodeObject_ co = vm->compile("from linalg import *", "raylib.py", EXEC_MODE);')
    cpp.append('    vm->_exec(co, mod);')
    # gen alias
    for alias in api.aliases:
        pyi.append(f'# {alias.description}')
        k, v = alias.name, ptype(alias.type)
        pyi.append(f'{k} = {v}')
        pyi.append(f'{k}_p = {v}_p')
        pyi.append('')
        cpp.append(f'    mod->attr().set("{k}", mod->attr("{v}"));')
        cpp.append(f'    mod->attr().set("{k}_p", mod->attr("{v}_p"));')

    cpp.append('}')

    cpp.append('}  // namespace pkpy')

    return Output(pyi, cpp, metadata, messages)

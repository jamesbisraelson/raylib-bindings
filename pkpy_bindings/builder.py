from typing import List
import json
import re
from .schema import *
from .utils import *
from .templates import *

class Output:
    def __init__(self, pyi: List[str], cpp: List[str]):
        self.pyi = pyi
        self.cpp = cpp

    def save(self, pyi_path: str, cpp_path: str):
        pyi = '\n'.join(self.pyi)
        cpp = '\n'.join(self.cpp)
        with open(pyi_path, 'w') as f:
            f.write(pyi)
        with open(cpp_path, 'w') as f:
            f.write(cpp)
    
def generate(json_file: str, /, module_name: str, headers: List[str], ignored_functions=None, vector_pattern=None, opaque_structs=None) -> Output:
    ignored_functions = set(ignored_functions or [])
    opaque_structs = set(opaque_structs or [])

    if isinstance(json_file, str):
        with open(json_file) as f:
            api = header_from_dict(json.load(f))
    elif isinstance(json_file, dict):
        api = header_from_dict(json_file)
    elif isinstance(json_file, Header):
        api = json_file

    # remove opaque structs
    api.structs = [s for s in api.structs if s.name not in opaque_structs]

    ptype = lambda x: ptype_ex(x, vector_pattern, opaque_structs)

    pyi = get_pyi_header()
    cpp = get_cpp_header(headers)

    # %%
    # gen enums
    for enum in api.enums:
        pyi.append(f'########## {enum.name} ##########')
        pyi.append(f'# {enum.description}')
        for v in enum.values:
            kv = f'{v.name} = {v.value}'
            pyi.append(f'{kv:48}# {v.description}')
        pyi.append('')

    # %%
    # gen struct
    pyi.append('')

    for struct in api.structs:
        if re.match(vector_pattern, struct.name):
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
    '''
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
            f'class {struct.name}_p(Pointer[{struct.name}], {wrapped_base_name}):',
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

    # gen alias
    for alias in api.aliases:
        pyi.append(f'# {alias.description}')
        pyi.append(f'{alias.name} = {ptype(alias.type)}')
        pyi.append(f'{alias.name}_p = {ptype(alias.type)}_p')
        pyi.append('')
    # %%
    # gen functions
    cpp.extend([
        '/' * 40,
        ''
        'void add_module_raylib(VM* vm){',
       f'    PyObject* mod = vm->new_module("{module_name}");',
        ''
    ])

    for enum in api.enums:
        cpp.append(f'    // {enum.name}')
        for val in enum.values:
            cpp.append(f'    mod->attr().set("{val.name}", py_var(vm, {val.value}));')

    cpp.append('')

    for struct in api.structs:
        if re.match(vector_pattern, struct.name):
            continue
        cpp.append(f'    wrapped__{struct.name}::register_class(vm, mod);')
        # generate its corresponding pointer type
        cpp.append( '    {')
        cpp.append(f'        PyObject* type = vm->new_type_object(mod, "{struct.name}_p", VoidP::_type(vm));')
        cpp.append(f'        PY_POINTER_SETGETITEM({struct.name})')
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
        parameters = ', '.join([f'{p.name}: {ptype(p.type)}' for p in (func.params or [])])
        sigpy = f'{func.name}({parameters}) -> {ptype(func.return_type)}'
        tmp = f'def {sigpy}:\n'
        tmp += f'    """{func.description}\n\n'
        tmp += f'    Wraps: `{sigc}`\n'
        tmp += f'    """\n'
        pyi.append(tmp)
        cpp.append(f'    _bind(vm, mod, "{sigpy}", &{func.name});')

    cpp.append('}')

    cpp.append('}  // namespace pkpy')

    return Output(pyi, cpp)

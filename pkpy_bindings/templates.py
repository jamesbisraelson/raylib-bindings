from typing import List

def get_pyi_header():
    return [
        'from typing import overload',
        'from linalg import *',
        'from c import *',
        'from c import _StructLike',
        '',
    ]

def get_cpp_header(headers: List[str]):
    return [f'#include "{h}"' for h in headers] + [
        '#include "pocketpy.h"',
        '',
        'namespace pkpy{',
'''
template<typename T0, typename T1>
T1 _struct_cast(T0& v){
    static_assert(sizeof(T0) == sizeof(T1));
    static_assert(std::is_trivially_copyable_v<T0>);
    static_assert(std::is_trivially_copyable_v<T1>);
    return (T1&)v;
}

template<size_t N>
void _bind_enums(VM* vm, PyObject* mod, Str name, const std::pair<const char*, i64> (&enums)[N]){
    Dict d(vm);
    for(auto [k, v]: enums){
        PyObject* int_obj = py_var(vm, v);
        mod->attr().set(k, int_obj);
        d.set(int_obj, py_var(vm, k));
    }
    mod->attr().set(name + "_names", py_var(vm, std::move(d)));
}
''',
    ]

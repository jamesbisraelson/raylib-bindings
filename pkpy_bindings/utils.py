import re
from typing import Set

_ptypes = {
    'char': 'int',
    'unsigned char': 'int',
    'short': 'int',
    'unsigned short': 'int',
    'int': 'int',
    'unsigned int': 'int',
    'long': 'int',
    'unsigned long': 'int',
    'long long': 'int',
    'unsigned long long': 'int',
    'float': 'float',
    'double': 'float',
    'bool': 'bool',
    'void': 'None',
    # pointers
    'char *': 'char_p',
    'unsigned char *': 'uchar_p',
    'short *': 'short_p',
    'unsigned short *': 'ushort_p',
    'int *': 'int_p',
    'unsigned int *': 'uint_p',
    'long *': 'long_p',
    'unsigned long *': 'ulong_p',
    'long long *': 'longlong_p',
    'unsigned long long *': 'ulonglong_p',
    'float *': 'float_p',
    'double *': 'double_p',
    'bool *': 'bool_p',
    'void *': 'void_p',
}

def _to_pointer(t: str, opaque_structs: Set[str]):
    if t in opaque_structs:
        return 'void_p'
    if f'{t} *' in _ptypes:
        return _ptypes[f'{t} *']
    return f"'{t}_p'"

def _convert_pointer(t: str, opaque_structs: Set[str]):
    t_backup = t
    t = t.replace(' ', '')
    # 'T[...]' or 'T*'
    if t.endswith(']'):
        assert '*' not in t
        t = t[:t.index('[')]
        return _to_pointer(t, opaque_structs)
    if t.endswith('*'):
        if t.count('*') == 1:
            t = t.rstrip(' *')
            return _to_pointer(t, opaque_structs)
        else:
            return 'void_p'
    return t_backup

def ptype_ex(t: str, vector_pattern: str, opaque_structs: Set[str]):
    t = re.sub(vector_pattern, r'vec\1', t)
    if t == 'const char *':
        return 'str'
    if 'const' in t:
        t = t.replace('const', '').strip()
    if t in _ptypes:
        return _ptypes[t]
    return _convert_pointer(t, opaque_structs)

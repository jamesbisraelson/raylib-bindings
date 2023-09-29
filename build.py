IGNORED_FUNCTIONS = {
    # callback functions
    "SetTraceLogCallback",
    "SetLoadFileDataCallback",
    "SetSaveFileDataCallback",
    "SetLoadFileTextCallback",
    "SetSaveFileTextCallback",
    'SetAudioStreamCallback',
    'AttachAudioStreamProcessor',
    'DetachAudioStreamProcessor',
    'AttachAudioMixedProcessor',
    'DetachAudioMixedProcessor',
}

from pkpy_bindings import generate

pyi_path = 'output/typings/raylib.pyi'
cpp_path = 'output/raylibw.cpp'

generate(
    'raylib/parser/output/raylib_api.json',
    module_name='raylib',
    headers=['raylib.h'],
    ignored_functions=IGNORED_FUNCTIONS,
    vector_pattern=r'\bVector(\d)\b',
    opaque_structs=['rAudioBuffer', 'rAudioProcessor']
).save(pyi_path, cpp_path)

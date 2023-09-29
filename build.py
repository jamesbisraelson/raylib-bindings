_FILE_MANAGEMENT_FUNCTIONS = {
    "LoadFileData",
    "UnloadFileData",
    "SaveFileData",
    "ExportDataAsCode",
    "LoadFileText",
    "UnloadFileText",
    "SaveFileText",
    "FileExists",
    "DirectoryExists",
    "IsFileExtension",
    "GetFileLength",
    "GetFileExtension",
    "GetFileName",
    "GetFileNameWithoutExt",
    "GetDirectoryPath",
    "GetPrevDirectoryPath",
    "GetWorkingDirectory",
    "GetApplicationDirectory",
    "ChangeDirectory",
    "IsPathFile",
    "LoadDirectoryFiles",
    "LoadDirectoryFilesEx",
    "UnloadDirectoryFiles",
    "IsFileDropped",
    "LoadDroppedFiles",
    "UnloadDroppedFiles",
    "GetFileModTime"
}

_MISC_FUNCTIONS = {
    "GetRandomValue",
    "SetRandomSeed",
    "TakeScreenshot",
    "SetConfigFlags",

    "TraceLog",
    "SetTraceLogLevel",
    "MemAlloc",
    "MemRealloc",
    "MemFree",

    "OpenURL"
}

_CUSTOM_CALLBACK_FUNCTIONS = {
    "SetTraceLogCallback",
    "SetLoadFileDataCallback",
    "SetSaveFileDataCallback",
    "SetLoadFileTextCallback",
    "SetSaveFileTextCallback"
}

_COMPRESSION_FUNCTIONS = {
    "CompressData",
    "DecompressData",
    "EncodeDataBase64",
    "DecodeDataBase64"
}

IGNORED_FUNCTIONS = {
    *_FILE_MANAGEMENT_FUNCTIONS,
    *_MISC_FUNCTIONS,
    *_CUSTOM_CALLBACK_FUNCTIONS,
    *_COMPRESSION_FUNCTIONS,
    # variadic functions
    'TextFormat',
    # with callback functions
    'SetAudioStreamCallback',
    'AttachAudioStreamProcessor',
    'DetachAudioStreamProcessor',
    'AttachAudioMixedProcessor',
    'DetachAudioMixedProcessor'
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

FUNCTIONS_UNSUPPORTED = {
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

# remove this line to generate full bindings
FUNCTIONS_3D_OPTIONAL = {'DrawLine3D', 'DrawPoint3D', 'DrawCircle3D', 'DrawTriangle3D', 'DrawTriangleStrip3D', 'DrawCube', 'DrawCubeV', 'DrawCubeWires', 'DrawCubeWiresV', 'DrawSphere', 'DrawSphereEx', 'DrawSphereWires', 'DrawCylinder', 'DrawCylinderEx', 'DrawCylinderWires', 'DrawCylinderWiresEx', 'DrawCapsule', 'DrawCapsuleWires', 'DrawPlane', 'DrawRay', 'DrawGrid', 'LoadModel', 'LoadModelFromMesh', 'IsModelReady', 'UnloadModel', 'GetModelBoundingBox', 'DrawModel', 'DrawModelEx', 'DrawModelWires', 'DrawModelWiresEx', 'DrawBoundingBox', 'DrawBillboard', 'DrawBillboardRec', 'DrawBillboardPro', 'UploadMesh', 'UpdateMeshBuffer', 'UnloadMesh', 'DrawMesh', 'DrawMeshInstanced', 'ExportMesh', 'GetMeshBoundingBox', 'GenMeshTangents', 'GenMeshPoly', 'GenMeshPlane', 'GenMeshCube', 'GenMeshSphere', 'GenMeshHemiSphere', 'GenMeshCylinder', 'GenMeshCone', 'GenMeshTorus', 'GenMeshKnot', 'GenMeshHeightmap', 'GenMeshCubicmap', 'LoadMaterials', 'LoadMaterialDefault', 'IsMaterialReady', 'UnloadMaterial', 'SetMaterialTexture', 'SetModelMeshMaterial', 'LoadModelAnimations', 'UpdateModelAnimation', 'UnloadModelAnimation', 'UnloadModelAnimations', 'IsModelAnimationValid', 'CheckCollisionSpheres', 'CheckCollisionBoxes', 'CheckCollisionBoxSphere', 'GetRayCollisionSphere', 'GetRayCollisionBox', 'GetRayCollisionMesh', 'GetRayCollisionTriangle', 'GetRayCollisionQuad'}

from pkpy_bindings import generate

pyi_path = 'output/typings/raylib.pyi'
cpp_path = 'output/raylibw.cpp'

generate(
    'raylib/parser/output/raylib_api.json',
    module_name='raylib',
    headers=['raylib.h'],
    ignored_functions=FUNCTIONS_UNSUPPORTED | FUNCTIONS_3D_OPTIONAL,
    vector_pattern=r'\bVector(\d)\b',
    opaque_structs=['rAudioBuffer', 'rAudioProcessor']
).save(pyi_path, cpp_path)

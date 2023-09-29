from typing import overload
from linalg import *
from c import *
from c import _StructLike

########## ConfigFlags ##########
# System/Window config flags
FLAG_VSYNC_HINT = 64                            # Set to try enabling V-Sync on GPU
FLAG_FULLSCREEN_MODE = 2                        # Set to run program in fullscreen
FLAG_WINDOW_RESIZABLE = 4                       # Set to allow resizable window
FLAG_WINDOW_UNDECORATED = 8                     # Set to disable window decoration (frame and buttons)
FLAG_WINDOW_HIDDEN = 128                        # Set to hide window
FLAG_WINDOW_MINIMIZED = 512                     # Set to minimize window (iconify)
FLAG_WINDOW_MAXIMIZED = 1024                    # Set to maximize window (expanded to monitor)
FLAG_WINDOW_UNFOCUSED = 2048                    # Set to window non focused
FLAG_WINDOW_TOPMOST = 4096                      # Set to window always on top
FLAG_WINDOW_ALWAYS_RUN = 256                    # Set to allow windows running while minimized
FLAG_WINDOW_TRANSPARENT = 16                    # Set to allow transparent framebuffer
FLAG_WINDOW_HIGHDPI = 8192                      # Set to support HighDPI
FLAG_WINDOW_MOUSE_PASSTHROUGH = 16384           # Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
FLAG_MSAA_4X_HINT = 32                          # Set to try enabling MSAA 4X
FLAG_INTERLACED_HINT = 65536                    # Set to try enabling interlaced video format (for V3D)

########## TraceLogLevel ##########
# Trace log level
LOG_ALL = 0                                     # Display all logs
LOG_TRACE = 1                                   # Trace logging, intended for internal use only
LOG_DEBUG = 2                                   # Debug logging, used for internal debugging, it should be disabled on release builds
LOG_INFO = 3                                    # Info logging, used for program execution info
LOG_WARNING = 4                                 # Warning logging, used on recoverable failures
LOG_ERROR = 5                                   # Error logging, used on unrecoverable failures
LOG_FATAL = 6                                   # Fatal logging, used to abort program: exit(EXIT_FAILURE)
LOG_NONE = 7                                    # Disable logging

########## KeyboardKey ##########
# Keyboard keys (US keyboard layout)
KEY_NULL = 0                                    # Key: NULL, used for no key pressed
KEY_APOSTROPHE = 39                             # Key: '
KEY_COMMA = 44                                  # Key: ,
KEY_MINUS = 45                                  # Key: -
KEY_PERIOD = 46                                 # Key: .
KEY_SLASH = 47                                  # Key: /
KEY_ZERO = 48                                   # Key: 0
KEY_ONE = 49                                    # Key: 1
KEY_TWO = 50                                    # Key: 2
KEY_THREE = 51                                  # Key: 3
KEY_FOUR = 52                                   # Key: 4
KEY_FIVE = 53                                   # Key: 5
KEY_SIX = 54                                    # Key: 6
KEY_SEVEN = 55                                  # Key: 7
KEY_EIGHT = 56                                  # Key: 8
KEY_NINE = 57                                   # Key: 9
KEY_SEMICOLON = 59                              # Key: ;
KEY_EQUAL = 61                                  # Key: =
KEY_A = 65                                      # Key: A | a
KEY_B = 66                                      # Key: B | b
KEY_C = 67                                      # Key: C | c
KEY_D = 68                                      # Key: D | d
KEY_E = 69                                      # Key: E | e
KEY_F = 70                                      # Key: F | f
KEY_G = 71                                      # Key: G | g
KEY_H = 72                                      # Key: H | h
KEY_I = 73                                      # Key: I | i
KEY_J = 74                                      # Key: J | j
KEY_K = 75                                      # Key: K | k
KEY_L = 76                                      # Key: L | l
KEY_M = 77                                      # Key: M | m
KEY_N = 78                                      # Key: N | n
KEY_O = 79                                      # Key: O | o
KEY_P = 80                                      # Key: P | p
KEY_Q = 81                                      # Key: Q | q
KEY_R = 82                                      # Key: R | r
KEY_S = 83                                      # Key: S | s
KEY_T = 84                                      # Key: T | t
KEY_U = 85                                      # Key: U | u
KEY_V = 86                                      # Key: V | v
KEY_W = 87                                      # Key: W | w
KEY_X = 88                                      # Key: X | x
KEY_Y = 89                                      # Key: Y | y
KEY_Z = 90                                      # Key: Z | z
KEY_LEFT_BRACKET = 91                           # Key: [
KEY_BACKSLASH = 92                              # Key: '\'
KEY_RIGHT_BRACKET = 93                          # Key: ]
KEY_GRAVE = 96                                  # Key: `
KEY_SPACE = 32                                  # Key: Space
KEY_ESCAPE = 256                                # Key: Esc
KEY_ENTER = 257                                 # Key: Enter
KEY_TAB = 258                                   # Key: Tab
KEY_BACKSPACE = 259                             # Key: Backspace
KEY_INSERT = 260                                # Key: Ins
KEY_DELETE = 261                                # Key: Del
KEY_RIGHT = 262                                 # Key: Cursor right
KEY_LEFT = 263                                  # Key: Cursor left
KEY_DOWN = 264                                  # Key: Cursor down
KEY_UP = 265                                    # Key: Cursor up
KEY_PAGE_UP = 266                               # Key: Page up
KEY_PAGE_DOWN = 267                             # Key: Page down
KEY_HOME = 268                                  # Key: Home
KEY_END = 269                                   # Key: End
KEY_CAPS_LOCK = 280                             # Key: Caps lock
KEY_SCROLL_LOCK = 281                           # Key: Scroll down
KEY_NUM_LOCK = 282                              # Key: Num lock
KEY_PRINT_SCREEN = 283                          # Key: Print screen
KEY_PAUSE = 284                                 # Key: Pause
KEY_F1 = 290                                    # Key: F1
KEY_F2 = 291                                    # Key: F2
KEY_F3 = 292                                    # Key: F3
KEY_F4 = 293                                    # Key: F4
KEY_F5 = 294                                    # Key: F5
KEY_F6 = 295                                    # Key: F6
KEY_F7 = 296                                    # Key: F7
KEY_F8 = 297                                    # Key: F8
KEY_F9 = 298                                    # Key: F9
KEY_F10 = 299                                   # Key: F10
KEY_F11 = 300                                   # Key: F11
KEY_F12 = 301                                   # Key: F12
KEY_LEFT_SHIFT = 340                            # Key: Shift left
KEY_LEFT_CONTROL = 341                          # Key: Control left
KEY_LEFT_ALT = 342                              # Key: Alt left
KEY_LEFT_SUPER = 343                            # Key: Super left
KEY_RIGHT_SHIFT = 344                           # Key: Shift right
KEY_RIGHT_CONTROL = 345                         # Key: Control right
KEY_RIGHT_ALT = 346                             # Key: Alt right
KEY_RIGHT_SUPER = 347                           # Key: Super right
KEY_KB_MENU = 348                               # Key: KB menu
KEY_KP_0 = 320                                  # Key: Keypad 0
KEY_KP_1 = 321                                  # Key: Keypad 1
KEY_KP_2 = 322                                  # Key: Keypad 2
KEY_KP_3 = 323                                  # Key: Keypad 3
KEY_KP_4 = 324                                  # Key: Keypad 4
KEY_KP_5 = 325                                  # Key: Keypad 5
KEY_KP_6 = 326                                  # Key: Keypad 6
KEY_KP_7 = 327                                  # Key: Keypad 7
KEY_KP_8 = 328                                  # Key: Keypad 8
KEY_KP_9 = 329                                  # Key: Keypad 9
KEY_KP_DECIMAL = 330                            # Key: Keypad .
KEY_KP_DIVIDE = 331                             # Key: Keypad /
KEY_KP_MULTIPLY = 332                           # Key: Keypad *
KEY_KP_SUBTRACT = 333                           # Key: Keypad -
KEY_KP_ADD = 334                                # Key: Keypad +
KEY_KP_ENTER = 335                              # Key: Keypad Enter
KEY_KP_EQUAL = 336                              # Key: Keypad =
KEY_BACK = 4                                    # Key: Android back button
KEY_MENU = 82                                   # Key: Android menu button
KEY_VOLUME_UP = 24                              # Key: Android volume up button
KEY_VOLUME_DOWN = 25                            # Key: Android volume down button

########## MouseButton ##########
# Mouse buttons
MOUSE_BUTTON_LEFT = 0                           # Mouse button left
MOUSE_BUTTON_RIGHT = 1                          # Mouse button right
MOUSE_BUTTON_MIDDLE = 2                         # Mouse button middle (pressed wheel)
MOUSE_BUTTON_SIDE = 3                           # Mouse button side (advanced mouse device)
MOUSE_BUTTON_EXTRA = 4                          # Mouse button extra (advanced mouse device)
MOUSE_BUTTON_FORWARD = 5                        # Mouse button forward (advanced mouse device)
MOUSE_BUTTON_BACK = 6                           # Mouse button back (advanced mouse device)

########## MouseCursor ##########
# Mouse cursor
MOUSE_CURSOR_DEFAULT = 0                        # Default pointer shape
MOUSE_CURSOR_ARROW = 1                          # Arrow shape
MOUSE_CURSOR_IBEAM = 2                          # Text writing cursor shape
MOUSE_CURSOR_CROSSHAIR = 3                      # Cross shape
MOUSE_CURSOR_POINTING_HAND = 4                  # Pointing hand cursor
MOUSE_CURSOR_RESIZE_EW = 5                      # Horizontal resize/move arrow shape
MOUSE_CURSOR_RESIZE_NS = 6                      # Vertical resize/move arrow shape
MOUSE_CURSOR_RESIZE_NWSE = 7                    # Top-left to bottom-right diagonal resize/move arrow shape
MOUSE_CURSOR_RESIZE_NESW = 8                    # The top-right to bottom-left diagonal resize/move arrow shape
MOUSE_CURSOR_RESIZE_ALL = 9                     # The omnidirectional resize/move cursor shape
MOUSE_CURSOR_NOT_ALLOWED = 10                   # The operation-not-allowed shape

########## GamepadButton ##########
# Gamepad buttons
GAMEPAD_BUTTON_UNKNOWN = 0                      # Unknown button, just for error checking
GAMEPAD_BUTTON_LEFT_FACE_UP = 1                 # Gamepad left DPAD up button
GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2              # Gamepad left DPAD right button
GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3               # Gamepad left DPAD down button
GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4               # Gamepad left DPAD left button
GAMEPAD_BUTTON_RIGHT_FACE_UP = 5                # Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6             # Gamepad right button right (i.e. PS3: Square, Xbox: X)
GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7              # Gamepad right button down (i.e. PS3: Cross, Xbox: A)
GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8              # Gamepad right button left (i.e. PS3: Circle, Xbox: B)
GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9               # Gamepad top/back trigger left (first), it could be a trailing button
GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10              # Gamepad top/back trigger left (second), it could be a trailing button
GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11             # Gamepad top/back trigger right (one), it could be a trailing button
GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12             # Gamepad top/back trigger right (second), it could be a trailing button
GAMEPAD_BUTTON_MIDDLE_LEFT = 13                 # Gamepad center buttons, left one (i.e. PS3: Select)
GAMEPAD_BUTTON_MIDDLE = 14                      # Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
GAMEPAD_BUTTON_MIDDLE_RIGHT = 15                # Gamepad center buttons, right one (i.e. PS3: Start)
GAMEPAD_BUTTON_LEFT_THUMB = 16                  # Gamepad joystick pressed button left
GAMEPAD_BUTTON_RIGHT_THUMB = 17                 # Gamepad joystick pressed button right

########## GamepadAxis ##########
# Gamepad axis
GAMEPAD_AXIS_LEFT_X = 0                         # Gamepad left stick X axis
GAMEPAD_AXIS_LEFT_Y = 1                         # Gamepad left stick Y axis
GAMEPAD_AXIS_RIGHT_X = 2                        # Gamepad right stick X axis
GAMEPAD_AXIS_RIGHT_Y = 3                        # Gamepad right stick Y axis
GAMEPAD_AXIS_LEFT_TRIGGER = 4                   # Gamepad back trigger left, pressure level: [1..-1]
GAMEPAD_AXIS_RIGHT_TRIGGER = 5                  # Gamepad back trigger right, pressure level: [1..-1]

########## MaterialMapIndex ##########
# Material map index
MATERIAL_MAP_ALBEDO = 0                         # Albedo material (same as: MATERIAL_MAP_DIFFUSE)
MATERIAL_MAP_METALNESS = 1                      # Metalness material (same as: MATERIAL_MAP_SPECULAR)
MATERIAL_MAP_NORMAL = 2                         # Normal material
MATERIAL_MAP_ROUGHNESS = 3                      # Roughness material
MATERIAL_MAP_OCCLUSION = 4                      # Ambient occlusion material
MATERIAL_MAP_EMISSION = 5                       # Emission material
MATERIAL_MAP_HEIGHT = 6                         # Heightmap material
MATERIAL_MAP_CUBEMAP = 7                        # Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_IRRADIANCE = 8                     # Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_PREFILTER = 9                      # Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_BRDF = 10                          # Brdf material

########## ShaderLocationIndex ##########
# Shader location index
SHADER_LOC_VERTEX_POSITION = 0                  # Shader location: vertex attribute: position
SHADER_LOC_VERTEX_TEXCOORD01 = 1                # Shader location: vertex attribute: texcoord01
SHADER_LOC_VERTEX_TEXCOORD02 = 2                # Shader location: vertex attribute: texcoord02
SHADER_LOC_VERTEX_NORMAL = 3                    # Shader location: vertex attribute: normal
SHADER_LOC_VERTEX_TANGENT = 4                   # Shader location: vertex attribute: tangent
SHADER_LOC_VERTEX_COLOR = 5                     # Shader location: vertex attribute: color
SHADER_LOC_MATRIX_MVP = 6                       # Shader location: matrix uniform: model-view-projection
SHADER_LOC_MATRIX_VIEW = 7                      # Shader location: matrix uniform: view (camera transform)
SHADER_LOC_MATRIX_PROJECTION = 8                # Shader location: matrix uniform: projection
SHADER_LOC_MATRIX_MODEL = 9                     # Shader location: matrix uniform: model (transform)
SHADER_LOC_MATRIX_NORMAL = 10                   # Shader location: matrix uniform: normal
SHADER_LOC_VECTOR_VIEW = 11                     # Shader location: vector uniform: view
SHADER_LOC_COLOR_DIFFUSE = 12                   # Shader location: vector uniform: diffuse color
SHADER_LOC_COLOR_SPECULAR = 13                  # Shader location: vector uniform: specular color
SHADER_LOC_COLOR_AMBIENT = 14                   # Shader location: vector uniform: ambient color
SHADER_LOC_MAP_ALBEDO = 15                      # Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
SHADER_LOC_MAP_METALNESS = 16                   # Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
SHADER_LOC_MAP_NORMAL = 17                      # Shader location: sampler2d texture: normal
SHADER_LOC_MAP_ROUGHNESS = 18                   # Shader location: sampler2d texture: roughness
SHADER_LOC_MAP_OCCLUSION = 19                   # Shader location: sampler2d texture: occlusion
SHADER_LOC_MAP_EMISSION = 20                    # Shader location: sampler2d texture: emission
SHADER_LOC_MAP_HEIGHT = 21                      # Shader location: sampler2d texture: height
SHADER_LOC_MAP_CUBEMAP = 22                     # Shader location: samplerCube texture: cubemap
SHADER_LOC_MAP_IRRADIANCE = 23                  # Shader location: samplerCube texture: irradiance
SHADER_LOC_MAP_PREFILTER = 24                   # Shader location: samplerCube texture: prefilter
SHADER_LOC_MAP_BRDF = 25                        # Shader location: sampler2d texture: brdf

########## ShaderUniformDataType ##########
# Shader uniform data type
SHADER_UNIFORM_FLOAT = 0                        # Shader uniform type: float
SHADER_UNIFORM_VEC2 = 1                         # Shader uniform type: vec2 (2 float)
SHADER_UNIFORM_VEC3 = 2                         # Shader uniform type: vec3 (3 float)
SHADER_UNIFORM_VEC4 = 3                         # Shader uniform type: vec4 (4 float)
SHADER_UNIFORM_INT = 4                          # Shader uniform type: int
SHADER_UNIFORM_IVEC2 = 5                        # Shader uniform type: ivec2 (2 int)
SHADER_UNIFORM_IVEC3 = 6                        # Shader uniform type: ivec3 (3 int)
SHADER_UNIFORM_IVEC4 = 7                        # Shader uniform type: ivec4 (4 int)
SHADER_UNIFORM_SAMPLER2D = 8                    # Shader uniform type: sampler2d

########## ShaderAttributeDataType ##########
# Shader attribute data types
SHADER_ATTRIB_FLOAT = 0                         # Shader attribute type: float
SHADER_ATTRIB_VEC2 = 1                          # Shader attribute type: vec2 (2 float)
SHADER_ATTRIB_VEC3 = 2                          # Shader attribute type: vec3 (3 float)
SHADER_ATTRIB_VEC4 = 3                          # Shader attribute type: vec4 (4 float)

########## PixelFormat ##########
# Pixel formats
PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1          # 8 bit per pixel (no alpha)
PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2         # 8*2 bpp (2 channels)
PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3             # 16 bpp
PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4             # 24 bpp
PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5           # 16 bpp (1 bit alpha)
PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6           # 16 bpp (4 bit alpha)
PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7           # 32 bpp
PIXELFORMAT_UNCOMPRESSED_R32 = 8                # 32 bpp (1 channel - float)
PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9          # 32*3 bpp (3 channels - float)
PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10      # 32*4 bpp (4 channels - float)
PIXELFORMAT_COMPRESSED_DXT1_RGB = 11            # 4 bpp (no alpha)
PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12           # 4 bpp (1 bit alpha)
PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13           # 8 bpp
PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14           # 8 bpp
PIXELFORMAT_COMPRESSED_ETC1_RGB = 15            # 4 bpp
PIXELFORMAT_COMPRESSED_ETC2_RGB = 16            # 4 bpp
PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17       # 8 bpp
PIXELFORMAT_COMPRESSED_PVRT_RGB = 18            # 4 bpp
PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19           # 4 bpp
PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20       # 8 bpp
PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21       # 2 bpp

########## TextureFilter ##########
# Texture parameters: filter mode
TEXTURE_FILTER_POINT = 0                        # No filter, just pixel approximation
TEXTURE_FILTER_BILINEAR = 1                     # Linear filtering
TEXTURE_FILTER_TRILINEAR = 2                    # Trilinear filtering (linear with mipmaps)
TEXTURE_FILTER_ANISOTROPIC_4X = 3               # Anisotropic filtering 4x
TEXTURE_FILTER_ANISOTROPIC_8X = 4               # Anisotropic filtering 8x
TEXTURE_FILTER_ANISOTROPIC_16X = 5              # Anisotropic filtering 16x

########## TextureWrap ##########
# Texture parameters: wrap mode
TEXTURE_WRAP_REPEAT = 0                         # Repeats texture in tiled mode
TEXTURE_WRAP_CLAMP = 1                          # Clamps texture to edge pixel in tiled mode
TEXTURE_WRAP_MIRROR_REPEAT = 2                  # Mirrors and repeats the texture in tiled mode
TEXTURE_WRAP_MIRROR_CLAMP = 3                   # Mirrors and clamps to border the texture in tiled mode

########## CubemapLayout ##########
# Cubemap layouts
CUBEMAP_LAYOUT_AUTO_DETECT = 0                  # Automatically detect layout type
CUBEMAP_LAYOUT_LINE_VERTICAL = 1                # Layout is defined by a vertical line with faces
CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2              # Layout is defined by a horizontal line with faces
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3          # Layout is defined by a 3x4 cross with cubemap faces
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4          # Layout is defined by a 4x3 cross with cubemap faces
CUBEMAP_LAYOUT_PANORAMA = 5                     # Layout is defined by a panorama image (equirrectangular map)

########## FontType ##########
# Font type, defines generation method
FONT_DEFAULT = 0                                # Default font generation, anti-aliased
FONT_BITMAP = 1                                 # Bitmap font generation, no anti-aliasing
FONT_SDF = 2                                    # SDF font generation, requires external shader

########## BlendMode ##########
# Color blending modes (pre-defined)
BLEND_ALPHA = 0                                 # Blend textures considering alpha (default)
BLEND_ADDITIVE = 1                              # Blend textures adding colors
BLEND_MULTIPLIED = 2                            # Blend textures multiplying colors
BLEND_ADD_COLORS = 3                            # Blend textures adding colors (alternative)
BLEND_SUBTRACT_COLORS = 4                       # Blend textures subtracting colors (alternative)
BLEND_ALPHA_PREMULTIPLY = 5                     # Blend premultiplied textures considering alpha
BLEND_CUSTOM = 6                                # Blend textures using custom src/dst factors (use rlSetBlendFactors())
BLEND_CUSTOM_SEPARATE = 7                       # Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendFactorsSeparate())

########## Gesture ##########
# Gesture
GESTURE_NONE = 0                                # No gesture
GESTURE_TAP = 1                                 # Tap gesture
GESTURE_DOUBLETAP = 2                           # Double tap gesture
GESTURE_HOLD = 4                                # Hold gesture
GESTURE_DRAG = 8                                # Drag gesture
GESTURE_SWIPE_RIGHT = 16                        # Swipe right gesture
GESTURE_SWIPE_LEFT = 32                         # Swipe left gesture
GESTURE_SWIPE_UP = 64                           # Swipe up gesture
GESTURE_SWIPE_DOWN = 128                        # Swipe down gesture
GESTURE_PINCH_IN = 256                          # Pinch in gesture
GESTURE_PINCH_OUT = 512                         # Pinch out gesture

########## CameraMode ##########
# Camera system modes
CAMERA_CUSTOM = 0                               # Custom camera
CAMERA_FREE = 1                                 # Free camera
CAMERA_ORBITAL = 2                              # Orbital camera
CAMERA_FIRST_PERSON = 3                         # First person camera
CAMERA_THIRD_PERSON = 4                         # Third person camera

########## CameraProjection ##########
# Camera projection
CAMERA_PERSPECTIVE = 0                          # Perspective projection
CAMERA_ORTHOGRAPHIC = 1                         # Orthographic projection

########## NPatchLayout ##########
# N-patch layout
NPATCH_NINE_PATCH = 0                           # Npatch layout: 3x3 tiles
NPATCH_THREE_PATCH_VERTICAL = 1                 # Npatch layout: 1x3 tiles
NPATCH_THREE_PATCH_HORIZONTAL = 2               # Npatch layout: 3x1 tiles


class _wrapped__Matrix:
    m0: float                           # `float`: Matrix first row (4 components)
    m4: float                           # `float`: Matrix first row (4 components)
    m8: float                           # `float`: Matrix first row (4 components)
    m12: float                          # `float`: Matrix first row (4 components)
    m1: float                           # `float`: Matrix second row (4 components)
    m5: float                           # `float`: Matrix second row (4 components)
    m9: float                           # `float`: Matrix second row (4 components)
    m13: float                          # `float`: Matrix second row (4 components)
    m2: float                           # `float`: Matrix third row (4 components)
    m6: float                           # `float`: Matrix third row (4 components)
    m10: float                          # `float`: Matrix third row (4 components)
    m14: float                          # `float`: Matrix third row (4 components)
    m3: float                           # `float`: Matrix fourth row (4 components)
    m7: float                           # `float`: Matrix fourth row (4 components)
    m11: float                          # `float`: Matrix fourth row (4 components)
    m15: float                          # `float`: Matrix fourth row (4 components)

class Matrix(_StructLike[Matrix], _wrapped__Matrix):
    """Matrix, 4x4 components, column major, OpenGL style, right-handed"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, m0: float, m4: float, m8: float, m12: float, m1: float, m5: float, m9: float, m13: float, m2: float, m6: float, m10: float, m14: float, m3: float, m7: float, m11: float, m15: float): ...

class Matrix_p(Pointer[Matrix], _wrapped__Matrix):
    """Wraps `Matrix *`"""

class _wrapped__Color:
    r: int                              # `unsigned char`: Color red value
    g: int                              # `unsigned char`: Color green value
    b: int                              # `unsigned char`: Color blue value
    a: int                              # `unsigned char`: Color alpha value

class Color(_StructLike[Color], _wrapped__Color):
    """Color, 4 components, R8G8B8A8 (32bit)"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, r: int, g: int, b: int, a: int): ...

class Color_p(Pointer[Color], _wrapped__Color):
    """Wraps `Color *`"""

class _wrapped__Rectangle:
    x: float                            # `float`: Rectangle top-left corner position x
    y: float                            # `float`: Rectangle top-left corner position y
    width: float                        # `float`: Rectangle width
    height: float                       # `float`: Rectangle height

class Rectangle(_StructLike[Rectangle], _wrapped__Rectangle):
    """Rectangle, 4 components"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, x: float, y: float, width: float, height: float): ...

class Rectangle_p(Pointer[Rectangle], _wrapped__Rectangle):
    """Wraps `Rectangle *`"""

class _wrapped__Image:
    data: void_p                        # `void *`: Image raw data
    width: int                          # `int`: Image base width
    height: int                         # `int`: Image base height
    mipmaps: int                        # `int`: Mipmap levels, 1 by default
    format: int                         # `int`: Data format (PixelFormat type)

class Image(_StructLike[Image], _wrapped__Image):
    """Image, pixel data stored in CPU memory (RAM)"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, data: void_p, width: int, height: int, mipmaps: int, format: int): ...

class Image_p(Pointer[Image], _wrapped__Image):
    """Wraps `Image *`"""

class _wrapped__Texture:
    id: int                             # `unsigned int`: OpenGL texture id
    width: int                          # `int`: Texture base width
    height: int                         # `int`: Texture base height
    mipmaps: int                        # `int`: Mipmap levels, 1 by default
    format: int                         # `int`: Data format (PixelFormat type)

class Texture(_StructLike[Texture], _wrapped__Texture):
    """Texture, tex data stored in GPU memory (VRAM)"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: int, width: int, height: int, mipmaps: int, format: int): ...

class Texture_p(Pointer[Texture], _wrapped__Texture):
    """Wraps `Texture *`"""

class _wrapped__RenderTexture:
    id: int                             # `unsigned int`: OpenGL framebuffer object id
    texture: Texture                    # `Texture`: Color buffer attachment texture
    depth: Texture                      # `Texture`: Depth buffer attachment texture

class RenderTexture(_StructLike[RenderTexture], _wrapped__RenderTexture):
    """RenderTexture, fbo for texture rendering"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: int, texture: Texture, depth: Texture): ...

class RenderTexture_p(Pointer[RenderTexture], _wrapped__RenderTexture):
    """Wraps `RenderTexture *`"""

class _wrapped__NPatchInfo:
    source: Rectangle                   # `Rectangle`: Texture source rectangle
    left: int                           # `int`: Left border offset
    top: int                            # `int`: Top border offset
    right: int                          # `int`: Right border offset
    bottom: int                         # `int`: Bottom border offset
    layout: int                         # `int`: Layout of the n-patch: 3x3, 1x3 or 3x1

class NPatchInfo(_StructLike[NPatchInfo], _wrapped__NPatchInfo):
    """NPatchInfo, n-patch layout info"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, source: Rectangle, left: int, top: int, right: int, bottom: int, layout: int): ...

class NPatchInfo_p(Pointer[NPatchInfo], _wrapped__NPatchInfo):
    """Wraps `NPatchInfo *`"""

class _wrapped__GlyphInfo:
    value: int                          # `int`: Character value (Unicode)
    offsetX: int                        # `int`: Character offset X when drawing
    offsetY: int                        # `int`: Character offset Y when drawing
    advanceX: int                       # `int`: Character advance position X
    image: Image                        # `Image`: Character image data

class GlyphInfo(_StructLike[GlyphInfo], _wrapped__GlyphInfo):
    """GlyphInfo, font characters glyphs info"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: int, offsetX: int, offsetY: int, advanceX: int, image: Image): ...

class GlyphInfo_p(Pointer[GlyphInfo], _wrapped__GlyphInfo):
    """Wraps `GlyphInfo *`"""

class _wrapped__Font:
    baseSize: int                       # `int`: Base size (default chars height)
    glyphCount: int                     # `int`: Number of glyph characters
    glyphPadding: int                   # `int`: Padding around the glyph characters
    texture: Texture2D                  # `Texture2D`: Texture atlas containing the glyphs
    recs: 'Rectangle_p'                 # `Rectangle *`: Rectangles in texture for the glyphs
    glyphs: 'GlyphInfo_p'               # `GlyphInfo *`: Glyphs info data

class Font(_StructLike[Font], _wrapped__Font):
    """Font, font texture and GlyphInfo array data"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, baseSize: int, glyphCount: int, glyphPadding: int, texture: Texture2D, recs: 'Rectangle_p', glyphs: 'GlyphInfo_p'): ...

class Font_p(Pointer[Font], _wrapped__Font):
    """Wraps `Font *`"""

class _wrapped__Camera3D:
    position: vec3                      # `Vector3`: Camera position
    target: vec3                        # `Vector3`: Camera target it looks-at
    up: vec3                            # `Vector3`: Camera up vector (rotation over its axis)
    fovy: float                         # `float`: Camera field-of-view aperture in Y (degrees) in perspective, used as near plane width in orthographic
    projection: int                     # `int`: Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC

class Camera3D(_StructLike[Camera3D], _wrapped__Camera3D):
    """Camera, defines position/orientation in 3d space"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, position: vec3, target: vec3, up: vec3, fovy: float, projection: int): ...

class Camera3D_p(Pointer[Camera3D], _wrapped__Camera3D):
    """Wraps `Camera3D *`"""

class _wrapped__Camera2D:
    offset: vec2                        # `Vector2`: Camera offset (displacement from target)
    target: vec2                        # `Vector2`: Camera target (rotation and zoom origin)
    rotation: float                     # `float`: Camera rotation in degrees
    zoom: float                         # `float`: Camera zoom (scaling), should be 1.0f by default

class Camera2D(_StructLike[Camera2D], _wrapped__Camera2D):
    """Camera2D, defines position/orientation in 2d space"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, offset: vec2, target: vec2, rotation: float, zoom: float): ...

class Camera2D_p(Pointer[Camera2D], _wrapped__Camera2D):
    """Wraps `Camera2D *`"""

class _wrapped__Mesh:
    vertexCount: int                    # `int`: Number of vertices stored in arrays
    triangleCount: int                  # `int`: Number of triangles stored (indexed or not)
    vertices: float_p                   # `float *`: Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
    texcoords: float_p                  # `float *`: Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
    texcoords2: float_p                 # `float *`: Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
    normals: float_p                    # `float *`: Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
    tangents: float_p                   # `float *`: Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
    colors: uchar_p                     # `unsigned char *`: Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
    indices: ushort_p                   # `unsigned short *`: Vertex indices (in case vertex data comes indexed)
    animVertices: float_p               # `float *`: Animated vertex positions (after bones transformations)
    animNormals: float_p                # `float *`: Animated normals (after bones transformations)
    boneIds: uchar_p                    # `unsigned char *`: Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
    boneWeights: float_p                # `float *`: Vertex bone weight, up to 4 bones influence by vertex (skinning)
    vaoId: int                          # `unsigned int`: OpenGL Vertex Array Object id
    vboId: uint_p                       # `unsigned int *`: OpenGL Vertex Buffer Objects id (default vertex data)

class Mesh(_StructLike[Mesh], _wrapped__Mesh):
    """Mesh, vertex data and vao/vbo"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, vertexCount: int, triangleCount: int, vertices: float_p, texcoords: float_p, texcoords2: float_p, normals: float_p, tangents: float_p, colors: uchar_p, indices: ushort_p, animVertices: float_p, animNormals: float_p, boneIds: uchar_p, boneWeights: float_p, vaoId: int, vboId: uint_p): ...

class Mesh_p(Pointer[Mesh], _wrapped__Mesh):
    """Wraps `Mesh *`"""

class _wrapped__Shader:
    id: int                             # `unsigned int`: Shader program id
    locs: int_p                         # `int *`: Shader locations array (RL_MAX_SHADER_LOCATIONS)

class Shader(_StructLike[Shader], _wrapped__Shader):
    """Shader"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: int, locs: int_p): ...

class Shader_p(Pointer[Shader], _wrapped__Shader):
    """Wraps `Shader *`"""

class _wrapped__MaterialMap:
    texture: Texture2D                  # `Texture2D`: Material map texture
    color: Color                        # `Color`: Material map color
    value: float                        # `float`: Material map value

class MaterialMap(_StructLike[MaterialMap], _wrapped__MaterialMap):
    """MaterialMap"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, texture: Texture2D, color: Color, value: float): ...

class MaterialMap_p(Pointer[MaterialMap], _wrapped__MaterialMap):
    """Wraps `MaterialMap *`"""

class _wrapped__Material:
    shader: Shader                      # `Shader`: Material shader
    maps: 'MaterialMap_p'               # `MaterialMap *`: Material maps array (MAX_MATERIAL_MAPS)
    params: float_p                     # `float[4]`: Material generic parameters (if required)

class Material(_StructLike[Material], _wrapped__Material):
    """Material, includes shader and maps"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, shader: Shader, maps: 'MaterialMap_p', params: float_p): ...

class Material_p(Pointer[Material], _wrapped__Material):
    """Wraps `Material *`"""

class _wrapped__Transform:
    translation: vec3                   # `Vector3`: Translation
    rotation: Quaternion                # `Quaternion`: Rotation
    scale: vec3                         # `Vector3`: Scale

class Transform(_StructLike[Transform], _wrapped__Transform):
    """Transform, vertex transformation data"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, translation: vec3, rotation: Quaternion, scale: vec3): ...

class Transform_p(Pointer[Transform], _wrapped__Transform):
    """Wraps `Transform *`"""

class _wrapped__BoneInfo:
    name: char_p                        # `char[32]`: Bone name
    parent: int                         # `int`: Bone parent

class BoneInfo(_StructLike[BoneInfo], _wrapped__BoneInfo):
    """Bone, skeletal animation bone"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: char_p, parent: int): ...

class BoneInfo_p(Pointer[BoneInfo], _wrapped__BoneInfo):
    """Wraps `BoneInfo *`"""

class _wrapped__Model:
    transform: Matrix                   # `Matrix`: Local transform matrix
    meshCount: int                      # `int`: Number of meshes
    materialCount: int                  # `int`: Number of materials
    meshes: 'Mesh_p'                    # `Mesh *`: Meshes array
    materials: 'Material_p'             # `Material *`: Materials array
    meshMaterial: int_p                 # `int *`: Mesh material number
    boneCount: int                      # `int`: Number of bones
    bones: 'BoneInfo_p'                 # `BoneInfo *`: Bones information (skeleton)
    bindPose: 'Transform_p'             # `Transform *`: Bones base transformation (pose)

class Model(_StructLike[Model], _wrapped__Model):
    """Model, meshes, materials and animation data"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, transform: Matrix, meshCount: int, materialCount: int, meshes: 'Mesh_p', materials: 'Material_p', meshMaterial: int_p, boneCount: int, bones: 'BoneInfo_p', bindPose: 'Transform_p'): ...

class Model_p(Pointer[Model], _wrapped__Model):
    """Wraps `Model *`"""

class _wrapped__ModelAnimation:
    boneCount: int                      # `int`: Number of bones
    frameCount: int                     # `int`: Number of animation frames
    bones: 'BoneInfo_p'                 # `BoneInfo *`: Bones information (skeleton)
    framePoses: void_p                  # `Transform **`: Poses array by frame
    name: char_p                        # `char[32]`: Animation name

class ModelAnimation(_StructLike[ModelAnimation], _wrapped__ModelAnimation):
    """ModelAnimation"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, boneCount: int, frameCount: int, bones: 'BoneInfo_p', framePoses: void_p, name: char_p): ...

class ModelAnimation_p(Pointer[ModelAnimation], _wrapped__ModelAnimation):
    """Wraps `ModelAnimation *`"""

class _wrapped__Ray:
    position: vec3                      # `Vector3`: Ray position (origin)
    direction: vec3                     # `Vector3`: Ray direction

class Ray(_StructLike[Ray], _wrapped__Ray):
    """Ray, ray for raycasting"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, position: vec3, direction: vec3): ...

class Ray_p(Pointer[Ray], _wrapped__Ray):
    """Wraps `Ray *`"""

class _wrapped__RayCollision:
    hit: bool                           # `bool`: Did the ray hit something?
    distance: float                     # `float`: Distance to the nearest hit
    point: vec3                         # `Vector3`: Point of the nearest hit
    normal: vec3                        # `Vector3`: Surface normal of hit

class RayCollision(_StructLike[RayCollision], _wrapped__RayCollision):
    """RayCollision, ray hit information"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, hit: bool, distance: float, point: vec3, normal: vec3): ...

class RayCollision_p(Pointer[RayCollision], _wrapped__RayCollision):
    """Wraps `RayCollision *`"""

class _wrapped__BoundingBox:
    min: vec3                           # `Vector3`: Minimum vertex box-corner
    max: vec3                           # `Vector3`: Maximum vertex box-corner

class BoundingBox(_StructLike[BoundingBox], _wrapped__BoundingBox):
    """BoundingBox"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, min: vec3, max: vec3): ...

class BoundingBox_p(Pointer[BoundingBox], _wrapped__BoundingBox):
    """Wraps `BoundingBox *`"""

class _wrapped__Wave:
    frameCount: int                     # `unsigned int`: Total number of frames (considering channels)
    sampleRate: int                     # `unsigned int`: Frequency (samples per second)
    sampleSize: int                     # `unsigned int`: Bit depth (bits per sample): 8, 16, 32 (24 not supported)
    channels: int                       # `unsigned int`: Number of channels (1-mono, 2-stereo, ...)
    data: void_p                        # `void *`: Buffer data pointer

class Wave(_StructLike[Wave], _wrapped__Wave):
    """Wave, audio wave data"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, frameCount: int, sampleRate: int, sampleSize: int, channels: int, data: void_p): ...

class Wave_p(Pointer[Wave], _wrapped__Wave):
    """Wraps `Wave *`"""

class _wrapped__AudioStream:
    buffer: void_p                      # `rAudioBuffer *`: Pointer to internal data used by the audio system
    processor: void_p                   # `rAudioProcessor *`: Pointer to internal data processor, useful for audio effects
    sampleRate: int                     # `unsigned int`: Frequency (samples per second)
    sampleSize: int                     # `unsigned int`: Bit depth (bits per sample): 8, 16, 32 (24 not supported)
    channels: int                       # `unsigned int`: Number of channels (1-mono, 2-stereo, ...)

class AudioStream(_StructLike[AudioStream], _wrapped__AudioStream):
    """AudioStream, custom audio stream"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, buffer: void_p, processor: void_p, sampleRate: int, sampleSize: int, channels: int): ...

class AudioStream_p(Pointer[AudioStream], _wrapped__AudioStream):
    """Wraps `AudioStream *`"""

class _wrapped__Sound:
    stream: AudioStream                 # `AudioStream`: Audio stream
    frameCount: int                     # `unsigned int`: Total number of frames (considering channels)

class Sound(_StructLike[Sound], _wrapped__Sound):
    """Sound"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, stream: AudioStream, frameCount: int): ...

class Sound_p(Pointer[Sound], _wrapped__Sound):
    """Wraps `Sound *`"""

class _wrapped__Music:
    stream: AudioStream                 # `AudioStream`: Audio stream
    frameCount: int                     # `unsigned int`: Total number of frames (considering channels)
    looping: bool                       # `bool`: Music looping enable
    ctxType: int                        # `int`: Type of music context (audio filetype)
    ctxData: void_p                     # `void *`: Audio context data, depends on type

class Music(_StructLike[Music], _wrapped__Music):
    """Music, audio stream, anything longer than ~10 seconds should be streamed"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, stream: AudioStream, frameCount: int, looping: bool, ctxType: int, ctxData: void_p): ...

class Music_p(Pointer[Music], _wrapped__Music):
    """Wraps `Music *`"""

class _wrapped__VrDeviceInfo:
    hResolution: int                    # `int`: Horizontal resolution in pixels
    vResolution: int                    # `int`: Vertical resolution in pixels
    hScreenSize: float                  # `float`: Horizontal size in meters
    vScreenSize: float                  # `float`: Vertical size in meters
    vScreenCenter: float                # `float`: Screen center in meters
    eyeToScreenDistance: float          # `float`: Distance between eye and display in meters
    lensSeparationDistance: float       # `float`: Lens separation distance in meters
    interpupillaryDistance: float       # `float`: IPD (distance between pupils) in meters
    lensDistortionValues: float_p       # `float[4]`: Lens distortion constant parameters
    chromaAbCorrection: float_p         # `float[4]`: Chromatic aberration correction parameters

class VrDeviceInfo(_StructLike[VrDeviceInfo], _wrapped__VrDeviceInfo):
    """VrDeviceInfo, Head-Mounted-Display device parameters"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, hResolution: int, vResolution: int, hScreenSize: float, vScreenSize: float, vScreenCenter: float, eyeToScreenDistance: float, lensSeparationDistance: float, interpupillaryDistance: float, lensDistortionValues: float_p, chromaAbCorrection: float_p): ...

class VrDeviceInfo_p(Pointer[VrDeviceInfo], _wrapped__VrDeviceInfo):
    """Wraps `VrDeviceInfo *`"""

class _wrapped__VrStereoConfig:
    projection: 'Matrix_p'              # `Matrix[2]`: VR projection matrices (per eye)
    viewOffset: 'Matrix_p'              # `Matrix[2]`: VR view offset matrices (per eye)
    leftLensCenter: float_p             # `float[2]`: VR left lens center
    rightLensCenter: float_p            # `float[2]`: VR right lens center
    leftScreenCenter: float_p           # `float[2]`: VR left screen center
    rightScreenCenter: float_p          # `float[2]`: VR right screen center
    scale: float_p                      # `float[2]`: VR distortion scale
    scaleIn: float_p                    # `float[2]`: VR distortion scale in

class VrStereoConfig(_StructLike[VrStereoConfig], _wrapped__VrStereoConfig):
    """VrStereoConfig, VR stereo rendering configuration for simulator"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, projection: 'Matrix_p', viewOffset: 'Matrix_p', leftLensCenter: float_p, rightLensCenter: float_p, leftScreenCenter: float_p, rightScreenCenter: float_p, scale: float_p, scaleIn: float_p): ...

class VrStereoConfig_p(Pointer[VrStereoConfig], _wrapped__VrStereoConfig):
    """Wraps `VrStereoConfig *`"""

class _wrapped__FilePathList:
    capacity: int                       # `unsigned int`: Filepaths max entries
    count: int                          # `unsigned int`: Filepaths entries count
    paths: void_p                       # `char **`: Filepaths entries

class FilePathList(_StructLike[FilePathList], _wrapped__FilePathList):
    """File path list"""
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int, count: int, paths: void_p): ...

class FilePathList_p(Pointer[FilePathList], _wrapped__FilePathList):
    """Wraps `FilePathList *`"""

# Quaternion, 4 components (Vector4 alias)
Quaternion = vec4
Quaternion_p = vec4_p

# Texture2D, same as Texture
Texture2D = Texture
Texture2D_p = Texture_p

# TextureCubemap, same as Texture
TextureCubemap = Texture
TextureCubemap_p = Texture_p

# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture
RenderTexture2D_p = RenderTexture_p

# Camera type fallback, defaults to Camera3D
Camera = Camera3D
Camera_p = Camera3D_p

def InitWindow(width: int, height: int, title: str) -> None:
    """Initialize window and OpenGL context

    Wraps: `void InitWindow(int width, int height, const char * title)`
    """

def WindowShouldClose() -> bool:
    """Check if KEY_ESCAPE pressed or Close icon pressed

    Wraps: `bool WindowShouldClose()`
    """

def CloseWindow() -> None:
    """Close window and unload OpenGL context

    Wraps: `void CloseWindow()`
    """

def IsWindowReady() -> bool:
    """Check if window has been initialized successfully

    Wraps: `bool IsWindowReady()`
    """

def IsWindowFullscreen() -> bool:
    """Check if window is currently fullscreen

    Wraps: `bool IsWindowFullscreen()`
    """

def IsWindowHidden() -> bool:
    """Check if window is currently hidden (only PLATFORM_DESKTOP)

    Wraps: `bool IsWindowHidden()`
    """

def IsWindowMinimized() -> bool:
    """Check if window is currently minimized (only PLATFORM_DESKTOP)

    Wraps: `bool IsWindowMinimized()`
    """

def IsWindowMaximized() -> bool:
    """Check if window is currently maximized (only PLATFORM_DESKTOP)

    Wraps: `bool IsWindowMaximized()`
    """

def IsWindowFocused() -> bool:
    """Check if window is currently focused (only PLATFORM_DESKTOP)

    Wraps: `bool IsWindowFocused()`
    """

def IsWindowResized() -> bool:
    """Check if window has been resized last frame

    Wraps: `bool IsWindowResized()`
    """

def IsWindowState(flag: int) -> bool:
    """Check if one specific window flag is enabled

    Wraps: `bool IsWindowState(unsigned int flag)`
    """

def SetWindowState(flags: int) -> None:
    """Set window configuration state using flags (only PLATFORM_DESKTOP)

    Wraps: `void SetWindowState(unsigned int flags)`
    """

def ClearWindowState(flags: int) -> None:
    """Clear window configuration state flags

    Wraps: `void ClearWindowState(unsigned int flags)`
    """

def ToggleFullscreen() -> None:
    """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)

    Wraps: `void ToggleFullscreen()`
    """

def MaximizeWindow() -> None:
    """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)

    Wraps: `void MaximizeWindow()`
    """

def MinimizeWindow() -> None:
    """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)

    Wraps: `void MinimizeWindow()`
    """

def RestoreWindow() -> None:
    """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)

    Wraps: `void RestoreWindow()`
    """

def SetWindowIcon(image: Image) -> None:
    """Set icon for window (single image, RGBA 32bit, only PLATFORM_DESKTOP)

    Wraps: `void SetWindowIcon(Image image)`
    """

def SetWindowIcons(images: 'Image_p', count: int) -> None:
    """Set icon for window (multiple images, RGBA 32bit, only PLATFORM_DESKTOP)

    Wraps: `void SetWindowIcons(Image * images, int count)`
    """

def SetWindowTitle(title: str) -> None:
    """Set title for window (only PLATFORM_DESKTOP)

    Wraps: `void SetWindowTitle(const char * title)`
    """

def SetWindowPosition(x: int, y: int) -> None:
    """Set window position on screen (only PLATFORM_DESKTOP)

    Wraps: `void SetWindowPosition(int x, int y)`
    """

def SetWindowMonitor(monitor: int) -> None:
    """Set monitor for the current window (fullscreen mode)

    Wraps: `void SetWindowMonitor(int monitor)`
    """

def SetWindowMinSize(width: int, height: int) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)

    Wraps: `void SetWindowMinSize(int width, int height)`
    """

def SetWindowSize(width: int, height: int) -> None:
    """Set window dimensions

    Wraps: `void SetWindowSize(int width, int height)`
    """

def SetWindowOpacity(opacity: float) -> None:
    """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)

    Wraps: `void SetWindowOpacity(float opacity)`
    """

def GetWindowHandle() -> void_p:
    """Get native window handle

    Wraps: `void * GetWindowHandle()`
    """

def GetScreenWidth() -> int:
    """Get current screen width

    Wraps: `int GetScreenWidth()`
    """

def GetScreenHeight() -> int:
    """Get current screen height

    Wraps: `int GetScreenHeight()`
    """

def GetRenderWidth() -> int:
    """Get current render width (it considers HiDPI)

    Wraps: `int GetRenderWidth()`
    """

def GetRenderHeight() -> int:
    """Get current render height (it considers HiDPI)

    Wraps: `int GetRenderHeight()`
    """

def GetMonitorCount() -> int:
    """Get number of connected monitors

    Wraps: `int GetMonitorCount()`
    """

def GetCurrentMonitor() -> int:
    """Get current connected monitor

    Wraps: `int GetCurrentMonitor()`
    """

def GetMonitorPosition(monitor: int) -> vec2:
    """Get specified monitor position

    Wraps: `Vector2 GetMonitorPosition(int monitor)`
    """

def GetMonitorWidth(monitor: int) -> int:
    """Get specified monitor width (current video mode used by monitor)

    Wraps: `int GetMonitorWidth(int monitor)`
    """

def GetMonitorHeight(monitor: int) -> int:
    """Get specified monitor height (current video mode used by monitor)

    Wraps: `int GetMonitorHeight(int monitor)`
    """

def GetMonitorPhysicalWidth(monitor: int) -> int:
    """Get specified monitor physical width in millimetres

    Wraps: `int GetMonitorPhysicalWidth(int monitor)`
    """

def GetMonitorPhysicalHeight(monitor: int) -> int:
    """Get specified monitor physical height in millimetres

    Wraps: `int GetMonitorPhysicalHeight(int monitor)`
    """

def GetMonitorRefreshRate(monitor: int) -> int:
    """Get specified monitor refresh rate

    Wraps: `int GetMonitorRefreshRate(int monitor)`
    """

def GetWindowPosition() -> vec2:
    """Get window position XY on monitor

    Wraps: `Vector2 GetWindowPosition()`
    """

def GetWindowScaleDPI() -> vec2:
    """Get window scale DPI factor

    Wraps: `Vector2 GetWindowScaleDPI()`
    """

def GetMonitorName(monitor: int) -> str:
    """Get the human-readable, UTF-8 encoded name of the primary monitor

    Wraps: `const char * GetMonitorName(int monitor)`
    """

def SetClipboardText(text: str) -> None:
    """Set clipboard text content

    Wraps: `void SetClipboardText(const char * text)`
    """

def GetClipboardText() -> str:
    """Get clipboard text content

    Wraps: `const char * GetClipboardText()`
    """

def EnableEventWaiting() -> None:
    """Enable waiting for events on EndDrawing(), no automatic event polling

    Wraps: `void EnableEventWaiting()`
    """

def DisableEventWaiting() -> None:
    """Disable waiting for events on EndDrawing(), automatic events polling

    Wraps: `void DisableEventWaiting()`
    """

def SwapScreenBuffer() -> None:
    """Swap back buffer with front buffer (screen drawing)

    Wraps: `void SwapScreenBuffer()`
    """

def PollInputEvents() -> None:
    """Register all input events

    Wraps: `void PollInputEvents()`
    """

def WaitTime(seconds: float) -> None:
    """Wait for some time (halt program execution)

    Wraps: `void WaitTime(double seconds)`
    """

def ShowCursor() -> None:
    """Shows cursor

    Wraps: `void ShowCursor()`
    """

def HideCursor() -> None:
    """Hides cursor

    Wraps: `void HideCursor()`
    """

def IsCursorHidden() -> bool:
    """Check if cursor is not visible

    Wraps: `bool IsCursorHidden()`
    """

def EnableCursor() -> None:
    """Enables cursor (unlock cursor)

    Wraps: `void EnableCursor()`
    """

def DisableCursor() -> None:
    """Disables cursor (lock cursor)

    Wraps: `void DisableCursor()`
    """

def IsCursorOnScreen() -> bool:
    """Check if cursor is on the screen

    Wraps: `bool IsCursorOnScreen()`
    """

def ClearBackground(color: Color) -> None:
    """Set background color (framebuffer clear color)

    Wraps: `void ClearBackground(Color color)`
    """

def BeginDrawing() -> None:
    """Setup canvas (framebuffer) to start drawing

    Wraps: `void BeginDrawing()`
    """

def EndDrawing() -> None:
    """End canvas drawing and swap buffers (double buffering)

    Wraps: `void EndDrawing()`
    """

def BeginMode2D(camera: Camera2D) -> None:
    """Begin 2D mode with custom camera (2D)

    Wraps: `void BeginMode2D(Camera2D camera)`
    """

def EndMode2D() -> None:
    """Ends 2D mode with custom camera

    Wraps: `void EndMode2D()`
    """

def BeginMode3D(camera: Camera3D) -> None:
    """Begin 3D mode with custom camera (3D)

    Wraps: `void BeginMode3D(Camera3D camera)`
    """

def EndMode3D() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode

    Wraps: `void EndMode3D()`
    """

def BeginTextureMode(target: RenderTexture2D) -> None:
    """Begin drawing to render texture

    Wraps: `void BeginTextureMode(RenderTexture2D target)`
    """

def EndTextureMode() -> None:
    """Ends drawing to render texture

    Wraps: `void EndTextureMode()`
    """

def BeginShaderMode(shader: Shader) -> None:
    """Begin custom shader drawing

    Wraps: `void BeginShaderMode(Shader shader)`
    """

def EndShaderMode() -> None:
    """End custom shader drawing (use default shader)

    Wraps: `void EndShaderMode()`
    """

def BeginBlendMode(mode: int) -> None:
    """Begin blending mode (alpha, additive, multiplied, subtract, custom)

    Wraps: `void BeginBlendMode(int mode)`
    """

def EndBlendMode() -> None:
    """End blending mode (reset to default: alpha blending)

    Wraps: `void EndBlendMode()`
    """

def BeginScissorMode(x: int, y: int, width: int, height: int) -> None:
    """Begin scissor mode (define screen area for following drawing)

    Wraps: `void BeginScissorMode(int x, int y, int width, int height)`
    """

def EndScissorMode() -> None:
    """End scissor mode

    Wraps: `void EndScissorMode()`
    """

def BeginVrStereoMode(config: VrStereoConfig) -> None:
    """Begin stereo rendering (requires VR simulator)

    Wraps: `void BeginVrStereoMode(VrStereoConfig config)`
    """

def EndVrStereoMode() -> None:
    """End stereo rendering (requires VR simulator)

    Wraps: `void EndVrStereoMode()`
    """

def LoadVrStereoConfig(device: VrDeviceInfo) -> VrStereoConfig:
    """Load VR stereo config for VR simulator device parameters

    Wraps: `VrStereoConfig LoadVrStereoConfig(VrDeviceInfo device)`
    """

def UnloadVrStereoConfig(config: VrStereoConfig) -> None:
    """Unload VR stereo config

    Wraps: `void UnloadVrStereoConfig(VrStereoConfig config)`
    """

def LoadShader(vsFileName: str, fsFileName: str) -> Shader:
    """Load shader from files and bind default locations

    Wraps: `Shader LoadShader(const char * vsFileName, const char * fsFileName)`
    """

def LoadShaderFromMemory(vsCode: str, fsCode: str) -> Shader:
    """Load shader from code strings and bind default locations

    Wraps: `Shader LoadShaderFromMemory(const char * vsCode, const char * fsCode)`
    """

def IsShaderReady(shader: Shader) -> bool:
    """Check if a shader is ready

    Wraps: `bool IsShaderReady(Shader shader)`
    """

def GetShaderLocation(shader: Shader, uniformName: str) -> int:
    """Get shader uniform location

    Wraps: `int GetShaderLocation(Shader shader, const char * uniformName)`
    """

def GetShaderLocationAttrib(shader: Shader, attribName: str) -> int:
    """Get shader attribute location

    Wraps: `int GetShaderLocationAttrib(Shader shader, const char * attribName)`
    """

def SetShaderValue(shader: Shader, locIndex: int, value: void_p, uniformType: int) -> None:
    """Set shader uniform value

    Wraps: `void SetShaderValue(Shader shader, int locIndex, const void * value, int uniformType)`
    """

def SetShaderValueV(shader: Shader, locIndex: int, value: void_p, uniformType: int, count: int) -> None:
    """Set shader uniform value vector

    Wraps: `void SetShaderValueV(Shader shader, int locIndex, const void * value, int uniformType, int count)`
    """

def SetShaderValueMatrix(shader: Shader, locIndex: int, mat: Matrix) -> None:
    """Set shader uniform value (matrix 4x4)

    Wraps: `void SetShaderValueMatrix(Shader shader, int locIndex, Matrix mat)`
    """

def SetShaderValueTexture(shader: Shader, locIndex: int, texture: Texture2D) -> None:
    """Set shader uniform value for texture (sampler2d)

    Wraps: `void SetShaderValueTexture(Shader shader, int locIndex, Texture2D texture)`
    """

def UnloadShader(shader: Shader) -> None:
    """Unload shader from GPU memory (VRAM)

    Wraps: `void UnloadShader(Shader shader)`
    """

def GetMouseRay(mousePosition: vec2, camera: Camera) -> Ray:
    """Get a ray trace from mouse position

    Wraps: `Ray GetMouseRay(Vector2 mousePosition, Camera camera)`
    """

def GetCameraMatrix(camera: Camera) -> Matrix:
    """Get camera transform matrix (view matrix)

    Wraps: `Matrix GetCameraMatrix(Camera camera)`
    """

def GetCameraMatrix2D(camera: Camera2D) -> Matrix:
    """Get camera 2d transform matrix

    Wraps: `Matrix GetCameraMatrix2D(Camera2D camera)`
    """

def GetWorldToScreen(position: vec3, camera: Camera) -> vec2:
    """Get the screen space position for a 3d world space position

    Wraps: `Vector2 GetWorldToScreen(Vector3 position, Camera camera)`
    """

def GetScreenToWorld2D(position: vec2, camera: Camera2D) -> vec2:
    """Get the world space position for a 2d camera screen space position

    Wraps: `Vector2 GetScreenToWorld2D(Vector2 position, Camera2D camera)`
    """

def GetWorldToScreenEx(position: vec3, camera: Camera, width: int, height: int) -> vec2:
    """Get size position for a 3d world space position

    Wraps: `Vector2 GetWorldToScreenEx(Vector3 position, Camera camera, int width, int height)`
    """

def GetWorldToScreen2D(position: vec2, camera: Camera2D) -> vec2:
    """Get the screen space position for a 2d camera world space position

    Wraps: `Vector2 GetWorldToScreen2D(Vector2 position, Camera2D camera)`
    """

def SetTargetFPS(fps: int) -> None:
    """Set target FPS (maximum)

    Wraps: `void SetTargetFPS(int fps)`
    """

def GetFPS() -> int:
    """Get current FPS

    Wraps: `int GetFPS()`
    """

def GetFrameTime() -> float:
    """Get time in seconds for last frame drawn (delta time)

    Wraps: `float GetFrameTime()`
    """

def GetTime() -> float:
    """Get elapsed time in seconds since InitWindow()

    Wraps: `double GetTime()`
    """

def IsKeyPressed(key: int) -> bool:
    """Check if a key has been pressed once

    Wraps: `bool IsKeyPressed(int key)`
    """

def IsKeyDown(key: int) -> bool:
    """Check if a key is being pressed

    Wraps: `bool IsKeyDown(int key)`
    """

def IsKeyReleased(key: int) -> bool:
    """Check if a key has been released once

    Wraps: `bool IsKeyReleased(int key)`
    """

def IsKeyUp(key: int) -> bool:
    """Check if a key is NOT being pressed

    Wraps: `bool IsKeyUp(int key)`
    """

def SetExitKey(key: int) -> None:
    """Set a custom key to exit program (default is ESC)

    Wraps: `void SetExitKey(int key)`
    """

def GetKeyPressed() -> int:
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty

    Wraps: `int GetKeyPressed()`
    """

def GetCharPressed() -> int:
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty

    Wraps: `int GetCharPressed()`
    """

def IsGamepadAvailable(gamepad: int) -> bool:
    """Check if a gamepad is available

    Wraps: `bool IsGamepadAvailable(int gamepad)`
    """

def GetGamepadName(gamepad: int) -> str:
    """Get gamepad internal name id

    Wraps: `const char * GetGamepadName(int gamepad)`
    """

def IsGamepadButtonPressed(gamepad: int, button: int) -> bool:
    """Check if a gamepad button has been pressed once

    Wraps: `bool IsGamepadButtonPressed(int gamepad, int button)`
    """

def IsGamepadButtonDown(gamepad: int, button: int) -> bool:
    """Check if a gamepad button is being pressed

    Wraps: `bool IsGamepadButtonDown(int gamepad, int button)`
    """

def IsGamepadButtonReleased(gamepad: int, button: int) -> bool:
    """Check if a gamepad button has been released once

    Wraps: `bool IsGamepadButtonReleased(int gamepad, int button)`
    """

def IsGamepadButtonUp(gamepad: int, button: int) -> bool:
    """Check if a gamepad button is NOT being pressed

    Wraps: `bool IsGamepadButtonUp(int gamepad, int button)`
    """

def GetGamepadButtonPressed() -> int:
    """Get the last gamepad button pressed

    Wraps: `int GetGamepadButtonPressed()`
    """

def GetGamepadAxisCount(gamepad: int) -> int:
    """Get gamepad axis count for a gamepad

    Wraps: `int GetGamepadAxisCount(int gamepad)`
    """

def GetGamepadAxisMovement(gamepad: int, axis: int) -> float:
    """Get axis movement value for a gamepad axis

    Wraps: `float GetGamepadAxisMovement(int gamepad, int axis)`
    """

def SetGamepadMappings(mappings: str) -> int:
    """Set internal gamepad mappings (SDL_GameControllerDB)

    Wraps: `int SetGamepadMappings(const char * mappings)`
    """

def IsMouseButtonPressed(button: int) -> bool:
    """Check if a mouse button has been pressed once

    Wraps: `bool IsMouseButtonPressed(int button)`
    """

def IsMouseButtonDown(button: int) -> bool:
    """Check if a mouse button is being pressed

    Wraps: `bool IsMouseButtonDown(int button)`
    """

def IsMouseButtonReleased(button: int) -> bool:
    """Check if a mouse button has been released once

    Wraps: `bool IsMouseButtonReleased(int button)`
    """

def IsMouseButtonUp(button: int) -> bool:
    """Check if a mouse button is NOT being pressed

    Wraps: `bool IsMouseButtonUp(int button)`
    """

def GetMouseX() -> int:
    """Get mouse position X

    Wraps: `int GetMouseX()`
    """

def GetMouseY() -> int:
    """Get mouse position Y

    Wraps: `int GetMouseY()`
    """

def GetMousePosition() -> vec2:
    """Get mouse position XY

    Wraps: `Vector2 GetMousePosition()`
    """

def GetMouseDelta() -> vec2:
    """Get mouse delta between frames

    Wraps: `Vector2 GetMouseDelta()`
    """

def SetMousePosition(x: int, y: int) -> None:
    """Set mouse position XY

    Wraps: `void SetMousePosition(int x, int y)`
    """

def SetMouseOffset(offsetX: int, offsetY: int) -> None:
    """Set mouse offset

    Wraps: `void SetMouseOffset(int offsetX, int offsetY)`
    """

def SetMouseScale(scaleX: float, scaleY: float) -> None:
    """Set mouse scaling

    Wraps: `void SetMouseScale(float scaleX, float scaleY)`
    """

def GetMouseWheelMove() -> float:
    """Get mouse wheel movement for X or Y, whichever is larger

    Wraps: `float GetMouseWheelMove()`
    """

def GetMouseWheelMoveV() -> vec2:
    """Get mouse wheel movement for both X and Y

    Wraps: `Vector2 GetMouseWheelMoveV()`
    """

def SetMouseCursor(cursor: int) -> None:
    """Set mouse cursor

    Wraps: `void SetMouseCursor(int cursor)`
    """

def GetTouchX() -> int:
    """Get touch position X for touch point 0 (relative to screen size)

    Wraps: `int GetTouchX()`
    """

def GetTouchY() -> int:
    """Get touch position Y for touch point 0 (relative to screen size)

    Wraps: `int GetTouchY()`
    """

def GetTouchPosition(index: int) -> vec2:
    """Get touch position XY for a touch point index (relative to screen size)

    Wraps: `Vector2 GetTouchPosition(int index)`
    """

def GetTouchPointId(index: int) -> int:
    """Get touch point identifier for given index

    Wraps: `int GetTouchPointId(int index)`
    """

def GetTouchPointCount() -> int:
    """Get number of touch points

    Wraps: `int GetTouchPointCount()`
    """

def SetGesturesEnabled(flags: int) -> None:
    """Enable a set of gestures using flags

    Wraps: `void SetGesturesEnabled(unsigned int flags)`
    """

def IsGestureDetected(gesture: int) -> bool:
    """Check if a gesture have been detected

    Wraps: `bool IsGestureDetected(int gesture)`
    """

def GetGestureDetected() -> int:
    """Get latest detected gesture

    Wraps: `int GetGestureDetected()`
    """

def GetGestureHoldDuration() -> float:
    """Get gesture hold time in milliseconds

    Wraps: `float GetGestureHoldDuration()`
    """

def GetGestureDragVector() -> vec2:
    """Get gesture drag vector

    Wraps: `Vector2 GetGestureDragVector()`
    """

def GetGestureDragAngle() -> float:
    """Get gesture drag angle

    Wraps: `float GetGestureDragAngle()`
    """

def GetGesturePinchVector() -> vec2:
    """Get gesture pinch delta

    Wraps: `Vector2 GetGesturePinchVector()`
    """

def GetGesturePinchAngle() -> float:
    """Get gesture pinch angle

    Wraps: `float GetGesturePinchAngle()`
    """

def UpdateCamera(camera: 'Camera_p', mode: int) -> None:
    """Update camera position for selected mode

    Wraps: `void UpdateCamera(Camera * camera, int mode)`
    """

def UpdateCameraPro(camera: 'Camera_p', movement: vec3, rotation: vec3, zoom: float) -> None:
    """Update camera movement/rotation

    Wraps: `void UpdateCameraPro(Camera * camera, Vector3 movement, Vector3 rotation, float zoom)`
    """

def SetShapesTexture(texture: Texture2D, source: Rectangle) -> None:
    """Set texture and rectangle to be used on shapes drawing

    Wraps: `void SetShapesTexture(Texture2D texture, Rectangle source)`
    """

def DrawPixel(posX: int, posY: int, color: Color) -> None:
    """Draw a pixel

    Wraps: `void DrawPixel(int posX, int posY, Color color)`
    """

def DrawPixelV(position: vec2, color: Color) -> None:
    """Draw a pixel (Vector version)

    Wraps: `void DrawPixelV(Vector2 position, Color color)`
    """

def DrawLine(startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
    """Draw a line

    Wraps: `void DrawLine(int startPosX, int startPosY, int endPosX, int endPosY, Color color)`
    """

def DrawLineV(startPos: vec2, endPos: vec2, color: Color) -> None:
    """Draw a line (Vector version)

    Wraps: `void DrawLineV(Vector2 startPos, Vector2 endPos, Color color)`
    """

def DrawLineEx(startPos: vec2, endPos: vec2, thick: float, color: Color) -> None:
    """Draw a line defining thickness

    Wraps: `void DrawLineEx(Vector2 startPos, Vector2 endPos, float thick, Color color)`
    """

def DrawLineBezier(startPos: vec2, endPos: vec2, thick: float, color: Color) -> None:
    """Draw a line using cubic-bezier curves in-out

    Wraps: `void DrawLineBezier(Vector2 startPos, Vector2 endPos, float thick, Color color)`
    """

def DrawLineBezierQuad(startPos: vec2, endPos: vec2, controlPos: vec2, thick: float, color: Color) -> None:
    """Draw line using quadratic bezier curves with a control point

    Wraps: `void DrawLineBezierQuad(Vector2 startPos, Vector2 endPos, Vector2 controlPos, float thick, Color color)`
    """

def DrawLineBezierCubic(startPos: vec2, endPos: vec2, startControlPos: vec2, endControlPos: vec2, thick: float, color: Color) -> None:
    """Draw line using cubic bezier curves with 2 control points

    Wraps: `void DrawLineBezierCubic(Vector2 startPos, Vector2 endPos, Vector2 startControlPos, Vector2 endControlPos, float thick, Color color)`
    """

def DrawLineStrip(points: 'vec2_p', pointCount: int, color: Color) -> None:
    """Draw lines sequence

    Wraps: `void DrawLineStrip(Vector2 * points, int pointCount, Color color)`
    """

def DrawCircle(centerX: int, centerY: int, radius: float, color: Color) -> None:
    """Draw a color-filled circle

    Wraps: `void DrawCircle(int centerX, int centerY, float radius, Color color)`
    """

def DrawCircleSector(center: vec2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
    """Draw a piece of a circle

    Wraps: `void DrawCircleSector(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color)`
    """

def DrawCircleSectorLines(center: vec2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
    """Draw circle sector outline

    Wraps: `void DrawCircleSectorLines(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color)`
    """

def DrawCircleGradient(centerX: int, centerY: int, radius: float, color1: Color, color2: Color) -> None:
    """Draw a gradient-filled circle

    Wraps: `void DrawCircleGradient(int centerX, int centerY, float radius, Color color1, Color color2)`
    """

def DrawCircleV(center: vec2, radius: float, color: Color) -> None:
    """Draw a color-filled circle (Vector version)

    Wraps: `void DrawCircleV(Vector2 center, float radius, Color color)`
    """

def DrawCircleLines(centerX: int, centerY: int, radius: float, color: Color) -> None:
    """Draw circle outline

    Wraps: `void DrawCircleLines(int centerX, int centerY, float radius, Color color)`
    """

def DrawEllipse(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
    """Draw ellipse

    Wraps: `void DrawEllipse(int centerX, int centerY, float radiusH, float radiusV, Color color)`
    """

def DrawEllipseLines(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None:
    """Draw ellipse outline

    Wraps: `void DrawEllipseLines(int centerX, int centerY, float radiusH, float radiusV, Color color)`
    """

def DrawRing(center: vec2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
    """Draw ring

    Wraps: `void DrawRing(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color)`
    """

def DrawRingLines(center: vec2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None:
    """Draw ring outline

    Wraps: `void DrawRingLines(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color)`
    """

def DrawRectangle(posX: int, posY: int, width: int, height: int, color: Color) -> None:
    """Draw a color-filled rectangle

    Wraps: `void DrawRectangle(int posX, int posY, int width, int height, Color color)`
    """

def DrawRectangleV(position: vec2, size: vec2, color: Color) -> None:
    """Draw a color-filled rectangle (Vector version)

    Wraps: `void DrawRectangleV(Vector2 position, Vector2 size, Color color)`
    """

def DrawRectangleRec(rec: Rectangle, color: Color) -> None:
    """Draw a color-filled rectangle

    Wraps: `void DrawRectangleRec(Rectangle rec, Color color)`
    """

def DrawRectanglePro(rec: Rectangle, origin: vec2, rotation: float, color: Color) -> None:
    """Draw a color-filled rectangle with pro parameters

    Wraps: `void DrawRectanglePro(Rectangle rec, Vector2 origin, float rotation, Color color)`
    """

def DrawRectangleGradientV(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
    """Draw a vertical-gradient-filled rectangle

    Wraps: `void DrawRectangleGradientV(int posX, int posY, int width, int height, Color color1, Color color2)`
    """

def DrawRectangleGradientH(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
    """Draw a horizontal-gradient-filled rectangle

    Wraps: `void DrawRectangleGradientH(int posX, int posY, int width, int height, Color color1, Color color2)`
    """

def DrawRectangleGradientEx(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
    """Draw a gradient-filled rectangle with custom vertex colors

    Wraps: `void DrawRectangleGradientEx(Rectangle rec, Color col1, Color col2, Color col3, Color col4)`
    """

def DrawRectangleLines(posX: int, posY: int, width: int, height: int, color: Color) -> None:
    """Draw rectangle outline

    Wraps: `void DrawRectangleLines(int posX, int posY, int width, int height, Color color)`
    """

def DrawRectangleLinesEx(rec: Rectangle, lineThick: float, color: Color) -> None:
    """Draw rectangle outline with extended parameters

    Wraps: `void DrawRectangleLinesEx(Rectangle rec, float lineThick, Color color)`
    """

def DrawRectangleRounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None:
    """Draw rectangle with rounded edges

    Wraps: `void DrawRectangleRounded(Rectangle rec, float roundness, int segments, Color color)`
    """

def DrawRectangleRoundedLines(rec: Rectangle, roundness: float, segments: int, lineThick: float, color: Color) -> None:
    """Draw rectangle with rounded edges outline

    Wraps: `void DrawRectangleRoundedLines(Rectangle rec, float roundness, int segments, float lineThick, Color color)`
    """

def DrawTriangle(v1: vec2, v2: vec2, v3: vec2, color: Color) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)

    Wraps: `void DrawTriangle(Vector2 v1, Vector2 v2, Vector2 v3, Color color)`
    """

def DrawTriangleLines(v1: vec2, v2: vec2, v3: vec2, color: Color) -> None:
    """Draw triangle outline (vertex in counter-clockwise order!)

    Wraps: `void DrawTriangleLines(Vector2 v1, Vector2 v2, Vector2 v3, Color color)`
    """

def DrawTriangleFan(points: 'vec2_p', pointCount: int, color: Color) -> None:
    """Draw a triangle fan defined by points (first vertex is the center)

    Wraps: `void DrawTriangleFan(Vector2 * points, int pointCount, Color color)`
    """

def DrawTriangleStrip(points: 'vec2_p', pointCount: int, color: Color) -> None:
    """Draw a triangle strip defined by points

    Wraps: `void DrawTriangleStrip(Vector2 * points, int pointCount, Color color)`
    """

def DrawPoly(center: vec2, sides: int, radius: float, rotation: float, color: Color) -> None:
    """Draw a regular polygon (Vector version)

    Wraps: `void DrawPoly(Vector2 center, int sides, float radius, float rotation, Color color)`
    """

def DrawPolyLines(center: vec2, sides: int, radius: float, rotation: float, color: Color) -> None:
    """Draw a polygon outline of n sides

    Wraps: `void DrawPolyLines(Vector2 center, int sides, float radius, float rotation, Color color)`
    """

def DrawPolyLinesEx(center: vec2, sides: int, radius: float, rotation: float, lineThick: float, color: Color) -> None:
    """Draw a polygon outline of n sides with extended parameters

    Wraps: `void DrawPolyLinesEx(Vector2 center, int sides, float radius, float rotation, float lineThick, Color color)`
    """

def CheckCollisionRecs(rec1: Rectangle, rec2: Rectangle) -> bool:
    """Check collision between two rectangles

    Wraps: `bool CheckCollisionRecs(Rectangle rec1, Rectangle rec2)`
    """

def CheckCollisionCircles(center1: vec2, radius1: float, center2: vec2, radius2: float) -> bool:
    """Check collision between two circles

    Wraps: `bool CheckCollisionCircles(Vector2 center1, float radius1, Vector2 center2, float radius2)`
    """

def CheckCollisionCircleRec(center: vec2, radius: float, rec: Rectangle) -> bool:
    """Check collision between circle and rectangle

    Wraps: `bool CheckCollisionCircleRec(Vector2 center, float radius, Rectangle rec)`
    """

def CheckCollisionPointRec(point: vec2, rec: Rectangle) -> bool:
    """Check if point is inside rectangle

    Wraps: `bool CheckCollisionPointRec(Vector2 point, Rectangle rec)`
    """

def CheckCollisionPointCircle(point: vec2, center: vec2, radius: float) -> bool:
    """Check if point is inside circle

    Wraps: `bool CheckCollisionPointCircle(Vector2 point, Vector2 center, float radius)`
    """

def CheckCollisionPointTriangle(point: vec2, p1: vec2, p2: vec2, p3: vec2) -> bool:
    """Check if point is inside a triangle

    Wraps: `bool CheckCollisionPointTriangle(Vector2 point, Vector2 p1, Vector2 p2, Vector2 p3)`
    """

def CheckCollisionPointPoly(point: vec2, points: 'vec2_p', pointCount: int) -> bool:
    """Check if point is within a polygon described by array of vertices

    Wraps: `bool CheckCollisionPointPoly(Vector2 point, Vector2 * points, int pointCount)`
    """

def CheckCollisionLines(startPos1: vec2, endPos1: vec2, startPos2: vec2, endPos2: vec2, collisionPoint: 'vec2_p') -> bool:
    """Check the collision between two lines defined by two points each, returns collision point by reference

    Wraps: `bool CheckCollisionLines(Vector2 startPos1, Vector2 endPos1, Vector2 startPos2, Vector2 endPos2, Vector2 * collisionPoint)`
    """

def CheckCollisionPointLine(point: vec2, p1: vec2, p2: vec2, threshold: int) -> bool:
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]

    Wraps: `bool CheckCollisionPointLine(Vector2 point, Vector2 p1, Vector2 p2, int threshold)`
    """

def GetCollisionRec(rec1: Rectangle, rec2: Rectangle) -> Rectangle:
    """Get collision rectangle for two rectangles collision

    Wraps: `Rectangle GetCollisionRec(Rectangle rec1, Rectangle rec2)`
    """

def LoadImage(fileName: str) -> Image:
    """Load image from file into CPU memory (RAM)

    Wraps: `Image LoadImage(const char * fileName)`
    """

def LoadImageRaw(fileName: str, width: int, height: int, format: int, headerSize: int) -> Image:
    """Load image from RAW file data

    Wraps: `Image LoadImageRaw(const char * fileName, int width, int height, int format, int headerSize)`
    """

def LoadImageAnim(fileName: str, frames: int_p) -> Image:
    """Load image sequence from file (frames appended to image.data)

    Wraps: `Image LoadImageAnim(const char * fileName, int * frames)`
    """

def LoadImageFromMemory(fileType: str, fileData: uchar_p, dataSize: int) -> Image:
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'

    Wraps: `Image LoadImageFromMemory(const char * fileType, const unsigned char * fileData, int dataSize)`
    """

def LoadImageFromTexture(texture: Texture2D) -> Image:
    """Load image from GPU texture data

    Wraps: `Image LoadImageFromTexture(Texture2D texture)`
    """

def LoadImageFromScreen() -> Image:
    """Load image from screen buffer and (screenshot)

    Wraps: `Image LoadImageFromScreen()`
    """

def IsImageReady(image: Image) -> bool:
    """Check if an image is ready

    Wraps: `bool IsImageReady(Image image)`
    """

def UnloadImage(image: Image) -> None:
    """Unload image from CPU memory (RAM)

    Wraps: `void UnloadImage(Image image)`
    """

def ExportImage(image: Image, fileName: str) -> bool:
    """Export image data to file, returns true on success

    Wraps: `bool ExportImage(Image image, const char * fileName)`
    """

def ExportImageAsCode(image: Image, fileName: str) -> bool:
    """Export image as code file defining an array of bytes, returns true on success

    Wraps: `bool ExportImageAsCode(Image image, const char * fileName)`
    """

def GenImageColor(width: int, height: int, color: Color) -> Image:
    """Generate image: plain color

    Wraps: `Image GenImageColor(int width, int height, Color color)`
    """

def GenImageGradientLinear(width: int, height: int, direction: int, start: Color, end: Color) -> Image:
    """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient

    Wraps: `Image GenImageGradientLinear(int width, int height, int direction, Color start, Color end)`
    """

def GenImageGradientRadial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
    """Generate image: radial gradient

    Wraps: `Image GenImageGradientRadial(int width, int height, float density, Color inner, Color outer)`
    """

def GenImageGradientSquare(width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
    """Generate image: square gradient

    Wraps: `Image GenImageGradientSquare(int width, int height, float density, Color inner, Color outer)`
    """

def GenImageChecked(width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image:
    """Generate image: checked

    Wraps: `Image GenImageChecked(int width, int height, int checksX, int checksY, Color col1, Color col2)`
    """

def GenImageWhiteNoise(width: int, height: int, factor: float) -> Image:
    """Generate image: white noise

    Wraps: `Image GenImageWhiteNoise(int width, int height, float factor)`
    """

def GenImagePerlinNoise(width: int, height: int, offsetX: int, offsetY: int, scale: float) -> Image:
    """Generate image: perlin noise

    Wraps: `Image GenImagePerlinNoise(int width, int height, int offsetX, int offsetY, float scale)`
    """

def GenImageCellular(width: int, height: int, tileSize: int) -> Image:
    """Generate image: cellular algorithm, bigger tileSize means bigger cells

    Wraps: `Image GenImageCellular(int width, int height, int tileSize)`
    """

def GenImageText(width: int, height: int, text: str) -> Image:
    """Generate image: grayscale image from text data

    Wraps: `Image GenImageText(int width, int height, const char * text)`
    """

def ImageCopy(image: Image) -> Image:
    """Create an image duplicate (useful for transformations)

    Wraps: `Image ImageCopy(Image image)`
    """

def ImageFromImage(image: Image, rec: Rectangle) -> Image:
    """Create an image from another image piece

    Wraps: `Image ImageFromImage(Image image, Rectangle rec)`
    """

def ImageText(text: str, fontSize: int, color: Color) -> Image:
    """Create an image from text (default font)

    Wraps: `Image ImageText(const char * text, int fontSize, Color color)`
    """

def ImageTextEx(font: Font, text: str, fontSize: float, spacing: float, tint: Color) -> Image:
    """Create an image from text (custom sprite font)

    Wraps: `Image ImageTextEx(Font font, const char * text, float fontSize, float spacing, Color tint)`
    """

def ImageFormat(image: 'Image_p', newFormat: int) -> None:
    """Convert image data to desired format

    Wraps: `void ImageFormat(Image * image, int newFormat)`
    """

def ImageToPOT(image: 'Image_p', fill: Color) -> None:
    """Convert image to POT (power-of-two)

    Wraps: `void ImageToPOT(Image * image, Color fill)`
    """

def ImageCrop(image: 'Image_p', crop: Rectangle) -> None:
    """Crop an image to a defined rectangle

    Wraps: `void ImageCrop(Image * image, Rectangle crop)`
    """

def ImageAlphaCrop(image: 'Image_p', threshold: float) -> None:
    """Crop image depending on alpha value

    Wraps: `void ImageAlphaCrop(Image * image, float threshold)`
    """

def ImageAlphaClear(image: 'Image_p', color: Color, threshold: float) -> None:
    """Clear alpha channel to desired color

    Wraps: `void ImageAlphaClear(Image * image, Color color, float threshold)`
    """

def ImageAlphaMask(image: 'Image_p', alphaMask: Image) -> None:
    """Apply alpha mask to image

    Wraps: `void ImageAlphaMask(Image * image, Image alphaMask)`
    """

def ImageAlphaPremultiply(image: 'Image_p') -> None:
    """Premultiply alpha channel

    Wraps: `void ImageAlphaPremultiply(Image * image)`
    """

def ImageBlurGaussian(image: 'Image_p', blurSize: int) -> None:
    """Apply Gaussian blur using a box blur approximation

    Wraps: `void ImageBlurGaussian(Image * image, int blurSize)`
    """

def ImageResize(image: 'Image_p', newWidth: int, newHeight: int) -> None:
    """Resize image (Bicubic scaling algorithm)

    Wraps: `void ImageResize(Image * image, int newWidth, int newHeight)`
    """

def ImageResizeNN(image: 'Image_p', newWidth: int, newHeight: int) -> None:
    """Resize image (Nearest-Neighbor scaling algorithm)

    Wraps: `void ImageResizeNN(Image * image, int newWidth, int newHeight)`
    """

def ImageResizeCanvas(image: 'Image_p', newWidth: int, newHeight: int, offsetX: int, offsetY: int, fill: Color) -> None:
    """Resize canvas and fill with color

    Wraps: `void ImageResizeCanvas(Image * image, int newWidth, int newHeight, int offsetX, int offsetY, Color fill)`
    """

def ImageMipmaps(image: 'Image_p') -> None:
    """Compute all mipmap levels for a provided image

    Wraps: `void ImageMipmaps(Image * image)`
    """

def ImageDither(image: 'Image_p', rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None:
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)

    Wraps: `void ImageDither(Image * image, int rBpp, int gBpp, int bBpp, int aBpp)`
    """

def ImageFlipVertical(image: 'Image_p') -> None:
    """Flip image vertically

    Wraps: `void ImageFlipVertical(Image * image)`
    """

def ImageFlipHorizontal(image: 'Image_p') -> None:
    """Flip image horizontally

    Wraps: `void ImageFlipHorizontal(Image * image)`
    """

def ImageRotate(image: 'Image_p', degrees: int) -> None:
    """Rotate image by input angle in degrees (-359 to 359) 

    Wraps: `void ImageRotate(Image * image, int degrees)`
    """

def ImageRotateCW(image: 'Image_p') -> None:
    """Rotate image clockwise 90deg

    Wraps: `void ImageRotateCW(Image * image)`
    """

def ImageRotateCCW(image: 'Image_p') -> None:
    """Rotate image counter-clockwise 90deg

    Wraps: `void ImageRotateCCW(Image * image)`
    """

def ImageColorTint(image: 'Image_p', color: Color) -> None:
    """Modify image color: tint

    Wraps: `void ImageColorTint(Image * image, Color color)`
    """

def ImageColorInvert(image: 'Image_p') -> None:
    """Modify image color: invert

    Wraps: `void ImageColorInvert(Image * image)`
    """

def ImageColorGrayscale(image: 'Image_p') -> None:
    """Modify image color: grayscale

    Wraps: `void ImageColorGrayscale(Image * image)`
    """

def ImageColorContrast(image: 'Image_p', contrast: float) -> None:
    """Modify image color: contrast (-100 to 100)

    Wraps: `void ImageColorContrast(Image * image, float contrast)`
    """

def ImageColorBrightness(image: 'Image_p', brightness: int) -> None:
    """Modify image color: brightness (-255 to 255)

    Wraps: `void ImageColorBrightness(Image * image, int brightness)`
    """

def ImageColorReplace(image: 'Image_p', color: Color, replace: Color) -> None:
    """Modify image color: replace color

    Wraps: `void ImageColorReplace(Image * image, Color color, Color replace)`
    """

def LoadImageColors(image: Image) -> 'Color_p':
    """Load color data from image as a Color array (RGBA - 32bit)

    Wraps: `Color * LoadImageColors(Image image)`
    """

def LoadImagePalette(image: Image, maxPaletteSize: int, colorCount: int_p) -> 'Color_p':
    """Load colors palette from image as a Color array (RGBA - 32bit)

    Wraps: `Color * LoadImagePalette(Image image, int maxPaletteSize, int * colorCount)`
    """

def UnloadImageColors(colors: 'Color_p') -> None:
    """Unload color data loaded with LoadImageColors()

    Wraps: `void UnloadImageColors(Color * colors)`
    """

def UnloadImagePalette(colors: 'Color_p') -> None:
    """Unload colors palette loaded with LoadImagePalette()

    Wraps: `void UnloadImagePalette(Color * colors)`
    """

def GetImageAlphaBorder(image: Image, threshold: float) -> Rectangle:
    """Get image alpha border rectangle

    Wraps: `Rectangle GetImageAlphaBorder(Image image, float threshold)`
    """

def GetImageColor(image: Image, x: int, y: int) -> Color:
    """Get image pixel color at (x, y) position

    Wraps: `Color GetImageColor(Image image, int x, int y)`
    """

def ImageClearBackground(dst: 'Image_p', color: Color) -> None:
    """Clear image background with given color

    Wraps: `void ImageClearBackground(Image * dst, Color color)`
    """

def ImageDrawPixel(dst: 'Image_p', posX: int, posY: int, color: Color) -> None:
    """Draw pixel within an image

    Wraps: `void ImageDrawPixel(Image * dst, int posX, int posY, Color color)`
    """

def ImageDrawPixelV(dst: 'Image_p', position: vec2, color: Color) -> None:
    """Draw pixel within an image (Vector version)

    Wraps: `void ImageDrawPixelV(Image * dst, Vector2 position, Color color)`
    """

def ImageDrawLine(dst: 'Image_p', startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None:
    """Draw line within an image

    Wraps: `void ImageDrawLine(Image * dst, int startPosX, int startPosY, int endPosX, int endPosY, Color color)`
    """

def ImageDrawLineV(dst: 'Image_p', start: vec2, end: vec2, color: Color) -> None:
    """Draw line within an image (Vector version)

    Wraps: `void ImageDrawLineV(Image * dst, Vector2 start, Vector2 end, Color color)`
    """

def ImageDrawCircle(dst: 'Image_p', centerX: int, centerY: int, radius: int, color: Color) -> None:
    """Draw a filled circle within an image

    Wraps: `void ImageDrawCircle(Image * dst, int centerX, int centerY, int radius, Color color)`
    """

def ImageDrawCircleV(dst: 'Image_p', center: vec2, radius: int, color: Color) -> None:
    """Draw a filled circle within an image (Vector version)

    Wraps: `void ImageDrawCircleV(Image * dst, Vector2 center, int radius, Color color)`
    """

def ImageDrawCircleLines(dst: 'Image_p', centerX: int, centerY: int, radius: int, color: Color) -> None:
    """Draw circle outline within an image

    Wraps: `void ImageDrawCircleLines(Image * dst, int centerX, int centerY, int radius, Color color)`
    """

def ImageDrawCircleLinesV(dst: 'Image_p', center: vec2, radius: int, color: Color) -> None:
    """Draw circle outline within an image (Vector version)

    Wraps: `void ImageDrawCircleLinesV(Image * dst, Vector2 center, int radius, Color color)`
    """

def ImageDrawRectangle(dst: 'Image_p', posX: int, posY: int, width: int, height: int, color: Color) -> None:
    """Draw rectangle within an image

    Wraps: `void ImageDrawRectangle(Image * dst, int posX, int posY, int width, int height, Color color)`
    """

def ImageDrawRectangleV(dst: 'Image_p', position: vec2, size: vec2, color: Color) -> None:
    """Draw rectangle within an image (Vector version)

    Wraps: `void ImageDrawRectangleV(Image * dst, Vector2 position, Vector2 size, Color color)`
    """

def ImageDrawRectangleRec(dst: 'Image_p', rec: Rectangle, color: Color) -> None:
    """Draw rectangle within an image

    Wraps: `void ImageDrawRectangleRec(Image * dst, Rectangle rec, Color color)`
    """

def ImageDrawRectangleLines(dst: 'Image_p', rec: Rectangle, thick: int, color: Color) -> None:
    """Draw rectangle lines within an image

    Wraps: `void ImageDrawRectangleLines(Image * dst, Rectangle rec, int thick, Color color)`
    """

def ImageDraw(dst: 'Image_p', src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None:
    """Draw a source image within a destination image (tint applied to source)

    Wraps: `void ImageDraw(Image * dst, Image src, Rectangle srcRec, Rectangle dstRec, Color tint)`
    """

def ImageDrawText(dst: 'Image_p', text: str, posX: int, posY: int, fontSize: int, color: Color) -> None:
    """Draw text (using default font) within an image (destination)

    Wraps: `void ImageDrawText(Image * dst, const char * text, int posX, int posY, int fontSize, Color color)`
    """

def ImageDrawTextEx(dst: 'Image_p', font: Font, text: str, position: vec2, fontSize: float, spacing: float, tint: Color) -> None:
    """Draw text (custom sprite font) within an image (destination)

    Wraps: `void ImageDrawTextEx(Image * dst, Font font, const char * text, Vector2 position, float fontSize, float spacing, Color tint)`
    """

def LoadTexture(fileName: str) -> Texture2D:
    """Load texture from file into GPU memory (VRAM)

    Wraps: `Texture2D LoadTexture(const char * fileName)`
    """

def LoadTextureFromImage(image: Image) -> Texture2D:
    """Load texture from image data

    Wraps: `Texture2D LoadTextureFromImage(Image image)`
    """

def LoadTextureCubemap(image: Image, layout: int) -> TextureCubemap:
    """Load cubemap from image, multiple image cubemap layouts supported

    Wraps: `TextureCubemap LoadTextureCubemap(Image image, int layout)`
    """

def LoadRenderTexture(width: int, height: int) -> RenderTexture2D:
    """Load texture for rendering (framebuffer)

    Wraps: `RenderTexture2D LoadRenderTexture(int width, int height)`
    """

def IsTextureReady(texture: Texture2D) -> bool:
    """Check if a texture is ready

    Wraps: `bool IsTextureReady(Texture2D texture)`
    """

def UnloadTexture(texture: Texture2D) -> None:
    """Unload texture from GPU memory (VRAM)

    Wraps: `void UnloadTexture(Texture2D texture)`
    """

def IsRenderTextureReady(target: RenderTexture2D) -> bool:
    """Check if a render texture is ready

    Wraps: `bool IsRenderTextureReady(RenderTexture2D target)`
    """

def UnloadRenderTexture(target: RenderTexture2D) -> None:
    """Unload render texture from GPU memory (VRAM)

    Wraps: `void UnloadRenderTexture(RenderTexture2D target)`
    """

def UpdateTexture(texture: Texture2D, pixels: void_p) -> None:
    """Update GPU texture with new data

    Wraps: `void UpdateTexture(Texture2D texture, const void * pixels)`
    """

def UpdateTextureRec(texture: Texture2D, rec: Rectangle, pixels: void_p) -> None:
    """Update GPU texture rectangle with new data

    Wraps: `void UpdateTextureRec(Texture2D texture, Rectangle rec, const void * pixels)`
    """

def GenTextureMipmaps(texture: 'Texture2D_p') -> None:
    """Generate GPU mipmaps for a texture

    Wraps: `void GenTextureMipmaps(Texture2D * texture)`
    """

def SetTextureFilter(texture: Texture2D, filter: int) -> None:
    """Set texture scaling filter mode

    Wraps: `void SetTextureFilter(Texture2D texture, int filter)`
    """

def SetTextureWrap(texture: Texture2D, wrap: int) -> None:
    """Set texture wrapping mode

    Wraps: `void SetTextureWrap(Texture2D texture, int wrap)`
    """

def DrawTexture(texture: Texture2D, posX: int, posY: int, tint: Color) -> None:
    """Draw a Texture2D

    Wraps: `void DrawTexture(Texture2D texture, int posX, int posY, Color tint)`
    """

def DrawTextureV(texture: Texture2D, position: vec2, tint: Color) -> None:
    """Draw a Texture2D with position defined as Vector2

    Wraps: `void DrawTextureV(Texture2D texture, Vector2 position, Color tint)`
    """

def DrawTextureEx(texture: Texture2D, position: vec2, rotation: float, scale: float, tint: Color) -> None:
    """Draw a Texture2D with extended parameters

    Wraps: `void DrawTextureEx(Texture2D texture, Vector2 position, float rotation, float scale, Color tint)`
    """

def DrawTextureRec(texture: Texture2D, source: Rectangle, position: vec2, tint: Color) -> None:
    """Draw a part of a texture defined by a rectangle

    Wraps: `void DrawTextureRec(Texture2D texture, Rectangle source, Vector2 position, Color tint)`
    """

def DrawTexturePro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: vec2, rotation: float, tint: Color) -> None:
    """Draw a part of a texture defined by a rectangle with 'pro' parameters

    Wraps: `void DrawTexturePro(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, Color tint)`
    """

def DrawTextureNPatch(texture: Texture2D, nPatchInfo: NPatchInfo, dest: Rectangle, origin: vec2, rotation: float, tint: Color) -> None:
    """Draws a texture (or part of it) that stretches or shrinks nicely

    Wraps: `void DrawTextureNPatch(Texture2D texture, NPatchInfo nPatchInfo, Rectangle dest, Vector2 origin, float rotation, Color tint)`
    """

def Fade(color: Color, alpha: float) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f

    Wraps: `Color Fade(Color color, float alpha)`
    """

def ColorToInt(color: Color) -> int:
    """Get hexadecimal value for a Color

    Wraps: `int ColorToInt(Color color)`
    """

def ColorNormalize(color: Color) -> vec4:
    """Get Color normalized as float [0..1]

    Wraps: `Vector4 ColorNormalize(Color color)`
    """

def ColorFromNormalized(normalized: vec4) -> Color:
    """Get Color from normalized values [0..1]

    Wraps: `Color ColorFromNormalized(Vector4 normalized)`
    """

def ColorToHSV(color: Color) -> vec3:
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]

    Wraps: `Vector3 ColorToHSV(Color color)`
    """

def ColorFromHSV(hue: float, saturation: float, value: float) -> Color:
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]

    Wraps: `Color ColorFromHSV(float hue, float saturation, float value)`
    """

def ColorTint(color: Color, tint: Color) -> Color:
    """Get color multiplied with another color

    Wraps: `Color ColorTint(Color color, Color tint)`
    """

def ColorBrightness(color: Color, factor: float) -> Color:
    """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f

    Wraps: `Color ColorBrightness(Color color, float factor)`
    """

def ColorContrast(color: Color, contrast: float) -> Color:
    """Get color with contrast correction, contrast values between -1.0f and 1.0f

    Wraps: `Color ColorContrast(Color color, float contrast)`
    """

def ColorAlpha(color: Color, alpha: float) -> Color:
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f

    Wraps: `Color ColorAlpha(Color color, float alpha)`
    """

def ColorAlphaBlend(dst: Color, src: Color, tint: Color) -> Color:
    """Get src alpha-blended into dst color with tint

    Wraps: `Color ColorAlphaBlend(Color dst, Color src, Color tint)`
    """

def GetColor(hexValue: int) -> Color:
    """Get Color structure from hexadecimal value

    Wraps: `Color GetColor(unsigned int hexValue)`
    """

def GetPixelColor(srcPtr: void_p, format: int) -> Color:
    """Get Color from a source pixel pointer of certain format

    Wraps: `Color GetPixelColor(void * srcPtr, int format)`
    """

def SetPixelColor(dstPtr: void_p, color: Color, format: int) -> None:
    """Set color formatted into destination pixel pointer

    Wraps: `void SetPixelColor(void * dstPtr, Color color, int format)`
    """

def GetPixelDataSize(width: int, height: int, format: int) -> int:
    """Get pixel data size in bytes for certain format

    Wraps: `int GetPixelDataSize(int width, int height, int format)`
    """

def GetFontDefault() -> Font:
    """Get the default Font

    Wraps: `Font GetFontDefault()`
    """

def LoadFont(fileName: str) -> Font:
    """Load font from file into GPU memory (VRAM)

    Wraps: `Font LoadFont(const char * fileName)`
    """

def LoadFontEx(fileName: str, fontSize: int, fontChars: int_p, glyphCount: int) -> Font:
    """Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set

    Wraps: `Font LoadFontEx(const char * fileName, int fontSize, int * fontChars, int glyphCount)`
    """

def LoadFontFromImage(image: Image, key: Color, firstChar: int) -> Font:
    """Load font from Image (XNA style)

    Wraps: `Font LoadFontFromImage(Image image, Color key, int firstChar)`
    """

def LoadFontFromMemory(fileType: str, fileData: uchar_p, dataSize: int, fontSize: int, fontChars: int_p, glyphCount: int) -> Font:
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'

    Wraps: `Font LoadFontFromMemory(const char * fileType, const unsigned char * fileData, int dataSize, int fontSize, int * fontChars, int glyphCount)`
    """

def IsFontReady(font: Font) -> bool:
    """Check if a font is ready

    Wraps: `bool IsFontReady(Font font)`
    """

def LoadFontData(fileData: uchar_p, dataSize: int, fontSize: int, fontChars: int_p, glyphCount: int, type: int) -> 'GlyphInfo_p':
    """Load font data for further use

    Wraps: `GlyphInfo * LoadFontData(const unsigned char * fileData, int dataSize, int fontSize, int * fontChars, int glyphCount, int type)`
    """

def GenImageFontAtlas(chars: 'GlyphInfo_p', recs: void_p, glyphCount: int, fontSize: int, padding: int, packMethod: int) -> Image:
    """Generate image font atlas using chars info

    Wraps: `Image GenImageFontAtlas(const GlyphInfo * chars, Rectangle ** recs, int glyphCount, int fontSize, int padding, int packMethod)`
    """

def UnloadFontData(chars: 'GlyphInfo_p', glyphCount: int) -> None:
    """Unload font chars info data (RAM)

    Wraps: `void UnloadFontData(GlyphInfo * chars, int glyphCount)`
    """

def UnloadFont(font: Font) -> None:
    """Unload font from GPU memory (VRAM)

    Wraps: `void UnloadFont(Font font)`
    """

def ExportFontAsCode(font: Font, fileName: str) -> bool:
    """Export font as code file, returns true on success

    Wraps: `bool ExportFontAsCode(Font font, const char * fileName)`
    """

def DrawFPS(posX: int, posY: int) -> None:
    """Draw current FPS

    Wraps: `void DrawFPS(int posX, int posY)`
    """

def DrawText(text: str, posX: int, posY: int, fontSize: int, color: Color) -> None:
    """Draw text (using default font)

    Wraps: `void DrawText(const char * text, int posX, int posY, int fontSize, Color color)`
    """

def DrawTextEx(font: Font, text: str, position: vec2, fontSize: float, spacing: float, tint: Color) -> None:
    """Draw text using font and additional parameters

    Wraps: `void DrawTextEx(Font font, const char * text, Vector2 position, float fontSize, float spacing, Color tint)`
    """

def DrawTextPro(font: Font, text: str, position: vec2, origin: vec2, rotation: float, fontSize: float, spacing: float, tint: Color) -> None:
    """Draw text using Font and pro parameters (rotation)

    Wraps: `void DrawTextPro(Font font, const char * text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint)`
    """

def DrawTextCodepoint(font: Font, codepoint: int, position: vec2, fontSize: float, tint: Color) -> None:
    """Draw one character (codepoint)

    Wraps: `void DrawTextCodepoint(Font font, int codepoint, Vector2 position, float fontSize, Color tint)`
    """

def DrawTextCodepoints(font: Font, codepoints: int_p, count: int, position: vec2, fontSize: float, spacing: float, tint: Color) -> None:
    """Draw multiple character (codepoint)

    Wraps: `void DrawTextCodepoints(Font font, const int * codepoints, int count, Vector2 position, float fontSize, float spacing, Color tint)`
    """

def MeasureText(text: str, fontSize: int) -> int:
    """Measure string width for default font

    Wraps: `int MeasureText(const char * text, int fontSize)`
    """

def MeasureTextEx(font: Font, text: str, fontSize: float, spacing: float) -> vec2:
    """Measure string size for Font

    Wraps: `Vector2 MeasureTextEx(Font font, const char * text, float fontSize, float spacing)`
    """

def GetGlyphIndex(font: Font, codepoint: int) -> int:
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found

    Wraps: `int GetGlyphIndex(Font font, int codepoint)`
    """

def GetGlyphInfo(font: Font, codepoint: int) -> GlyphInfo:
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found

    Wraps: `GlyphInfo GetGlyphInfo(Font font, int codepoint)`
    """

def GetGlyphAtlasRec(font: Font, codepoint: int) -> Rectangle:
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found

    Wraps: `Rectangle GetGlyphAtlasRec(Font font, int codepoint)`
    """

def LoadUTF8(codepoints: int_p, length: int) -> char_p:
    """Load UTF-8 text encoded from codepoints array

    Wraps: `char * LoadUTF8(const int * codepoints, int length)`
    """

def UnloadUTF8(text: char_p) -> None:
    """Unload UTF-8 text encoded from codepoints array

    Wraps: `void UnloadUTF8(char * text)`
    """

def LoadCodepoints(text: str, count: int_p) -> int_p:
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter

    Wraps: `int * LoadCodepoints(const char * text, int * count)`
    """

def UnloadCodepoints(codepoints: int_p) -> None:
    """Unload codepoints data from memory

    Wraps: `void UnloadCodepoints(int * codepoints)`
    """

def GetCodepointCount(text: str) -> int:
    """Get total number of codepoints in a UTF-8 encoded string

    Wraps: `int GetCodepointCount(const char * text)`
    """

def GetCodepoint(text: str, codepointSize: int_p) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

    Wraps: `int GetCodepoint(const char * text, int * codepointSize)`
    """

def GetCodepointNext(text: str, codepointSize: int_p) -> int:
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

    Wraps: `int GetCodepointNext(const char * text, int * codepointSize)`
    """

def GetCodepointPrevious(text: str, codepointSize: int_p) -> int:
    """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

    Wraps: `int GetCodepointPrevious(const char * text, int * codepointSize)`
    """

def CodepointToUTF8(codepoint: int, utf8Size: int_p) -> str:
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)

    Wraps: `const char * CodepointToUTF8(int codepoint, int * utf8Size)`
    """

def TextCopy(dst: char_p, src: str) -> int:
    """Copy one string to another, returns bytes copied

    Wraps: `int TextCopy(char * dst, const char * src)`
    """

def TextIsEqual(text1: str, text2: str) -> bool:
    """Check if two text string are equal

    Wraps: `bool TextIsEqual(const char * text1, const char * text2)`
    """

def TextLength(text: str) -> int:
    """Get text length, checks for '\0' ending

    Wraps: `unsigned int TextLength(const char * text)`
    """

def TextSubtext(text: str, position: int, length: int) -> str:
    """Get a piece of a text string

    Wraps: `const char * TextSubtext(const char * text, int position, int length)`
    """

def TextReplace(text: char_p, replace: str, by: str) -> char_p:
    """Replace text string (WARNING: memory must be freed!)

    Wraps: `char * TextReplace(char * text, const char * replace, const char * by)`
    """

def TextInsert(text: str, insert: str, position: int) -> char_p:
    """Insert text in a position (WARNING: memory must be freed!)

    Wraps: `char * TextInsert(const char * text, const char * insert, int position)`
    """

def TextJoin(textList: void_p, count: int, delimiter: str) -> str:
    """Join text strings with delimiter

    Wraps: `const char * TextJoin(const char ** textList, int count, const char * delimiter)`
    """

def TextSplit(text: str, delimiter: int, count: int_p) -> void_p:
    """Split text into multiple strings

    Wraps: `const char ** TextSplit(const char * text, char delimiter, int * count)`
    """

def TextAppend(text: char_p, append: str, position: int_p) -> None:
    """Append text at specific position and move cursor!

    Wraps: `void TextAppend(char * text, const char * append, int * position)`
    """

def TextFindIndex(text: str, find: str) -> int:
    """Find first text occurrence within a string

    Wraps: `int TextFindIndex(const char * text, const char * find)`
    """

def TextToUpper(text: str) -> str:
    """Get upper case version of provided string

    Wraps: `const char * TextToUpper(const char * text)`
    """

def TextToLower(text: str) -> str:
    """Get lower case version of provided string

    Wraps: `const char * TextToLower(const char * text)`
    """

def TextToPascal(text: str) -> str:
    """Get Pascal case notation version of provided string

    Wraps: `const char * TextToPascal(const char * text)`
    """

def TextToInteger(text: str) -> int:
    """Get integer value from text (negative values not supported)

    Wraps: `int TextToInteger(const char * text)`
    """

def DrawLine3D(startPos: vec3, endPos: vec3, color: Color) -> None:
    """Draw a line in 3D world space

    Wraps: `void DrawLine3D(Vector3 startPos, Vector3 endPos, Color color)`
    """

def DrawPoint3D(position: vec3, color: Color) -> None:
    """Draw a point in 3D space, actually a small line

    Wraps: `void DrawPoint3D(Vector3 position, Color color)`
    """

def DrawCircle3D(center: vec3, radius: float, rotationAxis: vec3, rotationAngle: float, color: Color) -> None:
    """Draw a circle in 3D world space

    Wraps: `void DrawCircle3D(Vector3 center, float radius, Vector3 rotationAxis, float rotationAngle, Color color)`
    """

def DrawTriangle3D(v1: vec3, v2: vec3, v3: vec3, color: Color) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)

    Wraps: `void DrawTriangle3D(Vector3 v1, Vector3 v2, Vector3 v3, Color color)`
    """

def DrawTriangleStrip3D(points: 'vec3_p', pointCount: int, color: Color) -> None:
    """Draw a triangle strip defined by points

    Wraps: `void DrawTriangleStrip3D(Vector3 * points, int pointCount, Color color)`
    """

def DrawCube(position: vec3, width: float, height: float, length: float, color: Color) -> None:
    """Draw cube

    Wraps: `void DrawCube(Vector3 position, float width, float height, float length, Color color)`
    """

def DrawCubeV(position: vec3, size: vec3, color: Color) -> None:
    """Draw cube (Vector version)

    Wraps: `void DrawCubeV(Vector3 position, Vector3 size, Color color)`
    """

def DrawCubeWires(position: vec3, width: float, height: float, length: float, color: Color) -> None:
    """Draw cube wires

    Wraps: `void DrawCubeWires(Vector3 position, float width, float height, float length, Color color)`
    """

def DrawCubeWiresV(position: vec3, size: vec3, color: Color) -> None:
    """Draw cube wires (Vector version)

    Wraps: `void DrawCubeWiresV(Vector3 position, Vector3 size, Color color)`
    """

def DrawSphere(centerPos: vec3, radius: float, color: Color) -> None:
    """Draw sphere

    Wraps: `void DrawSphere(Vector3 centerPos, float radius, Color color)`
    """

def DrawSphereEx(centerPos: vec3, radius: float, rings: int, slices: int, color: Color) -> None:
    """Draw sphere with extended parameters

    Wraps: `void DrawSphereEx(Vector3 centerPos, float radius, int rings, int slices, Color color)`
    """

def DrawSphereWires(centerPos: vec3, radius: float, rings: int, slices: int, color: Color) -> None:
    """Draw sphere wires

    Wraps: `void DrawSphereWires(Vector3 centerPos, float radius, int rings, int slices, Color color)`
    """

def DrawCylinder(position: vec3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
    """Draw a cylinder/cone

    Wraps: `void DrawCylinder(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color)`
    """

def DrawCylinderEx(startPos: vec3, endPos: vec3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
    """Draw a cylinder with base at startPos and top at endPos

    Wraps: `void DrawCylinderEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color)`
    """

def DrawCylinderWires(position: vec3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
    """Draw a cylinder/cone wires

    Wraps: `void DrawCylinderWires(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color)`
    """

def DrawCylinderWiresEx(startPos: vec3, endPos: vec3, startRadius: float, endRadius: float, sides: int, color: Color) -> None:
    """Draw a cylinder wires with base at startPos and top at endPos

    Wraps: `void DrawCylinderWiresEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color)`
    """

def DrawCapsule(startPos: vec3, endPos: vec3, radius: float, slices: int, rings: int, color: Color) -> None:
    """Draw a capsule with the center of its sphere caps at startPos and endPos

    Wraps: `void DrawCapsule(Vector3 startPos, Vector3 endPos, float radius, int slices, int rings, Color color)`
    """

def DrawCapsuleWires(startPos: vec3, endPos: vec3, radius: float, slices: int, rings: int, color: Color) -> None:
    """Draw capsule wireframe with the center of its sphere caps at startPos and endPos

    Wraps: `void DrawCapsuleWires(Vector3 startPos, Vector3 endPos, float radius, int slices, int rings, Color color)`
    """

def DrawPlane(centerPos: vec3, size: vec2, color: Color) -> None:
    """Draw a plane XZ

    Wraps: `void DrawPlane(Vector3 centerPos, Vector2 size, Color color)`
    """

def DrawRay(ray: Ray, color: Color) -> None:
    """Draw a ray line

    Wraps: `void DrawRay(Ray ray, Color color)`
    """

def DrawGrid(slices: int, spacing: float) -> None:
    """Draw a grid (centered at (0, 0, 0))

    Wraps: `void DrawGrid(int slices, float spacing)`
    """

def LoadModel(fileName: str) -> Model:
    """Load model from files (meshes and materials)

    Wraps: `Model LoadModel(const char * fileName)`
    """

def LoadModelFromMesh(mesh: Mesh) -> Model:
    """Load model from generated mesh (default material)

    Wraps: `Model LoadModelFromMesh(Mesh mesh)`
    """

def IsModelReady(model: Model) -> bool:
    """Check if a model is ready

    Wraps: `bool IsModelReady(Model model)`
    """

def UnloadModel(model: Model) -> None:
    """Unload model (including meshes) from memory (RAM and/or VRAM)

    Wraps: `void UnloadModel(Model model)`
    """

def GetModelBoundingBox(model: Model) -> BoundingBox:
    """Compute model bounding box limits (considers all meshes)

    Wraps: `BoundingBox GetModelBoundingBox(Model model)`
    """

def DrawModel(model: Model, position: vec3, scale: float, tint: Color) -> None:
    """Draw a model (with texture if set)

    Wraps: `void DrawModel(Model model, Vector3 position, float scale, Color tint)`
    """

def DrawModelEx(model: Model, position: vec3, rotationAxis: vec3, rotationAngle: float, scale: vec3, tint: Color) -> None:
    """Draw a model with extended parameters

    Wraps: `void DrawModelEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint)`
    """

def DrawModelWires(model: Model, position: vec3, scale: float, tint: Color) -> None:
    """Draw a model wires (with texture if set)

    Wraps: `void DrawModelWires(Model model, Vector3 position, float scale, Color tint)`
    """

def DrawModelWiresEx(model: Model, position: vec3, rotationAxis: vec3, rotationAngle: float, scale: vec3, tint: Color) -> None:
    """Draw a model wires (with texture if set) with extended parameters

    Wraps: `void DrawModelWiresEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint)`
    """

def DrawBoundingBox(box: BoundingBox, color: Color) -> None:
    """Draw bounding box (wires)

    Wraps: `void DrawBoundingBox(BoundingBox box, Color color)`
    """

def DrawBillboard(camera: Camera, texture: Texture2D, position: vec3, size: float, tint: Color) -> None:
    """Draw a billboard texture

    Wraps: `void DrawBillboard(Camera camera, Texture2D texture, Vector3 position, float size, Color tint)`
    """

def DrawBillboardRec(camera: Camera, texture: Texture2D, source: Rectangle, position: vec3, size: vec2, tint: Color) -> None:
    """Draw a billboard texture defined by source

    Wraps: `void DrawBillboardRec(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector2 size, Color tint)`
    """

def DrawBillboardPro(camera: Camera, texture: Texture2D, source: Rectangle, position: vec3, up: vec3, size: vec2, origin: vec2, rotation: float, tint: Color) -> None:
    """Draw a billboard texture defined by source and rotation

    Wraps: `void DrawBillboardPro(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector3 up, Vector2 size, Vector2 origin, float rotation, Color tint)`
    """

def UploadMesh(mesh: 'Mesh_p', dynamic: bool) -> None:
    """Upload mesh vertex data in GPU and provide VAO/VBO ids

    Wraps: `void UploadMesh(Mesh * mesh, bool dynamic)`
    """

def UpdateMeshBuffer(mesh: Mesh, index: int, data: void_p, dataSize: int, offset: int) -> None:
    """Update mesh vertex data in GPU for a specific buffer index

    Wraps: `void UpdateMeshBuffer(Mesh mesh, int index, const void * data, int dataSize, int offset)`
    """

def UnloadMesh(mesh: Mesh) -> None:
    """Unload mesh data from CPU and GPU

    Wraps: `void UnloadMesh(Mesh mesh)`
    """

def DrawMesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
    """Draw a 3d mesh with material and transform

    Wraps: `void DrawMesh(Mesh mesh, Material material, Matrix transform)`
    """

def DrawMeshInstanced(mesh: Mesh, material: Material, transforms: 'Matrix_p', instances: int) -> None:
    """Draw multiple mesh instances with material and different transforms

    Wraps: `void DrawMeshInstanced(Mesh mesh, Material material, const Matrix * transforms, int instances)`
    """

def ExportMesh(mesh: Mesh, fileName: str) -> bool:
    """Export mesh data to file, returns true on success

    Wraps: `bool ExportMesh(Mesh mesh, const char * fileName)`
    """

def GetMeshBoundingBox(mesh: Mesh) -> BoundingBox:
    """Compute mesh bounding box limits

    Wraps: `BoundingBox GetMeshBoundingBox(Mesh mesh)`
    """

def GenMeshTangents(mesh: 'Mesh_p') -> None:
    """Compute mesh tangents

    Wraps: `void GenMeshTangents(Mesh * mesh)`
    """

def GenMeshPoly(sides: int, radius: float) -> Mesh:
    """Generate polygonal mesh

    Wraps: `Mesh GenMeshPoly(int sides, float radius)`
    """

def GenMeshPlane(width: float, length: float, resX: int, resZ: int) -> Mesh:
    """Generate plane mesh (with subdivisions)

    Wraps: `Mesh GenMeshPlane(float width, float length, int resX, int resZ)`
    """

def GenMeshCube(width: float, height: float, length: float) -> Mesh:
    """Generate cuboid mesh

    Wraps: `Mesh GenMeshCube(float width, float height, float length)`
    """

def GenMeshSphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate sphere mesh (standard sphere)

    Wraps: `Mesh GenMeshSphere(float radius, int rings, int slices)`
    """

def GenMeshHemiSphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate half-sphere mesh (no bottom cap)

    Wraps: `Mesh GenMeshHemiSphere(float radius, int rings, int slices)`
    """

def GenMeshCylinder(radius: float, height: float, slices: int) -> Mesh:
    """Generate cylinder mesh

    Wraps: `Mesh GenMeshCylinder(float radius, float height, int slices)`
    """

def GenMeshCone(radius: float, height: float, slices: int) -> Mesh:
    """Generate cone/pyramid mesh

    Wraps: `Mesh GenMeshCone(float radius, float height, int slices)`
    """

def GenMeshTorus(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
    """Generate torus mesh

    Wraps: `Mesh GenMeshTorus(float radius, float size, int radSeg, int sides)`
    """

def GenMeshKnot(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
    """Generate trefoil knot mesh

    Wraps: `Mesh GenMeshKnot(float radius, float size, int radSeg, int sides)`
    """

def GenMeshHeightmap(heightmap: Image, size: vec3) -> Mesh:
    """Generate heightmap mesh from image data

    Wraps: `Mesh GenMeshHeightmap(Image heightmap, Vector3 size)`
    """

def GenMeshCubicmap(cubicmap: Image, cubeSize: vec3) -> Mesh:
    """Generate cubes-based map mesh from image data

    Wraps: `Mesh GenMeshCubicmap(Image cubicmap, Vector3 cubeSize)`
    """

def LoadMaterials(fileName: str, materialCount: int_p) -> 'Material_p':
    """Load materials from model file

    Wraps: `Material * LoadMaterials(const char * fileName, int * materialCount)`
    """

def LoadMaterialDefault() -> Material:
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)

    Wraps: `Material LoadMaterialDefault()`
    """

def IsMaterialReady(material: Material) -> bool:
    """Check if a material is ready

    Wraps: `bool IsMaterialReady(Material material)`
    """

def UnloadMaterial(material: Material) -> None:
    """Unload material from GPU memory (VRAM)

    Wraps: `void UnloadMaterial(Material material)`
    """

def SetMaterialTexture(material: 'Material_p', mapType: int, texture: Texture2D) -> None:
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)

    Wraps: `void SetMaterialTexture(Material * material, int mapType, Texture2D texture)`
    """

def SetModelMeshMaterial(model: 'Model_p', meshId: int, materialId: int) -> None:
    """Set material for a mesh

    Wraps: `void SetModelMeshMaterial(Model * model, int meshId, int materialId)`
    """

def LoadModelAnimations(fileName: str, animCount: uint_p) -> 'ModelAnimation_p':
    """Load model animations from file

    Wraps: `ModelAnimation * LoadModelAnimations(const char * fileName, unsigned int * animCount)`
    """

def UpdateModelAnimation(model: Model, anim: ModelAnimation, frame: int) -> None:
    """Update model animation pose

    Wraps: `void UpdateModelAnimation(Model model, ModelAnimation anim, int frame)`
    """

def UnloadModelAnimation(anim: ModelAnimation) -> None:
    """Unload animation data

    Wraps: `void UnloadModelAnimation(ModelAnimation anim)`
    """

def UnloadModelAnimations(animations: 'ModelAnimation_p', count: int) -> None:
    """Unload animation array data

    Wraps: `void UnloadModelAnimations(ModelAnimation * animations, unsigned int count)`
    """

def IsModelAnimationValid(model: Model, anim: ModelAnimation) -> bool:
    """Check model animation skeleton match

    Wraps: `bool IsModelAnimationValid(Model model, ModelAnimation anim)`
    """

def CheckCollisionSpheres(center1: vec3, radius1: float, center2: vec3, radius2: float) -> bool:
    """Check collision between two spheres

    Wraps: `bool CheckCollisionSpheres(Vector3 center1, float radius1, Vector3 center2, float radius2)`
    """

def CheckCollisionBoxes(box1: BoundingBox, box2: BoundingBox) -> bool:
    """Check collision between two bounding boxes

    Wraps: `bool CheckCollisionBoxes(BoundingBox box1, BoundingBox box2)`
    """

def CheckCollisionBoxSphere(box: BoundingBox, center: vec3, radius: float) -> bool:
    """Check collision between box and sphere

    Wraps: `bool CheckCollisionBoxSphere(BoundingBox box, Vector3 center, float radius)`
    """

def GetRayCollisionSphere(ray: Ray, center: vec3, radius: float) -> RayCollision:
    """Get collision info between ray and sphere

    Wraps: `RayCollision GetRayCollisionSphere(Ray ray, Vector3 center, float radius)`
    """

def GetRayCollisionBox(ray: Ray, box: BoundingBox) -> RayCollision:
    """Get collision info between ray and box

    Wraps: `RayCollision GetRayCollisionBox(Ray ray, BoundingBox box)`
    """

def GetRayCollisionMesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision:
    """Get collision info between ray and mesh

    Wraps: `RayCollision GetRayCollisionMesh(Ray ray, Mesh mesh, Matrix transform)`
    """

def GetRayCollisionTriangle(ray: Ray, p1: vec3, p2: vec3, p3: vec3) -> RayCollision:
    """Get collision info between ray and triangle

    Wraps: `RayCollision GetRayCollisionTriangle(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3)`
    """

def GetRayCollisionQuad(ray: Ray, p1: vec3, p2: vec3, p3: vec3, p4: vec3) -> RayCollision:
    """Get collision info between ray and quad

    Wraps: `RayCollision GetRayCollisionQuad(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3, Vector3 p4)`
    """

def InitAudioDevice() -> None:
    """Initialize audio device and context

    Wraps: `void InitAudioDevice()`
    """

def CloseAudioDevice() -> None:
    """Close the audio device and context

    Wraps: `void CloseAudioDevice()`
    """

def IsAudioDeviceReady() -> bool:
    """Check if audio device has been initialized successfully

    Wraps: `bool IsAudioDeviceReady()`
    """

def SetMasterVolume(volume: float) -> None:
    """Set master volume (listener)

    Wraps: `void SetMasterVolume(float volume)`
    """

def LoadWave(fileName: str) -> Wave:
    """Load wave data from file

    Wraps: `Wave LoadWave(const char * fileName)`
    """

def LoadWaveFromMemory(fileType: str, fileData: uchar_p, dataSize: int) -> Wave:
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'

    Wraps: `Wave LoadWaveFromMemory(const char * fileType, const unsigned char * fileData, int dataSize)`
    """

def IsWaveReady(wave: Wave) -> bool:
    """Checks if wave data is ready

    Wraps: `bool IsWaveReady(Wave wave)`
    """

def LoadSound(fileName: str) -> Sound:
    """Load sound from file

    Wraps: `Sound LoadSound(const char * fileName)`
    """

def LoadSoundFromWave(wave: Wave) -> Sound:
    """Load sound from wave data

    Wraps: `Sound LoadSoundFromWave(Wave wave)`
    """

def IsSoundReady(sound: Sound) -> bool:
    """Checks if a sound is ready

    Wraps: `bool IsSoundReady(Sound sound)`
    """

def UpdateSound(sound: Sound, data: void_p, sampleCount: int) -> None:
    """Update sound buffer with new data

    Wraps: `void UpdateSound(Sound sound, const void * data, int sampleCount)`
    """

def UnloadWave(wave: Wave) -> None:
    """Unload wave data

    Wraps: `void UnloadWave(Wave wave)`
    """

def UnloadSound(sound: Sound) -> None:
    """Unload sound

    Wraps: `void UnloadSound(Sound sound)`
    """

def ExportWave(wave: Wave, fileName: str) -> bool:
    """Export wave data to file, returns true on success

    Wraps: `bool ExportWave(Wave wave, const char * fileName)`
    """

def ExportWaveAsCode(wave: Wave, fileName: str) -> bool:
    """Export wave sample data to code (.h), returns true on success

    Wraps: `bool ExportWaveAsCode(Wave wave, const char * fileName)`
    """

def PlaySound(sound: Sound) -> None:
    """Play a sound

    Wraps: `void PlaySound(Sound sound)`
    """

def StopSound(sound: Sound) -> None:
    """Stop playing a sound

    Wraps: `void StopSound(Sound sound)`
    """

def PauseSound(sound: Sound) -> None:
    """Pause a sound

    Wraps: `void PauseSound(Sound sound)`
    """

def ResumeSound(sound: Sound) -> None:
    """Resume a paused sound

    Wraps: `void ResumeSound(Sound sound)`
    """

def IsSoundPlaying(sound: Sound) -> bool:
    """Check if a sound is currently playing

    Wraps: `bool IsSoundPlaying(Sound sound)`
    """

def SetSoundVolume(sound: Sound, volume: float) -> None:
    """Set volume for a sound (1.0 is max level)

    Wraps: `void SetSoundVolume(Sound sound, float volume)`
    """

def SetSoundPitch(sound: Sound, pitch: float) -> None:
    """Set pitch for a sound (1.0 is base level)

    Wraps: `void SetSoundPitch(Sound sound, float pitch)`
    """

def SetSoundPan(sound: Sound, pan: float) -> None:
    """Set pan for a sound (0.5 is center)

    Wraps: `void SetSoundPan(Sound sound, float pan)`
    """

def WaveCopy(wave: Wave) -> Wave:
    """Copy a wave to a new wave

    Wraps: `Wave WaveCopy(Wave wave)`
    """

def WaveCrop(wave: 'Wave_p', initSample: int, finalSample: int) -> None:
    """Crop a wave to defined samples range

    Wraps: `void WaveCrop(Wave * wave, int initSample, int finalSample)`
    """

def WaveFormat(wave: 'Wave_p', sampleRate: int, sampleSize: int, channels: int) -> None:
    """Convert wave data to desired format

    Wraps: `void WaveFormat(Wave * wave, int sampleRate, int sampleSize, int channels)`
    """

def LoadWaveSamples(wave: Wave) -> float_p:
    """Load samples data from wave as a 32bit float data array

    Wraps: `float * LoadWaveSamples(Wave wave)`
    """

def UnloadWaveSamples(samples: float_p) -> None:
    """Unload samples data loaded with LoadWaveSamples()

    Wraps: `void UnloadWaveSamples(float * samples)`
    """

def LoadMusicStream(fileName: str) -> Music:
    """Load music stream from file

    Wraps: `Music LoadMusicStream(const char * fileName)`
    """

def LoadMusicStreamFromMemory(fileType: str, data: uchar_p, dataSize: int) -> Music:
    """Load music stream from data

    Wraps: `Music LoadMusicStreamFromMemory(const char * fileType, const unsigned char * data, int dataSize)`
    """

def IsMusicReady(music: Music) -> bool:
    """Checks if a music stream is ready

    Wraps: `bool IsMusicReady(Music music)`
    """

def UnloadMusicStream(music: Music) -> None:
    """Unload music stream

    Wraps: `void UnloadMusicStream(Music music)`
    """

def PlayMusicStream(music: Music) -> None:
    """Start music playing

    Wraps: `void PlayMusicStream(Music music)`
    """

def IsMusicStreamPlaying(music: Music) -> bool:
    """Check if music is playing

    Wraps: `bool IsMusicStreamPlaying(Music music)`
    """

def UpdateMusicStream(music: Music) -> None:
    """Updates buffers for music streaming

    Wraps: `void UpdateMusicStream(Music music)`
    """

def StopMusicStream(music: Music) -> None:
    """Stop music playing

    Wraps: `void StopMusicStream(Music music)`
    """

def PauseMusicStream(music: Music) -> None:
    """Pause music playing

    Wraps: `void PauseMusicStream(Music music)`
    """

def ResumeMusicStream(music: Music) -> None:
    """Resume playing paused music

    Wraps: `void ResumeMusicStream(Music music)`
    """

def SeekMusicStream(music: Music, position: float) -> None:
    """Seek music to a position (in seconds)

    Wraps: `void SeekMusicStream(Music music, float position)`
    """

def SetMusicVolume(music: Music, volume: float) -> None:
    """Set volume for music (1.0 is max level)

    Wraps: `void SetMusicVolume(Music music, float volume)`
    """

def SetMusicPitch(music: Music, pitch: float) -> None:
    """Set pitch for a music (1.0 is base level)

    Wraps: `void SetMusicPitch(Music music, float pitch)`
    """

def SetMusicPan(music: Music, pan: float) -> None:
    """Set pan for a music (0.5 is center)

    Wraps: `void SetMusicPan(Music music, float pan)`
    """

def GetMusicTimeLength(music: Music) -> float:
    """Get music time length (in seconds)

    Wraps: `float GetMusicTimeLength(Music music)`
    """

def GetMusicTimePlayed(music: Music) -> float:
    """Get current music time played (in seconds)

    Wraps: `float GetMusicTimePlayed(Music music)`
    """

def LoadAudioStream(sampleRate: int, sampleSize: int, channels: int) -> AudioStream:
    """Load audio stream (to stream raw audio pcm data)

    Wraps: `AudioStream LoadAudioStream(unsigned int sampleRate, unsigned int sampleSize, unsigned int channels)`
    """

def IsAudioStreamReady(stream: AudioStream) -> bool:
    """Checks if an audio stream is ready

    Wraps: `bool IsAudioStreamReady(AudioStream stream)`
    """

def UnloadAudioStream(stream: AudioStream) -> None:
    """Unload audio stream and free memory

    Wraps: `void UnloadAudioStream(AudioStream stream)`
    """

def UpdateAudioStream(stream: AudioStream, data: void_p, frameCount: int) -> None:
    """Update audio stream buffers with data

    Wraps: `void UpdateAudioStream(AudioStream stream, const void * data, int frameCount)`
    """

def IsAudioStreamProcessed(stream: AudioStream) -> bool:
    """Check if any audio stream buffers requires refill

    Wraps: `bool IsAudioStreamProcessed(AudioStream stream)`
    """

def PlayAudioStream(stream: AudioStream) -> None:
    """Play audio stream

    Wraps: `void PlayAudioStream(AudioStream stream)`
    """

def PauseAudioStream(stream: AudioStream) -> None:
    """Pause audio stream

    Wraps: `void PauseAudioStream(AudioStream stream)`
    """

def ResumeAudioStream(stream: AudioStream) -> None:
    """Resume audio stream

    Wraps: `void ResumeAudioStream(AudioStream stream)`
    """

def IsAudioStreamPlaying(stream: AudioStream) -> bool:
    """Check if audio stream is playing

    Wraps: `bool IsAudioStreamPlaying(AudioStream stream)`
    """

def StopAudioStream(stream: AudioStream) -> None:
    """Stop audio stream

    Wraps: `void StopAudioStream(AudioStream stream)`
    """

def SetAudioStreamVolume(stream: AudioStream, volume: float) -> None:
    """Set volume for audio stream (1.0 is max level)

    Wraps: `void SetAudioStreamVolume(AudioStream stream, float volume)`
    """

def SetAudioStreamPitch(stream: AudioStream, pitch: float) -> None:
    """Set pitch for audio stream (1.0 is base level)

    Wraps: `void SetAudioStreamPitch(AudioStream stream, float pitch)`
    """

def SetAudioStreamPan(stream: AudioStream, pan: float) -> None:
    """Set pan for audio stream (0.5 is centered)

    Wraps: `void SetAudioStreamPan(AudioStream stream, float pan)`
    """

def SetAudioStreamBufferSizeDefault(size: int) -> None:
    """Default size for new audio streams

    Wraps: `void SetAudioStreamBufferSizeDefault(int size)`
    """

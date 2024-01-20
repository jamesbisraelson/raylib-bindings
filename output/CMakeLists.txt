cmake_minimum_required(VERSION 3.15)

project(RaylibW)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 11)

add_subdirectory(../raylib ${CMAKE_CURRENT_BINARY_DIR}/raylib)

add_subdirectory(../pocketpy ${CMAKE_CURRENT_BINARY_DIR}/pocketpy)
target_compile_definitions(pocketpy PUBLIC PK_ENABLE_OS=1)

# build static library
add_library(raylibw STATIC
    raylibw.cpp
)

target_link_libraries(raylibw PUBLIC
    raylib
    pocketpy
)

include_directories(${pocketpy_SOURCE_DIR}/include)
include_directories(${raylib_SOURCE_DIR}/src)

add_executable(raylibw_test
    main.cpp
)

target_link_libraries(raylibw_test PUBLIC
    raylibw
)





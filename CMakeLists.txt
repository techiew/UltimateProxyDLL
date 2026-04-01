cmake_minimum_required(VERSION 3.15)

project(ExampleProxyDLL LANGUAGES CXX)

if (NOT MSVC)
    message(FATAL_ERROR "This project must be built using MSVC due to MSVC-specific linker options.")
endif()

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type")
endif()

add_library(ExampleProxyDLL SHARED DllMain.cpp UltimateProxyDLL.h)
target_compile_features(ExampleProxyDLL PRIVATE cxx_std_11)
set_target_properties(ExampleProxyDLL PROPERTIES LINKER_LANGUAGE CXX OUTPUT_NAME dxgi)
set_property(TARGET ExampleProxyDLL PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded")

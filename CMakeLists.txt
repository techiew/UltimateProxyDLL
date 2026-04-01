cmake_minimum_required(VERSION 3.15)

project(UltimateProxyDLL LANGUAGES CXX)

if (NOT MSVC)
    message(FATAL_ERROR "This project must be built using MSVC due to MSVC-specific linker options.")
endif()

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type")
endif()

add_library(UltimateProxyDLL SHARED DllMain.cpp UltimateProxyDLL.h)
target_compile_features(UltimateProxyDLL PRIVATE cxx_std_11)
set_target_properties(UltimateProxyDLL PROPERTIES LINKER_LANGUAGE CXX OUTPUT_NAME dxgi)
target_link_options(UltimateProxyDLL PRIVATE /INCREMENTAL:NO /IGNORE:4202,4104,4197)
set_property(TARGET UltimateProxyDLL PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded")

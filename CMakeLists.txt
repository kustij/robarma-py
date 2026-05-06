cmake_minimum_required(VERSION 3.15)

# Auto-enable vcpkg when VCPKG_ROOT is provided (useful in CI/cibuildwheel).
if(NOT DEFINED CMAKE_TOOLCHAIN_FILE AND DEFINED ENV{VCPKG_ROOT})
	set(_vcpkg_toolchain "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake")
	if(EXISTS "${_vcpkg_toolchain}")
		set(CMAKE_TOOLCHAIN_FILE "${_vcpkg_toolchain}" CACHE STRING "vcpkg toolchain file")
		message(STATUS "Using vcpkg toolchain: ${CMAKE_TOOLCHAIN_FILE}")
	endif()
endif()

project(robarma_py LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add pybind11
find_package(pybind11 REQUIRED)

# Add the robarma header-only library, but do not install its headers globally
add_subdirectory(external/robarma EXCLUDE_FROM_ALL)




# Create the Python module (scikit-build expects the target to match the import name)
pybind11_add_module(_robarma src/bindings.cpp)

# Include directories
# (Assuming robarma has include/robarma/*.hpp)
target_include_directories(_robarma PRIVATE cpp/robarma/include)

target_link_libraries(_robarma PRIVATE robarma)

# Ensure the extension is installed into the package directory
install(TARGETS _robarma LIBRARY DESTINATION robarma)
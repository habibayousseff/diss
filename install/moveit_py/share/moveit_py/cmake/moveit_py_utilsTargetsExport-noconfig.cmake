#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "moveit_py::moveit_py_utils" for configuration ""
set_property(TARGET moveit_py::moveit_py_utils APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(moveit_py::moveit_py_utils PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libmoveit_py_utils.so."
  IMPORTED_SONAME_NOCONFIG "libmoveit_py_utils.so."
  )

list(APPEND _cmake_import_check_targets moveit_py::moveit_py_utils )
list(APPEND _cmake_import_check_files_for_moveit_py::moveit_py_utils "${_IMPORT_PREFIX}/lib/libmoveit_py_utils.so." )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)

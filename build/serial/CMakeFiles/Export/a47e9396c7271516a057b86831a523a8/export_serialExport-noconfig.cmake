#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "serial::serial" for configuration ""
set_property(TARGET serial::serial APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(serial::serial PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "CXX"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libserial.a"
  )

list(APPEND _cmake_import_check_targets serial::serial )
list(APPEND _cmake_import_check_files_for_serial::serial "${_IMPORT_PREFIX}/lib/libserial.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)

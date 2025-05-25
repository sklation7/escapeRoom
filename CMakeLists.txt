cmake_minimum_required(VERSION 3.13)

# Initialize the SDK
include(pico_sdk_import.cmake)

project(escape_room_pico CXX C ASM)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 11)

# Initializes the pico_sdk from a path defined by PICO_SDK_PATH
# (Must be done before project() but after an initial include of pico_sdk_import.cmake)
pico_sdk_init()

# Add your source files
add_executable(${PROJECT_NAME}
    src/main.cpp
)

# Add pico_stdlib library and any other necessary libraries
target_link_libraries(${PROJECT_NAME} pico_stdlib)

# Enable usb output, enable serial output
pico_enable_stdio_usb(${PROJECT_NAME} 1)
pico_enable_stdio_uart(${PROJECT_NAME} 0)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(${PROJECT_NAME})

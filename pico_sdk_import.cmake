# This is a standard file for Pico projects to locate the SDK
# It is typically copied from the pico-sdk/external directory
# or created manually.

# Path to the Pico SDK (update this if your SDK is in a different location)
set(PICO_SDK_PATH "$ENV{PICO_SDK_PATH}")

if (NOT PICO_SDK_PATH)
    message(FATAL_ERROR "PICO_SDK_PATH not set. Please set this environment variable to point to your Pico SDK installation.")
endif()

# Add the Pico SDK to the CMake module path
list(APPEND CMAKE_MODULE_PATH ${PICO_SDK_PATH}/cmake)

# Include the Pico SDK CMake file
include(pico_sdk_init)

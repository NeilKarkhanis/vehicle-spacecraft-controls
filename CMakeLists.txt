cmake_minimum_required(VERSION 3.16)
project(VehicleSpacecraftControls LANGUAGES CXX)

add_executable(run_vehicle_cpp cpp/run_vehicle.cpp)
set_target_properties(run_vehicle_cpp PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)

include(CTest)
if(BUILD_TESTING)
    find_package(Python3 REQUIRED COMPONENTS Interpreter)
    add_test(NAME vehicle_python_parity
        COMMAND "${Python3_EXECUTABLE}" -m scripts.check_vehicle_parity
                "$<TARGET_FILE:run_vehicle_cpp>"
    )
    set_tests_properties(vehicle_python_parity PROPERTIES
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    )
endif()

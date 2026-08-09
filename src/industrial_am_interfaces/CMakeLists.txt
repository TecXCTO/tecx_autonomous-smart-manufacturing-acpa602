cmake_minimum_required(VERSION 3.8)
project(industrial_am_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate custom structured message pipelines
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MeltpoolTelemetry.msg"
  "srv/EmergencyOverride.srv"
  DEPENDENCIES builtin_interfaces
)

ament_package()

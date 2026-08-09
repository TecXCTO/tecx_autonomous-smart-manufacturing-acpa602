cmake_minimum_required(VERSION 3.8)
project(realtime_hardware_drivers)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -O3) # Force maximum level performance optimization
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

# Compile the Laser Feedback Control Node
add_executable(laser_feedback_node src/laser_feedback_node.cpp)
ament_target_dependencies(laser_feedback_node rclcpp std_msgs)

# Compile the Diagnostic Jitter Profiler Node
add_executable(latency_jitter_analyzer src/latency_jitter_analyzer.cpp)
ament_target_dependencies(latency_jitter_analyzer rclcpp std_msgs)

install(TARGETS
  laser_feedback_node
  latency_jitter_analyzer
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

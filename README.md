# tecx_autonomous-smart-manufacturing-acpa602
TecX(Technology Engineering Computation Expansion) Autonomous Smart Manufacturing acpa(Advanced Cyber-Physical Automation) 602

# Autonomous Smart Manufacturing: Converging Edge AI, ROS 2, and 3D Printing (ACPA-602)

Welcome to the official central engineering workspace repository for the **ACPA-602** curriculum. This repository houses the complete suite of open-source real-time software drivers, neural network quantization configurations, and multi-axis robotics middleware packages utilized throughout the course.

## 🛠️ Main Infrastructure Core Components
* **`/scripts`**: Automated deployment scripts for setting up your environment and patching your system with the real-time `PREEMPT_RT` Linux kernel.
* **`/src/realtime_hardware_drivers`**: Low-latency C++ ROS 2 nodes configured with `Best Effort` QoS streaming properties to analyze latency jitter.
* **`/src/edge_ai_controllers`**: On-device Python inference modules designed to process high-speed image streams locally on edge processors.

## 🚀 One-Click Quickstart Environment Setup
To clone this repository and configure your local ROS 2 network automatically on an Ubuntu 24.04 LTS development station, open your terminal and run:

```bash
wget -qO- https://githubusercontent.com | bash
```

## 📜 Shared Licensing Architecture
All software driver source code streams contained within this workspace are distributed under the protective conditions of the **Apache License, Version 2.0**. All mechanical schematics, wiring maps, and curriculum documentation pages are separately licensed under the **Creative Commons Attribution-ShareAlike 4.0 International Framework (CC BY-SA 4.0)**.

# Repository Description: Official source code, templates, and systems engineering configurations for the ACPA-602 curriculum: Converging Edge AI, ROS 2, PREEMPT_RT, and Hybrid Additive Manufacturing.

```
autonomous-smart-manufacturing-acpa602/
├── .github/
│   └── workflows/
│       ├── ros2_ci_build.yml          # Automated system testing loop configurations
│       └── python_linter.yml          # On-commit quality compilation check
├── config/
│   ├── dds_profile_isolated.xml       # Custom network boundary router settings
│   └── preempt_rt_6.1.46.config       # Pre-configured RTOS kernel profile
├── docs/
│   ├── laboratory_manual_acpa602.pdf  # Comprehensive printable lab workbook
│   └── schematics_motherboard_io.png  # High-resolution hardware pinout maps
├── datasets/
│   ├── calibration_meltpool/          # Tiny image cache used for model quantization
│   └── sample_telemetry_vibration.csv # Baseline datasets for health tracking nodes
├── scripts/
│   ├── setup_ros2_jazzy.sh            # One-click environment bootstrap tool
│   ├── build_preempt_rt_kernel.sh     # Automated RTOS kernel compiler tool
│   └── compress_model_int8.py         # Post-Training Quantization calibration asset
├── src/
│   ├── industrial_am_interfaces/      # Custom structured ROS 2 interface definition
│   │   ├── CMakeLists.txt
│   │   ├── package.xml
│   │   ├── msg/
│   │   │   └── MeltpoolTelemetry.msg  # Specialized real-time data message packet
│   │   └── srv/
│   │       └── EmergencyOverride.srv  # Fast security override message packet
│   ├── edge_ai_controllers/           # Edge processing inference node code (Python)
│   │   ├── package.xml
│   │   ├── setup.py
│   │   └── edge_ai_controllers/
│   │       ├── __init__.py
│   │       ├── advanced_edge_controller.py
│   │       └── camera_exposure_calibrator.py
│   └── realtime_hardware_drivers/     # High-precision C++ driver communication node
│       ├── CMakeLists.txt
│       ├── package.xml
│       ├── include/
│       │   └── qos_policy_config.hpp  # Low-overhead real-time QoS profiles
│       └── src/
│           ├── laser_feedback_node.cpp
│           └── latency_jitter_analyzer.cpp
├── LICENSE                            # Shared Open-Source Licensure Mandate
└── README.md                          # Main repository dashboard page
```


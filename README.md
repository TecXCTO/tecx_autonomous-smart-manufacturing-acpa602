# tecx_autonomous-smart-manufacturing-acpa602
TecX(Technology Engineering Computation Expansion) Autonomous Smart Manufacturing acpa(Advanced Cyber-Physical Automation) 602

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

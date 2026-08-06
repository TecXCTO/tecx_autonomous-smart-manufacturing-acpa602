# ACPA-602 Codebase Contribution & Development Guidelines

Thank you for contributing to the Advanced Cyber-Physical Automation Open-Source Hub! To maintain strict code quality, safety, and compliance with our multi-robot workspace standards, all code updates must pass this review process.

## 🛠️ The Pull Request (PR) Workflow Architecture
1. **Fork the Workspace:** Generate a private or tracking development fork of this repository to your profile space.
2. **Isolate Your Code Changes:** Create a clean, descriptive feature branch before modifying code lines:
   ```bash
   git checkout -b feature/optimize-int8-NPU-quantizer
   ```
3. **Run Automated Compilation Checks:** Before committing, verify your local code builds without errors on your local machine:
   ```bash
   colcon build --packages-select realtime_hardware_drivers
   ```
4. **Submit a Merge Request:** Open a Pull Request targeting our `development` branch. Do not target the `main` stable production branch directly.

## 📜 Strict Coding Standards & Code Quality Targets
* **C++ Memory Guardrails:** All real-time driver definitions must utilize low-overhead parameters, avoid standard heap memory allocations (`new`/`delete`) inside active execution tracks, and strictly follow the custom `PREEMPT_RT` determinism guidelines.
* **QoS Compliance Rule:** Sensor telemetry tracking streams must retain a `Best Effort` QoS profile configuration to prevent queue bottlenecks.
* **Licensure Sign-Off:** By submitting a pull request, you explicitly agree to license your code additions under our repository's default **Apache License, Version 2.0**.
* 

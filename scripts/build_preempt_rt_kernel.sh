#!/bin/bash
# Automated RTOS Kernel Compiler Pipeline Tool
set -e

KERNEL_V="6.1.46"
PATCH_V="6.1.46-rt13"
BUILD_DIR="$HOME/kernel_workspace"

mkdir -p "$BUILD_DIR" && cd "$BUILD_DIR"

echo "=== Pulling Linux Engine Tar Archives ==="
wget -c https://kernel.org{KERNEL_V}.tar.xz
wget -c https://kernel.org{PATCH_V}.patch.xz

tar -xf linux-${KERNEL_V}.tar.xz
cd linux-${KERNEL_V}

echo "=== Injecting Real-Time Patch Set ==="
xzcat ../patch-${PATCH_V}.patch.xz | patch -p1

echo "=== Loading Course Hard Real-Time Baseline Overrides ==="
# Pull the pre-configured RTOS kernel profile from the local config repository path
cp ~/autonomous-smart-manufacturing-acpa602/config/preempt_rt_6.1.46.config .config
make olddefconfig

echo "=== Running Multi-Threaded Compilation Loop ==="
make -j$(nproc) deb-pkg

echo "Kernel built successfully. Run 'sudo dpkg -i ../*.deb' to flash the target real-time OS."

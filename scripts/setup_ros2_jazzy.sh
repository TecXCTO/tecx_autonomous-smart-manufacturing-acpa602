#!/bin/bash
# One-Click Environment Bootstrap Setup Tool
set -e

echo "=== [1/3] System Locale Calibration ==="
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

echo "=== [2/3] Adding ROS 2 Official GPG Sign Keys & Repos ==="
sudo apt install software-properties-common curl -y
sudo curl -sSL https://githubusercontent.com -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://ros.org $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

echo "=== [3/3] Installing ROS 2 Jazzy & Development Dependencies ==="
sudo apt update
sudo apt install -y ros-jazzy-ros-base python3-colcon-common-extensions python3-rosdep python3-argcomplete
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
    sudo rosdep init
fi
rosdep update

echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "export FASTRTPS_DEFAULT_PROFILES_FILE=$(pwd)/config/dds_profile_isolated.xml" >> ~/.bashrc
echo "Workspace setup completed successfully. Please restart your shell profile."

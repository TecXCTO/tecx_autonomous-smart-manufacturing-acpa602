from setuptools import find_packages, setup

package_name = "edge_ai_controllers"

setup(
    name=package_name,
    version="6.2.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Advanced Automation Lab Director",
    maintainer_email="labs@automation.edu",
    description="Python nodes for running low-latency Edge AI inference pipelines.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "advanced_edge_controller = edge_ai_controllers.advanced_edge_controller:main",
            "camera_exposure_calibrator = edge_ai_controllers.camera_exposure_calibrator:main",
        ],
    },
)

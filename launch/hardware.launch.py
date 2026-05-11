#!/usr/bin/env python3

"""Launch file to include all hardware-related launch files."""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def include_launch(package_share_dir: str, launch_file_name: str) -> IncludeLaunchDescription:
    """
    Helper function to include a launch file from a package's share directory.

    Args:
        package_share_dir (str): The path to the package's share directory.
        launch_file_name (str): The name of the launch file to include.

    Returns:
        IncludeLaunchDescription: The included launch description.
    """
    launch_file_path = os.path.join(package_share_dir, "launch", launch_file_name)
    return IncludeLaunchDescription(PythonLaunchDescriptionSource(launch_file_path))


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description that includes all hardware-related nodes.

    Returns:
        LaunchDescription: The composite launch description.
    """
    package_share_dir = get_package_share_directory("stryderx_bringup")

    return LaunchDescription(
        [
            include_launch(package_share_dir, "joystick.launch.py"),
            include_launch(package_share_dir, "drive.launch.py"),
            include_launch(package_share_dir, "steering.launch.py"),
            # include_launch(package_share_dir, "camera.launch.py"),
        ]
    )

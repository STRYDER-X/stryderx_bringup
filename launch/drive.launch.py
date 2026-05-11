#!/usr/bin/env python3

"""Launch file for the drive controller node."""

import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """Generate a launch description for the drive controller node."""
    package_share_dir = get_package_share_directory("stryderx_bringup")

    drive_controller_config_file = os.path.join(
        package_share_dir,
        "config",
        "drive_controller_params.yaml",
    )

    drive_controller_node = Node(
        package="stryderx_hardware",
        executable="drive_controller",
        output="screen",
        parameters=[drive_controller_config_file],
    )

    return LaunchDescription([drive_controller_node])

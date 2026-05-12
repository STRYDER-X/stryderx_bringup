#!/usr/bin/env python3

"""Launch file for the joystick node."""

import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """Generate a launch description for the joystick node."""
    package_share_dir = get_package_share_directory("stryderx_bringup")

    joystick_config_file = os.path.join(
        package_share_dir,
        "config",
        "joystick_params.yaml",
    )

    joystick_node = Node(
        package="joy",
        executable="joy_node",
        output="screen",
    )

    joystick_teleop_node = Node(
        package="stryderx_hardware",
        executable="joystick_teleop",
        output="screen",
        parameters=[joystick_config_file],
    )

    return LaunchDescription(
        [
            joystick_node,
            joystick_teleop_node,
        ]
    )

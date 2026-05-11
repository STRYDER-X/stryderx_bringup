#!/usr/bin/env python3

"""Launch file for the steering controller node."""

import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description for the steering controller node.

    Returns:
        LaunchDescription: The launch description for the steering controller node.
    """
    package_share_dir = get_package_share_directory("stryderx_bringup")

    steering_controller_config_file = os.path.join(
        package_share_dir,
        "config",
        "steering_controller_params.yaml",
    )

    steering_controller_node = Node(
        package="stryderx_hardware",
        executable="steering_controller",
        output="screen",
        parameters=[steering_controller_config_file],
    )

    return LaunchDescription([steering_controller_node])

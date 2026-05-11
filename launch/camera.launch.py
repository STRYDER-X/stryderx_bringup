#!/usr/bin/env python3

"""Launch file for the camera server node."""

import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """Generate a launch description for the camera server node."""
    package_share_dir = get_package_share_directory("stryderx_bringup")

    camera_config_file = os.path.join(
        package_share_dir,
        "config",
        "camera_params.yaml",
    )

    camera_server_node = Node(
        package="stryderx_hardware",
        executable="camera_server_node",
        output="screen",
        parameters=[camera_config_file],
    )

    return LaunchDescription([camera_server_node])

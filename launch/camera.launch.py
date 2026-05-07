#!/usr/bin/env python3

"""Launch file for the camera server node."""

from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description for the camera server node.

    Returns:
        LaunchDescription: The launch description for the camera server node.
    """
    camera_server_node = Node(
        package="stryderx_hardware",
        executable="camera_server_node",
        output="screen",
    )

    return LaunchDescription([camera_server_node])

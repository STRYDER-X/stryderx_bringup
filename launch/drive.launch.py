#!/usr/bin/env python3

"""Launch file for the drive controller node."""

from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description for the drive controller node.

    Returns:
        LaunchDescription: The launch description for the drive controller node.
    """
    drive_controller_node = Node(
        package="stryderx_hardware",
        executable="drive_controller",
        output="screen",
    )

    return LaunchDescription([drive_controller_node])

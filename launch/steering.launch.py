#!/usr/bin/env python3

"""Launch file for the steering controller node."""

from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description for the steering controller node.

    Returns:
        LaunchDescription: The launch description for the steering controller node.
    """
    steering_controller_node = Node(
        package="stryderx_hardware",
        executable="steering_controller",
        output="screen",
    )

    return LaunchDescription([steering_controller_node])

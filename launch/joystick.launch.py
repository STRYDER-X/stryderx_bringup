#!/usr/bin/env python3

"""Launch file for the joystick node."""

from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    """
    Generate a launch description for the joystick node.

    Returns:
        LaunchDescription: The launch description for the joystick node.
    """
    joy_node = Node(
        package="joy",
        executable="joy_node",
        output="screen",
    )

    return LaunchDescription([joy_node])

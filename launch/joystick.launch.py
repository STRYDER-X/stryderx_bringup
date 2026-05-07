from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    joy_node = Node(
        package="joy",
        executable="joy_node",
        output="screen",
    )

    return LaunchDescription([joy_node])

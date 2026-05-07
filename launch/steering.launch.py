from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    steering_controller_node = Node(
        package="stryderx_hardware",
        executable="steering_controller",
        output="screen",
    )

    return LaunchDescription([steering_controller_node])

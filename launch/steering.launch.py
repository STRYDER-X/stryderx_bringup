from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    steering_controller_node = Node(
        package="stryderx_hardware",
        executable="steering_controller",
        output="screen",
    )

    return LaunchDescription([steering_controller_node])

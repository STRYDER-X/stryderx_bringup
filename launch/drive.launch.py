from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    drive_controller_node = Node(
        package="stryderx_hardware",
        executable="drive_controller",
        output="screen",
    )

    return LaunchDescription([drive_controller_node])

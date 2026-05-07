from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    camera_server_node = Node(
        package="stryderx_hardware",
        executable="camera_server_node",
        output="screen",
    )

    return LaunchDescription([camera_server_node])

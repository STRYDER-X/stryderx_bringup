from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description() -> LaunchDescription:
    camera_server_node = Node(
        package="stryderx_hardware",
        executable="camera_server_node",
        output="screen",
    )

    return LaunchDescription([camera_server_node])

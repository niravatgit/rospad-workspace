from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='my_talker', executable='my_talker', name='talker'),
        Node(package='my_talker', executable='my_listner', name='listener'),
    ])
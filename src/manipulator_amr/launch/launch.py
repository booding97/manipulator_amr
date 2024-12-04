import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='manipulator_amr',
            executable='server',
            name='server_node'
        ),
        Node(
            package='manipulator_amr',
            executable='amr',
            name='amr_node'
        ),
        Node(
            package='manipulator_amr',
            executable='gui',
            name='gui_node'
        ),
        Node(
            package='manipulator_amr',
            executable='manipulator',
            name='manipulator_node'
        ),

    ])

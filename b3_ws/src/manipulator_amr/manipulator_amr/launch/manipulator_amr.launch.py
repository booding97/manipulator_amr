from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare launch arguments (if needed)
        DeclareLaunchArgument(
            'robot_name', default_value='manipulator_amr', description='The name of the robot'
        ),
        Node(
            package='manipulator_amr',
            executable='server',
            name='server_node',
            output='screen',
            parameters=[{'robot_name': LaunchConfiguration('robot_name')}],
        )
    ])

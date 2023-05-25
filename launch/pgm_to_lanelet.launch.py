# Copyright 2023 Perception for Physical Interaction Laboratory at Poznan University of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    pkg_prefix = FindPackageShare(LaunchConfiguration('param_file_pkg'))
    config = PathJoinSubstitution([pkg_prefix, LaunchConfiguration('param_file')])

    pgm_to_lanelet_node = Node(
        name='pgm_to_lanelet_node',
        namespace='',
        package='pgm_to_lanelet',
        executable='pgm_to_lanelet_node.py',
        parameters=[
                config,
                {'map_yaml_path': LaunchConfiguration('map_yaml_path')}
        ],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info', '--enable-stdout-logs'],
        emulate_tty=True
    )

    return [
        pgm_to_lanelet_node
    ]


def generate_launch_description():
    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            'param_file_pkg',
            default_value='pgm_to_lanelet',
            description='Package name which contains param file.'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'param_file',
            default_value='param/defaults.param.yaml',
            description='Param file (relative path).'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'map_yaml_path',
            description='Path to map config file.'
        )
    )

    return LaunchDescription([
        *declared_arguments,
        OpaqueFunction(function=launch_setup)
    ])
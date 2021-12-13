import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import xacro


def load_file(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, "r") as file:
            return file.read()
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path, "r") as file:
            return yaml.safe_load(file)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def generate_launch_description():
    # MoveItCpp demo executable
    run_moveit_cpp_node = Node(
        name="run_moveit_cpp",
        package="run_moveit_cpp",
        # TODO(henningkayser): add debug argument
        # prefix='xterm -e gdb --args',
        executable="run_moveit_cpp",
        output="screen",
        parameters=[
            moveit_cpp_yaml_file_name,
            robot_description,
            robot_description_semantic,
            kinematics_yaml,
            ompl_planning_pipeline_config,
            moveit_controllers,
            joint_limits_yaml,
        ],
    )
    return LaunchDescription(
        [
            run_moveit_cpp_node,
        ]
        + load_controllers
    )

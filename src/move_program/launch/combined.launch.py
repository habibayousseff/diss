# """
# Combined Launch File:
# This file merges the logic of both your simulation launch (or_sim.launch.py)
# and your MoveIt2 launch (ur_moveit.launch.py) into one unified file.
# It sets up the robot in Gazebo, configures MoveIt2 (with its controllers,
# move_group, and RViz), and launches all necessary simulation and planning nodes.
# All nodes share the same parameter context so that parameters (e.g. robot_description)
# are passed consistently.
# """

# import os
# import yaml
# from pathlib import Path

# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, RegisterEventHandler, ExecuteProcess, OpaqueFunction
# from launch.conditions import IfCondition, UnlessCondition
# from launch.event_handlers import OnProcessExit
# from launch.substitutions import (
#     Command,
#     FindExecutable,
#     LaunchConfiguration,
#     PathJoinSubstitution,
#     IfElseSubstitution,
# )
# from launch_ros.actions import Node
# from ament_index_python.packages import get_package_share_directory

# # ------------------------------------------------------------------------------
# # Helper Function: load_yaml
# # Loads a YAML file from the specified package and file path.
# # ------------------------------------------------------------------------------
# def load_yaml(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)
#     try:
#         with open(absolute_file_path) as file:
#             return yaml.safe_load(file)
#     except OSError:
#         return None

# # ------------------------------------------------------------------------------
# # Function: launch_setup
# # Called by an OpaqueFunction during launch.
# # Gathers all launch arguments, expands the URDF using xacro,
# # and creates nodes for simulation and MoveIt2.
# # ------------------------------------------------------------------------------
# def launch_setup(context, *args, **kwargs):
#     # 1) Gather launch parameters from declared arguments.
#     ur_type = LaunchConfiguration("ur_type").perform(context)
#     safety_limits = LaunchConfiguration("safety_limits").perform(context)
#     safety_pos_margin = LaunchConfiguration("safety_pos_margin").perform(context)
#     safety_k_position = LaunchConfiguration("safety_k_position").perform(context)
#     controllers_file = LaunchConfiguration("controllers_file").perform(context)
#     tf_prefix = LaunchConfiguration("tf_prefix").perform(context)
#     description_file = LaunchConfiguration("description_file").perform(context)
    
#     # or_sim-specific parameters:
#     activate_joint_controller = LaunchConfiguration("activate_joint_controller").perform(context)
#     initial_joint_controller = LaunchConfiguration("initial_joint_controller").perform(context)
#     launch_rviz_sim = LaunchConfiguration("launch_rviz_sim").perform(context)
#     rviz_config_file_sim = LaunchConfiguration("rviz_config_file_sim").perform(context)
#     gazebo_gui = LaunchConfiguration("gazebo_gui").perform(context)
#     world_file = LaunchConfiguration("world_file").perform(context)
    
#     # MoveIt2-specific parameters:
#     warehouse_sqlite_path = LaunchConfiguration("warehouse_sqlite_path").perform(context)
#     launch_servo = LaunchConfiguration("launch_servo").perform(context)
#     use_sim_time = LaunchConfiguration("use_sim_time").perform(context)
#     publish_robot_description_semantic = LaunchConfiguration("publish_robot_description_semantic").perform(context)
    
#     # MoveIt2 RViz-specific parameters:
#     launch_rviz_moveit = LaunchConfiguration("launch_rviz_moveit").perform(context)
#     rviz_config_file_moveit = LaunchConfiguration("rviz_config_file_moveit").perform(context)

#     # 2) Expand the URDF using xacro.
#     robot_description_content = Command(
#         [
#             PathJoinSubstitution([FindExecutable(name="xacro")]),
#             " ",
#             description_file,
#             " ",
#             "safety_limits:=", safety_limits,
#             " ",
#             "safety_pos_margin:=", safety_pos_margin,
#             " ",
#             "safety_k_position:=", safety_k_position,
#             " ",
#             "name:=", "ur",
#             " ",
#             "ur_type:=", ur_type,
#             " ",
#             "tf_prefix:=", tf_prefix,
#             " ",
#             "simulation_controllers:=", controllers_file,
#         ]
#     )
#     robot_description = {"robot_description": robot_description_content}
#     expanded_urdf = robot_description_content.perform(context)


#     # 3) Robot State Publisher: publishes TFs using the robot_description.
#     robot_state_publisher_node = Node(
#         package="robot_state_publisher",
#         executable="robot_state_publisher",
#         output="both",
#         parameters=[{"use_sim_time": True}, robot_description],
#     )

#     # 4) Gazebo Simulation Setup:
#     # 4a) Spawn the robot in Gazebo.
#     gz_spawn_entity = Node(
#         package="ros_gz_sim",
#         executable="create",
#         output="screen",
#         arguments=[
#             "-string",
#             robot_description_content,
#             "-name",
#             "ur",
#             "-allow_renaming",
#             "true",
#         ],
#     )
    
#     # 4b) Include the Gazebo launch file.
#     from launch.launch_description_sources import PythonLaunchDescriptionSource
#     from launch.actions import IncludeLaunchDescription
#     gz_launch_description = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(get_package_share_directory("ros_gz_sim"), "launch", "gz_sim.launch.py")
#         ),
#         launch_arguments={
#             "gz_args": IfElseSubstitution(
#                 LaunchConfiguration("gazebo_gui"),
#                 if_value=[" -r -v 4 ", world_file],
#                 else_value=[" -s -r -v 4 ", world_file],
#             )
#         }.items(),
#     )
    
#     # 4c) Bridge the simulation clock from Gazebo to ROS 2.
#     gz_sim_bridge = Node(
#         package="ros_gz_bridge",
#         executable="parameter_bridge",
#         arguments=["/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"],
#         output="screen",
#     )
    
#     # 5) Joint State Broadcaster and RViz for Simulation:
#     joint_state_broadcaster_spawner = Node(
#         package="controller_manager",
#         executable="spawner",
#         arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
#     )
    
#     rviz_sim_node = Node(
#         package="rviz2",
#         executable="rviz2",
#         name="rviz2_sim",
#         output="log",
#         arguments=["-d", rviz_config_file_sim],
#         condition=IfCondition(LaunchConfiguration("launch_rviz_sim")),
#     )
    
#     delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
#         event_handler=OnProcessExit(
#             target_action=joint_state_broadcaster_spawner,
#             on_exit=[rviz_sim_node],
#         ),
#         condition=IfCondition(LaunchConfiguration("launch_rviz_sim")),
#     )
    
#     initial_joint_controller_spawner_started = Node(
#         package="controller_manager",
#         executable="spawner",
#         arguments=[initial_joint_controller, "-c", "/controller_manager"],
#         condition=IfCondition(LaunchConfiguration("activate_joint_controller")),
#     )
#     initial_joint_controller_spawner_stopped = Node(
#         package="controller_manager",
#         executable="spawner",
#         arguments=[initial_joint_controller, "-c", "/controller_manager", "--stopped"],
#         condition=UnlessCondition(LaunchConfiguration("activate_joint_controller")),
#     )
    
#     # 6) MoveIt2 Side Setup:
#     wait_robot_description = Node(
#         package="ur_robot_driver",
#         executable="wait_for_robot_description",
#         output="screen",
#     )
    
#     from moveit_configs_utils import MoveItConfigsBuilder
#     moveit_config = (
#         MoveItConfigsBuilder(robot_name="ur", package_name="ur_moveit_config")
#         .robot_description_semantic(Path("srdf") / "ur.srdf.xacro", {"name": ur_type})
#         .trajectory_execution(file_path="config/moveit_controllers.yaml")
#         .planning_pipelines(pipelines=["chomp"])
#         .planning_scene_monitor(
#             publish_robot_description=True,
#             publish_robot_description_semantic=True
#         )
#         .to_moveit_configs()
#     )
    
#     warehouse_ros_config = {
#         "warehouse_plugin": "warehouse_ros_sqlite::DatabaseConnection",
#         "warehouse_host": warehouse_sqlite_path,
#     }
    
#     move_group_capabilities = {"capabilities": "move_group/ExecuteTaskSolutionCapability"}
    
#     move_group_node = Node(
#         package="moveit_ros_move_group",
#         executable="move_group",
#         output="screen",
#         parameters=[
#             moveit_config.to_dict(),
#             move_group_capabilities,
#             warehouse_ros_config,
#             {
#                 "use_sim_time": True,
#                 "publish_robot_description_semantic": publish_robot_description_semantic,
#             },
#         ],
#     )
    
#     ros2_controllers_path = os.path.join(
#         get_package_share_directory("ur_moveit_config"), "config", "ros2_controllers.yaml"
#     )
#     ros2_control_node = Node(
#         package="controller_manager",
#         executable="ros2_control_node",
#         parameters=[ros2_controllers_path],
#         output="both",
#     )
    
#     servo_yaml = load_yaml("ur_moveit_config", "config/ur_servo.yaml")
#     servo_params = {"moveit_servo": servo_yaml}
#     servo_node = Node(
#         package="moveit_servo",
#         condition=IfCondition(LaunchConfiguration("launch_servo")),
#         executable="servo_node",
#         parameters=[moveit_config.to_dict(), servo_params],
#         output="screen",
#     )
    
#     rviz_moveit_node = Node(
#         package="rviz2",
#         condition=IfCondition(LaunchConfiguration("launch_rviz_moveit")),
#         executable="rviz2",
#         name="rviz2_moveit",
#         output="log",
#         arguments=["-d", rviz_config_file_moveit],
#         parameters=[
#             moveit_config.robot_description,
#             moveit_config.robot_description_semantic,
#             moveit_config.robot_description_kinematics,
#             moveit_config.planning_pipelines,
#             moveit_config.joint_limits,
#             warehouse_ros_config,
#             {"use_sim_time": True},
#         ],
#     )
    
#     robot_description_publisher_node = Node(
#         package="move_program",  # your package name
#         executable="robot_description_publisher.py",
#         parameters=[{"use_sim_time": True}, expanded_urdf],
#         output="screen"
#     )
    
#     delay_move_group_after_wait = RegisterEventHandler(
#         event_handler=OnProcessExit(
#             target_action=wait_robot_description,
#             on_exit=[move_group_node, rviz_moveit_node, servo_node],
#         )
#     )
    
#     spawn_controllers = []
#     for ctrl in ["joint_state_broadcaster", "scaled_joint_trajectory_controller"]:
#         spawn_controllers.append(
#             ExecuteProcess(
#                 cmd=["ros2 run controller_manager spawner {}".format(ctrl)],
#                 shell=True,
#                 output="screen",
#             )
#         )
    
#     # 7) Gather All Nodes from both simulation and MoveIt sides.
#     nodes_to_start = [
#         robot_state_publisher_node,
#         gz_spawn_entity,
#         gz_launch_description,
#         gz_sim_bridge,
#         joint_state_broadcaster_spawner,
#         delay_rviz_after_joint_state_broadcaster_spawner,
#         initial_joint_controller_spawner_stopped,
#         initial_joint_controller_spawner_started,
#         wait_robot_description,
#         delay_move_group_after_wait,
#         ros2_control_node,
#         robot_description_publisher_node,
#     ]
#     nodes_to_start.extend(spawn_controllers)
    
#     return nodes_to_start

# # ------------------------------------------------------------------------------
# # Generate the Launch Description:
# # This function declares launch arguments and uses an OpaqueFunction to create all nodes.
# # ------------------------------------------------------------------------------
# def generate_launch_description():
#     ld = LaunchDescription()

#     # Declare unified launch arguments.
#     ld.add_action(DeclareLaunchArgument("ur_type", default_value="ur5"))
#     ld.add_action(DeclareLaunchArgument("safety_limits", default_value="true"))
#     ld.add_action(DeclareLaunchArgument("safety_pos_margin", default_value="0.15"))
#     ld.add_action(DeclareLaunchArgument("safety_k_position", default_value="20"))
#     ld.add_action(DeclareLaunchArgument("controllers_file", default_value=os.path.join(
#         get_package_share_directory("ur_simulation_gz"), "config", "ur_controllers.yaml"
#     )))
#     ld.add_action(DeclareLaunchArgument("tf_prefix", default_value=""))
#     ld.add_action(DeclareLaunchArgument("description_file", default_value=os.path.join(
#         get_package_share_directory("ur_simulation_gz"), "urdf", "ur_gz.urdf.xacro"
#     )))
#     # or_sim-specific arguments.
#     ld.add_action(DeclareLaunchArgument("activate_joint_controller", default_value="true"))
#     ld.add_action(DeclareLaunchArgument("initial_joint_controller", default_value="scaled_joint_trajectory_controller"))
#     ld.add_action(DeclareLaunchArgument("launch_rviz_sim", default_value="false"))
#     ld.add_action(DeclareLaunchArgument("rviz_config_file_sim", default_value=os.path.join(
#         get_package_share_directory("ur_description"), "rviz", "view_robot.rviz"
#     )))
#     ld.add_action(DeclareLaunchArgument("gazebo_gui", default_value="true"))
#     # <<-- Here we set the world_file to the absolute path from your or_sim.launch.py:
#     ld.add_action(DeclareLaunchArgument("world_file", default_value="/home/habibahassan/project/src/Universal_Robots_ROS2_GZ_Simulation/ur_simulation_gz/worlds/trial.sdf"))
    
#     # MoveIt-specific arguments.
#     ld.add_action(DeclareLaunchArgument("warehouse_sqlite_path", default_value="~/.ros/warehouse_ros.sqlite"))
#     ld.add_action(DeclareLaunchArgument("launch_servo", default_value="false"))
#     ld.add_action(DeclareLaunchArgument("use_sim_time", default_value="true"))
#     ld.add_action(DeclareLaunchArgument("publish_robot_description_semantic", default_value="true"))
#     ld.add_action(DeclareLaunchArgument("launch_rviz_moveit", default_value="true"))
#     ld.add_action(DeclareLaunchArgument("rviz_config_file_moveit", default_value=os.path.join(
#         get_package_share_directory("ur_moveit_config"), "config", "moveit.rviz"
#     )))
    
#     from launch.actions import OpaqueFunction
#     ld.add_action(OpaqueFunction(function=launch_setup))

#     return ld

# if __name__ == '__main__':
#     generate_launch_description()

"""
Combined Launch File:
This file merges the logic of both your simulation launch (or_sim.launch.py)
and your MoveIt2 launch (ur_moveit.launch.py) into one unified file.
It sets up the robot in Gazebo, configures MoveIt2 (with its controllers,
move_group, and RViz), and launches all necessary simulation and planning nodes.
All nodes share the same parameter context so that parameters (e.g. robot_description)
are passed consistently.
"""

import os
import yaml
from pathlib import Path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, ExecuteProcess, OpaqueFunction
from launch.conditions import IfCondition, UnlessCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    IfElseSubstitution,
)
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

# ------------------------------------------------------------------------------
# Helper Function: load_yaml
# Loads a YAML file from the specified package and file path.
# ------------------------------------------------------------------------------
def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:
        return None

# ------------------------------------------------------------------------------
# Function: launch_setup
# Called by an OpaqueFunction during launch.
# Gathers all launch arguments, expands the URDF using xacro,
# and creates nodes for simulation and MoveIt2.
# ------------------------------------------------------------------------------
def launch_setup(context, *args, **kwargs):
    # 1) Gather launch parameters from declared arguments.
    ur_type = LaunchConfiguration("ur_type").perform(context)
    safety_limits = LaunchConfiguration("safety_limits").perform(context)
    safety_pos_margin = LaunchConfiguration("safety_pos_margin").perform(context)
    safety_k_position = LaunchConfiguration("safety_k_position").perform(context)
    controllers_file = LaunchConfiguration("controllers_file").perform(context)
    tf_prefix = LaunchConfiguration("tf_prefix").perform(context)
    description_file = LaunchConfiguration("description_file").perform(context)
    
    # or_sim-specific parameters:
    activate_joint_controller = LaunchConfiguration("activate_joint_controller").perform(context)
    initial_joint_controller = LaunchConfiguration("initial_joint_controller").perform(context)
    launch_rviz_sim = LaunchConfiguration("launch_rviz_sim").perform(context)
    rviz_config_file_sim = LaunchConfiguration("rviz_config_file_sim").perform(context)
    gazebo_gui = LaunchConfiguration("gazebo_gui").perform(context)
    world_file = LaunchConfiguration("world_file").perform(context)
    
    # MoveIt2-specific parameters:
    warehouse_sqlite_path = LaunchConfiguration("warehouse_sqlite_path").perform(context)
    launch_servo = LaunchConfiguration("launch_servo").perform(context)
    use_sim_time = LaunchConfiguration("use_sim_time").perform(context)
    publish_robot_description_semantic = LaunchConfiguration("publish_robot_description_semantic").perform(context)
    
    # MoveIt2 RViz-specific parameters:
    launch_rviz_moveit = LaunchConfiguration("launch_rviz_moveit").perform(context)
    rviz_config_file_moveit = LaunchConfiguration("rviz_config_file_moveit").perform(context)

    # 2) Expand the URDF using xacro.
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            description_file,
            " ",
            "safety_limits:=", safety_limits,
            " ",
            "safety_pos_margin:=", safety_pos_margin,
            " ",
            "safety_k_position:=", safety_k_position,
            " ",
            "name:=", "ur",
            " ",
            "ur_type:=", ur_type,
            " ",
            "tf_prefix:=", tf_prefix,
            " ",
            "simulation_controllers:=", controllers_file,
        ]
    )
    robot_description = {"robot_description": robot_description_content}
    expanded_urdf = robot_description_content.perform(context)


    # 3) Robot State Publisher: publishes TFs using the robot_description.
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{"use_sim_time": True}, robot_description],
    )

    # 4) Gazebo Simulation Setup:
    # 4a) Spawn the robot in Gazebo.
    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-string",
            robot_description_content,
            "-name",
            "ur",
            "-allow_renaming",
            "true",
        ],
    )
    
    # 4b) Include the Gazebo launch file.
    from launch.launch_description_sources import PythonLaunchDescriptionSource
    from launch.actions import IncludeLaunchDescription
    gz_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("ros_gz_sim"), "launch", "gz_sim.launch.py")
        ),
        launch_arguments={
            "gz_args": IfElseSubstitution(
                LaunchConfiguration("gazebo_gui"),
                if_value=[" -r -v 4 ", world_file],
                else_value=[" -s -r -v 4 ", world_file],
            )
        }.items(),
    )
    
    # 4c) Bridge the simulation clock from Gazebo to ROS 2.
    gz_sim_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=["/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"],
        output="screen",
    )
    
    # 5) Joint State Broadcaster and RViz for Simulation:
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )
    
    rviz_sim_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2_sim",
        output="log",
        arguments=["-d", rviz_config_file_sim],
        condition=IfCondition(LaunchConfiguration("launch_rviz_sim")),
    )
    
    delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[rviz_sim_node],
        ),
        condition=IfCondition(LaunchConfiguration("launch_rviz_sim")),
    )
    
    initial_joint_controller_spawner_started = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[initial_joint_controller, "-c", "/controller_manager"],
        condition=IfCondition(LaunchConfiguration("activate_joint_controller")),
    )
    initial_joint_controller_spawner_stopped = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[initial_joint_controller, "-c", "/controller_manager", "--stopped"],
        condition=UnlessCondition(LaunchConfiguration("activate_joint_controller")),
    )
    
    # 6) MoveIt2 Side Setup:
    wait_robot_description = Node(
        package="ur_robot_driver",
        executable="wait_for_robot_description",
        output="screen",
    )
    
    from moveit_configs_utils import MoveItConfigsBuilder
    moveit_config = (
        MoveItConfigsBuilder(robot_name="ur", package_name="ur_moveit_config")
        .robot_description_semantic(Path("srdf") / "ur.srdf.xacro", {"name": ur_type})
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .planning_pipelines(pipelines=["ompl"])
        .planning_scene_monitor(
            publish_robot_description=True,
            publish_robot_description_semantic=True
        )
        .to_moveit_configs()
    )
    
    warehouse_ros_config = {
        "warehouse_plugin": "warehouse_ros_sqlite::DatabaseConnection",
        "warehouse_host": warehouse_sqlite_path,
    }
    
    move_group_capabilities = {"capabilities": "move_group/ExecuteTaskSolutionCapability"}
    
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            moveit_config.to_dict(),
            move_group_capabilities,
            warehouse_ros_config,
            {
                "use_sim_time": True,
                "publish_robot_description_semantic": publish_robot_description_semantic,
            },
        ],
    )
    
    ros2_controllers_path = os.path.join(
        get_package_share_directory("ur_moveit_config"), "config", "ros2_controllers.yaml"
    )
    ros2_control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[ros2_controllers_path],
        output="both",
    )
    
    servo_yaml = load_yaml("ur_moveit_config", "config/ur_servo.yaml")
    servo_params = {"moveit_servo": servo_yaml}
    servo_node = Node(
        package="moveit_servo",
        condition=IfCondition(LaunchConfiguration("launch_servo")),
        executable="servo_node",
        parameters=[moveit_config.to_dict(), servo_params],
        output="screen",
    )
    
    rviz_moveit_node = Node(
        package="rviz2",
        condition=IfCondition(LaunchConfiguration("launch_rviz_moveit")),
        executable="rviz2",
        name="rviz2_moveit",
        output="log",
        arguments=["-d", rviz_config_file_moveit],
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            warehouse_ros_config,
            {"use_sim_time": True},
        ],
    )
    
    robot_description_publisher_node = Node(
        package="move_program",  # your package name
        executable="robot_description_publisher.py",
        parameters=[{"use_sim_time": True}, expanded_urdf],
        output="screen"
    )
        
    trial_with_launch_node = Node(
        package="move_program",              # replace with your package name
        executable="trial_with_launch.py",   # the new file to be launched
        output="screen",
        parameters=[
            {"use_sim_time": True},
            robot_description,  # from your launch file’s expanded URDF
            moveit_config.robot_description_semantic,  # from MoveItConfigsBuilder
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            warehouse_ros_config,  # if needed
        ]
    )

    delay_move_group_after_wait = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=wait_robot_description,
            on_exit=[move_group_node, rviz_moveit_node, servo_node],
        )
    )
    
    spawn_controllers = []
    for ctrl in ["joint_state_broadcaster", "scaled_joint_trajectory_controller"]:
        spawn_controllers.append(
            ExecuteProcess(
                cmd=["ros2 run controller_manager spawner {}".format(ctrl)],
                shell=True,
                output="screen",
            )
        )
    
    # 7) Gather All Nodes from both simulation and MoveIt sides.
    nodes_to_start = [
        robot_state_publisher_node,
        gz_spawn_entity,
        gz_launch_description,
        gz_sim_bridge,
        joint_state_broadcaster_spawner,
        delay_rviz_after_joint_state_broadcaster_spawner,
        initial_joint_controller_spawner_stopped,
        initial_joint_controller_spawner_started,
        wait_robot_description,
        delay_move_group_after_wait,
        ros2_control_node,
        robot_description_publisher_node,
        trial_with_launch_node,
    ]
    nodes_to_start.extend(spawn_controllers)
    
    return nodes_to_start

# ------------------------------------------------------------------------------
# Generate the Launch Description:
# This function declares launch arguments and uses an OpaqueFunction to create all nodes.
# ------------------------------------------------------------------------------
def generate_launch_description():
    ld = LaunchDescription()

    # Declare unified launch arguments.
    ld.add_action(DeclareLaunchArgument("ur_type", default_value="ur5"))
    ld.add_action(DeclareLaunchArgument("safety_limits", default_value="true"))
    ld.add_action(DeclareLaunchArgument("safety_pos_margin", default_value="0.15"))
    ld.add_action(DeclareLaunchArgument("safety_k_position", default_value="20"))
    ld.add_action(DeclareLaunchArgument("controllers_file", default_value=os.path.join(
        get_package_share_directory("ur_simulation_gz"), "config", "ur_controllers.yaml"
    )))
    ld.add_action(DeclareLaunchArgument("tf_prefix", default_value=""))
    ld.add_action(DeclareLaunchArgument("description_file", default_value=os.path.join(
        get_package_share_directory("ur_simulation_gz"), "urdf", "ur_gz.urdf.xacro"
    )))
    # or_sim-specific arguments.
    ld.add_action(DeclareLaunchArgument("activate_joint_controller", default_value="true"))
    ld.add_action(DeclareLaunchArgument("initial_joint_controller", default_value="scaled_joint_trajectory_controller"))
    ld.add_action(DeclareLaunchArgument("launch_rviz_sim", default_value="false"))
    ld.add_action(DeclareLaunchArgument("rviz_config_file_sim", default_value=os.path.join(
        get_package_share_directory("ur_description"), "rviz", "view_robot.rviz"
    )))
    ld.add_action(DeclareLaunchArgument("gazebo_gui", default_value="true"))
    # <<-- Here we set the world_file to the absolute path from your or_sim.launch.py:
    ld.add_action(DeclareLaunchArgument("world_file", default_value="/home/habibahassan/project/src/Universal_Robots_ROS2_GZ_Simulation/ur_simulation_gz/worlds/trial.sdf"))
    
    # MoveIt-specific arguments.
    ld.add_action(DeclareLaunchArgument("warehouse_sqlite_path", default_value="~/.ros/warehouse_ros.sqlite"))
    ld.add_action(DeclareLaunchArgument("launch_servo", default_value="false"))
    ld.add_action(DeclareLaunchArgument("use_sim_time", default_value="true"))
    ld.add_action(DeclareLaunchArgument("publish_robot_description_semantic", default_value="true"))
    ld.add_action(DeclareLaunchArgument("launch_rviz_moveit", default_value="true"))
    ld.add_action(DeclareLaunchArgument("rviz_config_file_moveit", default_value=os.path.join(
        get_package_share_directory("ur_moveit_config"), "config", "moveit.rviz"
    )))
    
    from launch.actions import OpaqueFunction
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld

if __name__ == '__main__':
    generate_launch_description()
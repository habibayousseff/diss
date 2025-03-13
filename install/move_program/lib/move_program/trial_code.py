#!/usr/bin/env python3

import os
import sys
import yaml
import rclpy
import numpy as np
from pathlib import Path

# message libraries
from geometry_msgs.msg import PoseStamped, Pose

# moveit_py
from moveit.planning import MoveItPy
from moveit.core.robot_state import RobotState

# config file libraries
from moveit_configs_utils import MoveItConfigsBuilder
from ament_index_python.packages import get_package_share_directory
  
builder = (
    MoveItConfigsBuilder(robot_name="ur", package_name="ur_moveit_config")
    .robot_description_semantic(Path("srdf") / "ur.srdf.xacro", {"name": "ur5"})
    .trajectory_execution(file_path="config/moveit_controllers.yaml")
    .planning_pipelines(pipelines=["chomp"])
    .planning_scene_monitor(
        publish_robot_description=True,
        publish_robot_description_semantic=True,
    )
    .moveit_cpp(
        file_path=os.path.join(
            get_package_share_directory("ur_moveit_config"),
            "config",
            "chomp_planning.yaml",
        )
    )
)

moveit_config = builder.to_moveit_configs().to_dict()

# initialise rclpy (only for logging purposes)
rclpy.init()

# instantiate moveit_py instance and a planning component for the panda_arm
ur = MoveItPy(node_name="moveit_py", config_dict=moveit_config)
ur_manipulator = ur.get_planning_component("ur_manipulator")

def plan_and_execute(
        robot,
        planning_component,
        single_plan_parameters=None,
        multi_plan_parameters=None,
):
        """A helper function to plan and execute a motion."""
        # plan to goal
        if multi_plan_parameters is not None:
                plan_result = planning_component.plan(
                        multi_plan_parameters=multi_plan_parameters
                )
        elif single_plan_parameters is not None:
                plan_result = planning_component.plan(
                single_plan_parameters=single_plan_parameters
        )
        else:
                plan_result = planning_component.plan()

        # execute the plan
        if plan_result:
                robot_trajectory = plan_result.trajectory
                robot.execute(robot_trajectory, controllers=[])
        else:
                print("Planning failed")
                
# set plan start state using predefined state
ur_manipulator.set_start_state("ready")

# set pose goal using predefined state
ur_manipulator.set_goal_state(configuration_name = "extended")

# plan to goal
plan_and_execute(ur, ur_manipulator)

# set plan start state using predefined state
ur_manipulator.set_start_state_to_current_state()

# set goal using a pose message this time
pose_goal = PoseStamped()
pose_goal.header.frame_id = "base_link"
pose_goal.pose.orientation.w = 1.0
pose_goal.pose.position.x = 0.28
pose_goal.pose.position.y = -0.2
pose_goal.pose.position.z = 0.5
ur_manipulator.set_goal_state(pose_stamped_msg = pose_goal, pose_link = "wrist_link3")

# plan to goal
plan_and_execute(ur, ur_manipulator)
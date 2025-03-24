#!/usr/bin/env python3

"""
unified_llm_nav.py
One single node that:
 - Provides a text-based interface to an LLM (OpenAI GPT).
 - Moves the UR end effector to named cup goals in a MoveIt environment.

To run interactively in a separate console, do:
  ros2 run move_program unified_llm_nav.py

Or if you want to have it launched automatically with your Gazebo + MoveIt,
add it as a Node(...) in your combined.launch.py. 
But be aware that interactive input might be messy if logs stream to the same console.
"""

import os
import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

import openai

# MoveIt / geometry message imports
from geometry_msgs.msg import Pose
from shape_msgs.msg import SolidPrimitive
from moveit_msgs.msg import (
    MotionPlanRequest,
    Constraints,
    PositionConstraint,
    OrientationConstraint,
    PlanningOptions
)
from moveit_msgs.action import MoveGroup, ExecuteTrajectory

print(openai.__version__)

# openai.api_key = "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"

# response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}]
# )
# print(response)

# Hard-coded dictionary of known object poses
OBJECT_GOALS = {
    "RedCup": {
        "position": [1.01, 1.295022, 1.27],
        "orientation": [0.720, 0.694, -0.029, -0.013]
    },
    "GreenCup": {
        "position": [1.148940, 1.295022, 1.27],
        "orientation": [0.714, 0.699, -0.032, -0.041]
    },
    "BlueCup": {
        "position": [1.29, 1.27, 1.27],
        "orientation": [0.714, 0.699, -0.032, -0.041]
    },
    "YellowCup": {
        "position": [0.963062, 1.461358, 1.27],
        "orientation": [0.714, 0.699, -0.032, -0.041]
    },
    "PurpleCup": {
        "position": [1.168, 1.466, 1.27],
        "orientation": [0.714, 0.699, -0.032, -0.041]
    },
}


class LLMAndNavNode(Node):
    def __init__(self):
        super().__init__('llm_and_nav_node')

        # Set your OpenAI API key here or via an environment variable:
        openai.api_key = os.getenv("OPENAI_API_KEY", "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")

        self.get_logger().info("LLM + Navigation Node started. Type commands in console...")

        # Timer to poll for user input every 5 seconds
        self.poll_timer = self.create_timer(5.0, self.poll_user)
        self.busy = False

        # We'll also keep an action client around for MoveGroup
        self._move_client = ActionClient(self, MoveGroup, '/move_action')
        self._exec_client = ActionClient(self, ExecuteTrajectory, '/execute_trajectory')

    def poll_user(self):
        """Called periodically to ask the user for text input in the same console."""
        if self.busy:
            return
        self.busy = True

        user_text = input("\nType a command (e.g. 'Go to red cup'): ")
        if not user_text.strip():
            self.busy = False
            return

        # Step 1: Query GPT or GPT-4
        response = self.query_llm(user_text)

        # Step 2: Look for color in the LLM's text
        self.get_logger().info(f"LLM says: {response}")
        color = self.extract_color_from_response(response)

        # If found a color, do a move
        if color:
            self.get_logger().info(f"Detected color: {color}. Moving now.")
            self.move_to_named_goal(color)
        else:
            self.get_logger().info("No recognized color found in LLM response.")

        self.busy = False

    def query_llm(self, prompt_text):
        """Minimal call to GPT-4 or GPT-3.5 via openai API"""
        try:
            resp = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", 
                     "content": "You are a helpful robotics assistant. We have cups named RedCup, GreenCup, BlueCup, YellowCup, PurpleCup. If user wants to go to a cup, mention the color in your suggestion."},
                    {"role": "user", "content": prompt_text},
                ],
                temperature=0.0,
            )
            return resp.choices[0].message.content
        except Exception as e:
            self.get_logger().error(f"OpenAI API error: {str(e)}")
            return "Error: could not query LLM"

    def extract_color_from_response(self, response_text):
        """Naive check for color keywords in LLM response."""
        lower = response_text.lower()
        for color in ["red", "green", "blue", "yellow", "purple"]:
            if color in lower:
                # Return the dictionary key: RedCup, GreenCup, etc.
                # We'll do a simple capital approach:
                return color.capitalize() + "Cup"
        return None

    def move_to_named_goal(self, goal_name: str):
        """Send a MoveGroup action request to plan to the named goal (dictionary above)."""
        if goal_name not in OBJECT_GOALS:
            self.get_logger().error(f"No known goal for {goal_name}")
            return

        # Wait for servers
        self.get_logger().info("Waiting for /move_action server...")
        self._move_client.wait_for_server()
        self.get_logger().info("Waiting for /execute_trajectory server...")
        self._exec_client.wait_for_server()

        # Build the MoveGroup request
        pos = OBJECT_GOALS[goal_name]["position"]
        ori = OBJECT_GOALS[goal_name]["orientation"]

        goal_msg = MoveGroup.Goal()
        request = MotionPlanRequest()
        request.group_name = "ur_manipulator"
        request.allowed_planning_time = 5.0
        request.max_velocity_scaling_factor = 0.7
        request.max_acceleration_scaling_factor = 0.7

        constraints = Constraints()

        # PositionConstraint
        pc = PositionConstraint()
        pc.header.frame_id = "world"
        pc.link_name = "tool0"
        pc.weight = 1.0

        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.008]  # small bounding region
        sphere_pose = Pose()
        sphere_pose.position.x = pos[0]
        sphere_pose.position.y = pos[1]
        sphere_pose.position.z = pos[2]
        sphere_pose.orientation.w = 1.0
        pc.constraint_region.primitives.append(sphere)
        pc.constraint_region.primitive_poses.append(sphere_pose)

        # OrientationConstraint
        oc = OrientationConstraint()
        oc.header.frame_id = "world"
        oc.link_name = "tool0"
        oc.orientation.x = ori[0]
        oc.orientation.y = ori[1]
        oc.orientation.z = ori[2]
        oc.orientation.w = ori[3]
        oc.absolute_x_axis_tolerance = 0.1
        oc.absolute_y_axis_tolerance = 0.1
        oc.absolute_z_axis_tolerance = 0.1
        oc.weight = 1.0

        constraints.position_constraints.append(pc)
        constraints.orientation_constraints.append(oc)
        request.goal_constraints.append(constraints)

        # Minimal planning options
        planning_options = PlanningOptions()
        planning_options.planning_scene_diff.is_diff = True
        planning_options.planning_scene_diff.robot_state.is_diff = True

        goal_msg.request = request
        goal_msg.planning_options = planning_options

        self.get_logger().info(f"Sending MoveIt goal for: {goal_name}")
        future = self._move_client.send_goal_async(goal_msg, feedback_callback=self.feedback_cb)
        future.add_done_callback(self.goal_response_cb)

    def feedback_cb(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback}")

    def goal_response_cb(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error("MoveGroup goal was rejected.")
            return

        self.get_logger().info("Goal accepted; waiting for result...")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_cb)

    def result_cb(self, future):
        result = future.result().result
        if result.error_code.val == 1:
            self.get_logger().info("Motion planning + execution succeeded!")
        else:
            self.get_logger().error(f"Motion failed with error code: {result.error_code.val}")


def main(args=None):
    rclpy.init(args=args)
    node = LLMAndNavNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

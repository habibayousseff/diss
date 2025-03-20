#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped, Quaternion
from moveit_msgs.msg import (
    MotionPlanRequest,
    Constraints,
    PositionConstraint,
    OrientationConstraint,
    PlanningOptions
)
from moveit_msgs.action import MoveGroup, ExecuteTrajectory

from math import sin, cos
# If you store Euler angles, you'll want to convert to quaternions. 
# Or just store quaternions directly in the dictionary.

# Import the dictionary of known object poses:

OBJECT_GOALS = {
    "RedCup": {
        "position": [1.26495221, 1.711521262, 1.160112403],
        "orientation": [0.0, 0.0, 0.0, 1.0]
    },
    
# EE Position - x: 1.274, y: 1.352, z: 1.195
# EE Orientation - x: 0.668, y: 0.743, z: -0.043, w: 0.026  
    "GreenCup": {
        "position": [1.274, 1.352, 1.195],
        "orientation": [0.668, 0.743, -0.043, -0.026]
    },
    "BlueCup": {
        "position": [1.8295634595, 1.8338560006, 1.1601171328],
        "orientation": [0.0, 0.0, 0.0, 1.0]
    },
    "YellowCup": {
        "position": [1.2721769239, 2.0702431481, 1.1601075924],
        "orientation": [0.0, 0.0, 0.0, 1.0]
    },
    "PurpleCup": {
        "position": [1.8936378055, 2.2400947626, 1.1604751876],
        "orientation": [0.0, 0.0, 0.0, 1.0]
    },
}


class PredefinedObjectClient(Node):
    def __init__(self, goal_name):
        super().__init__('predefined_object_client')
        self._move_client = ActionClient(self, MoveGroup, '/move_action')
        self._exec_client = ActionClient(self, ExecuteTrajectory, '/execute_trajectory')
        self.done = False
        self.goal_name = goal_name

    def send_goal(self):
        self.get_logger().info("Waiting for /move_action server...")
        self._move_client.wait_for_server()
        self.get_logger().info("Waiting for /execute_trajectory server...")
        self._exec_client.wait_for_server()

        # 1) Lookup the goal pose from the dictionary
        if self.goal_name not in OBJECT_GOALS:
            self.get_logger().error(f"Goal '{self.goal_name}' not found in OBJECT_GOALS!")
            self.done = True
            return

        pos = OBJECT_GOALS[self.goal_name]["position"]  # [x, y, z]
        ori = OBJECT_GOALS[self.goal_name]["orientation"] # [qx, qy, qz, qw] or [roll, pitch, yaw] ?

        # If you stored Euler angles, convert them to quaternion here.
        # For example, if orientation=[rx,ry,rz], do the conversion. 
        # Otherwise, skip this if you already have a quaternion in the dictionary.

        # 2) Build the MoveGroup request
        goal_msg = MoveGroup.Goal()
        request = MotionPlanRequest()
        request.group_name = "ur_manipulator"
        request.allowed_planning_time = 5.0
        request.max_velocity_scaling_factor = 0.7
        request.max_acceleration_scaling_factor = 0.7

        # Create a bounding region or direct constraints
        constraints = Constraints()

        pc = PositionConstraint()
        pc.header.frame_id = "world"
        pc.link_name = "tool0"  # or "wrist_3_link" if that’s your actual EE link
        pc.weight = 1.0
        # The bounding region: a small sphere around the target
        from shape_msgs.msg import SolidPrimitive
        from geometry_msgs.msg import Pose

        sphere = SolidPrimitive()
        sphere.type = SolidPrimitive.SPHERE
        sphere.dimensions = [0.01]  # 1 cm radius

        sphere_pose = Pose()
        sphere_pose.position.x = pos[0]
        sphere_pose.position.y = pos[1]
        sphere_pose.position.z = pos[2]
        sphere_pose.orientation.w = 1.0

        pc.constraint_region.primitives.append(sphere)
        pc.constraint_region.primitive_poses.append(sphere_pose)

        oc = OrientationConstraint()
        oc.header.frame_id = "world"
        oc.link_name = pc.link_name
        oc.weight = 1.0
        # If you store a quaternion in ori, fill it here:
        oc.orientation.x = ori[0]
        oc.orientation.y = ori[1]
        oc.orientation.z = ori[2]
        oc.orientation.w = ori[3]
        # Looser or stricter orientation tolerance in radians
        oc.absolute_x_axis_tolerance = 0.1
        oc.absolute_y_axis_tolerance = 0.1
        oc.absolute_z_axis_tolerance = 0.1

        constraints.position_constraints.append(pc)
        constraints.orientation_constraints.append(oc)
        request.goal_constraints.append(constraints)

        # Minimal planning options
        planning_options = PlanningOptions()
        planning_options.planning_scene_diff.is_diff = True
        planning_options.planning_scene_diff.robot_state.is_diff = True

        goal_msg.request = request
        goal_msg.planning_options = planning_options

        # 3) Send the request
        self.get_logger().info(f"Sending MoveIt goal for object: {self.goal_name}")
        future = self._move_client.send_goal_async(goal_msg, feedback_callback=self.feedback_cb)
        future.add_done_callback(self.goal_response_cb)

    def feedback_cb(self, feedback):
        self.get_logger().info(f"Feedback: {feedback.feedback}")

    def goal_response_cb(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error("Goal was rejected by MoveGroup.")
            self.done = True
            return

        self.get_logger().info("Goal accepted. Waiting for result...")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_cb)

    def result_cb(self, future):
        result = future.result().result
        if result.error_code.val == 1:
            self.get_logger().info("Motion planning + execution succeeded!")
        else:
            self.get_logger().error(f"Motion failed with error code: {result.error_code.val}")
        self.done = True

def main(args=None):
    rclpy.init(args=args)

    # Option 1: parse the argument from sys.argv
    # e.g. user does: ros2 run move_program predefined_object_navigation goal:=GreenCup
    # In ROS 2, that usually becomes: --ros-args -p goal:=GreenCup
    # But let's do a quick parse for demonstration:
    goal_name = "GreenCup"  # default
    for arg in sys.argv:
        if "goal:=" in arg:
            goal_name = arg.split(":=")[1]

    node = PredefinedObjectClient(goal_name)
    node.send_goal()

    while rclpy.ok() and not node.done:
        rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

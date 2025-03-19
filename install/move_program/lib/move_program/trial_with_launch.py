#!/usr/bin/env python3




# import rclpy
# from rclpy.node import Node
# from rclpy.action import ActionClient

# from std_msgs.msg import String
# from sensor_msgs.msg import JointState
# from geometry_msgs.msg import PoseStamped
# from moveit_msgs.msg import MotionPlanRequest, PlanningOptions
# from moveit_msgs.action import MoveGroup, ExecuteTrajectory


# class MoveGroupActionClient(Node):
#     def __init__(self):
#         super().__init__('move_group_action_client')
#         # Create action clients for /move_action and /execute_trajectory
#         self._move_action_client = ActionClient(self, MoveGroup, 'move_action')
#         self._execute_action_client = ActionClient(self, ExecuteTrajectory, 'execute_trajectory')

#         # A simple flag to tell our main code when we’re done
#         self.done = False

#     def send_goal(self):
#         """Send a goal to the MoveGroup action server to plan to a pose."""
#         self.get_logger().info("Waiting for /move_action (move_group) server...")
#         self._move_action_client.wait_for_server()

#         self.get_logger().info("Waiting for /execute_trajectory (move_group) server...")
#         self._execute_action_client.wait_for_server()

#         # Build the MoveGroup goal
#         goal_msg = MoveGroup.Goal()
#         request = MotionPlanRequest()
#         request.group_name = "ur_manipulator"  # adjust as needed

#         # Example: target pose for the end-effector
#         pose_goal = PoseStamped()
#         pose_goal.header.frame_id = "world"  # must match the TF target frame
#         pose_goal.pose.position.x = 1.142
#         pose_goal.pose.position.y = 0.283
#         pose_goal.pose.position.z = 1.618
#         pose_goal.pose.orientation.x = -0.021
#         pose_goal.pose.orientation.y = 0.998
#         pose_goal.pose.orientation.z = 0.056
#         pose_goal.pose.orientation.w = 0.008
#         # (In a full example you'd convert pose_goal into constraints.)

#         goal_msg.request = request

#         # Minimal planning options
#         planning_options = PlanningOptions()
#         planning_options.planning_scene_diff.is_diff = True
#         planning_options.planning_scene_diff.robot_state.is_diff = True
#         goal_msg.planning_options = planning_options

#         # Send the goal asynchronously
#         future = self._move_action_client.send_goal_async(
#             goal_msg,
#             feedback_callback=self.feedback_callback
#         )
#         future.add_done_callback(self.goal_response_callback)

#     def feedback_callback(self, feedback_msg):
#         """Called whenever MoveGroup sends intermediate feedback."""
#         self.get_logger().info(f"Feedback: {feedback_msg.feedback}")

#     def goal_response_callback(self, future):
#         """Called once the MoveGroup server has accepted/rejected our goal."""
#         goal_handle = future.result()
#         if not goal_handle.accepted:
#             self.get_logger().error("Goal was rejected by move_group!")
#             self.done = True
#             return

#         self.get_logger().info("Goal accepted; waiting for result...")
#         result_future = goal_handle.get_result_async()
#         result_future.add_done_callback(self.get_result_callback)

#     def get_result_callback(self, future):
#         """Called once the MoveGroup action has a final result (success/fail)."""
#         result = future.result().result
#         self.get_logger().info(f"Final result from move_group: {result}")
#         # Signal that we’re completely done
#         self.done = True


# class ConditionalNode(Node):
#     def __init__(self):
#         super().__init__('conditional_node')
#         self.get_logger().info("Conditional node launched. Press 'x' to plan, anything else to skip...")

#     def run(self):
#         # Wait for user input (blocking)
#         key = input("Press 'x' to run motion planning action, or any other key to do nothing: ")
#         if key.lower() == 'x':
#             self.get_logger().info("Key 'x' pressed -> sending motion plan goal.")
#             mg_client = MoveGroupActionClient()
#             mg_client.send_goal()

#             # Spin “manually” until mg_client.done is True
#             while rclpy.ok() and not mg_client.done:
#                 rclpy.spin_once(mg_client, timeout_sec=0.1)

#             mg_client.destroy_node()
#         else:
#             self.get_logger().info("Key not recognized -> no motion plan.")


# def main(args=None):
#     rclpy.init(args=args)
#     node = ConditionalNode()
#     node.run()
#     # Clean up
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()

















# import rclpy
# import os
# import yaml
# from rclpy.node import Node
# from rclpy.action import ActionClient
# from std_msgs.msg import String
# from sensor_msgs.msg import JointState
# from moveit_msgs.msg import PlanningScene
# from geometry_msgs.msg import PoseStamped
# from ament_index_python.packages import get_package_share_directory

# # MoveIt’s actions
# from moveit_msgs.action import MoveGroup, ExecuteTrajectory
# from moveit_msgs.msg import MotionPlanRequest, PlanningOptions
# from action_msgs.msg import GoalStatusArray  # (if needed for status)

# # Helper function to load YAML files (if needed)
# def load_yaml(package_name, file_path):
#     package_path = get_package_share_directory(package_name)
#     absolute_file_path = os.path.join(package_path, file_path)
#     try:
#         with open(absolute_file_path) as file:
#             return yaml.safe_load(file)
#     except OSError:
#         return None

# # (Optional) load servo parameters
# servo_yaml = load_yaml("ur_moveit_config", "config/ur_servo.yaml")
# servo_params = {"moveit_servo": servo_yaml}


# class MoveGroupActionClient(Node):
#     def __init__(self):
#         super().__init__('move_group_action_client')
#         # Create action clients for /move_action and /execute_trajectory
#         self._move_action_client = ActionClient(self, MoveGroup, 'move_action/_action')
#         self._execute_action_client = ActionClient(self, ExecuteTrajectory, 'execute_trajectory/_action')
#         self.done = False  # flag to signal completion

#     def send_goal(self):
#         self.get_logger().info("Waiting for move_action server...")
#         self._move_action_client.wait_for_server()
#         self.get_logger().info("Waiting for execute_trajectory server...")
#         self._execute_action_client.wait_for_server()

#         # Build the MoveGroup goal
#         goal_msg = MoveGroup.Goal()

#         # Build a minimal MotionPlanRequest:
#         request = MotionPlanRequest()
#         request.group_name = "ur_manipulator"  # adjust to your planning group
#         # Define the desired end-effector pose
#         pose_goal = PoseStamped()
#         pose_goal.header.frame_id = "world"  # adjust as needed (world or base_link)
#         pose_goal.pose.position.x = 1.142
#         pose_goal.pose.position.y = 0.283
#         pose_goal.pose.position.z = 1.618
#         pose_goal.pose.orientation.x = -0.021
#         pose_goal.pose.orientation.y = 0.998
#         pose_goal.pose.orientation.z = 0.056
#         pose_goal.pose.orientation.w = 0.008
#         # In a complete implementation, you would convert pose_goal to goal constraints
#         # For this example, we assume the MoveGroup action server uses the request fields.

#         # (You might add: request.goal_constraints = your_constraint_function(pose_goal))
#         # For now, we simply store the group name in the request.
#         goal_msg.request = request

#         # Specify planning options
#         planning_options = PlanningOptions()
#         planning_options.planning_scene_diff.is_diff = True
#         planning_options.planning_scene_diff.robot_state.is_diff = True
#         goal_msg.planning_options = planning_options

#         self.get_logger().info("Sending motion planning goal...")
#         send_goal_future = self._move_action_client.send_goal_async(
#             goal_msg, feedback_callback=self.feedback_callback
#         )
#         send_goal_future.add_done_callback(self.goal_response_callback)

#     def feedback_callback(self, feedback_msg):
#         self.get_logger().info(f"Feedback: {feedback_msg.feedback}")

#     def goal_response_callback(self, future):
#         goal_handle = future.result()
#         if not goal_handle.accepted:
#             self.get_logger().error("Goal rejected by move_group")
#             self.done = True
#             return
#         self.get_logger().info("Goal accepted; waiting for result...")
#         goal_handle.get_result_async().add_done_callback(self.get_result_callback)

#     def get_result_callback(self, future):
#         result = future.result().result
#         self.get_logger().info(f"Final result from move_group: {result}")
#         self.done = True


# class ConditionalNode(Node):
#     def __init__(self):
#         super().__init__('conditional_node')
#         self.get_logger().info("Conditional node launched. Waiting for key press...")

#     def run(self):
#         key = input("Press 'x' to execute motion planning action, or any other key to do nothing: ")
#         if key.lower() == 'x':
#             self.get_logger().info("Key 'x' pressed. Executing motion planning action.")
#             mg_client = MoveGroupActionClient()
#             mg_client.send_goal()
#             # Spin until the action client is done
#             while rclpy.ok() and not mg_client.done:
#                 rclpy.spin_once(mg_client, timeout_sec=0.1)
#             mg_client.destroy_node()
#         else:
#             self.get_logger().info("Key not recognized; no action executed.")


# def main(args=None):
#     rclpy.init(args=args)
#     node = ConditionalNode()
#     node.run()
#     node.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()


























import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import MotionPlanRequest, PlanningOptions
from moveit_msgs.action import MoveGroup, ExecuteTrajectory
from moveit_msgs.msg import Constraints, PositionConstraint, OrientationConstraint


class MoveGroupActionClient(Node):
    def __init__(self):
        super().__init__('move_group_action_client')
        # Use the corrected action server names based on rqt graph
        self._move_action_client = ActionClient(self, MoveGroup, '/move_action')
        self._execute_action_client = ActionClient(self, ExecuteTrajectory, '/execute_trajectory')

        # A simple flag to track when execution is complete
        self.done = False

    def send_goal(self):
        """Send a goal to the MoveGroup action server to plan to a pose."""
        self.get_logger().info("Waiting for /move_action (MoveGroup) server...")
        self._move_action_client.wait_for_server()

        self.get_logger().info("Waiting for /execute_trajectory (ExecuteTrajectory) server...")
        self._execute_action_client.wait_for_server()

        # Build the MoveGroup goal
        goal_msg = MoveGroup.Goal()
        request = MotionPlanRequest()
        request.group_name = "ur_manipulator"

        # Define the goal constraints properly
        pose_goal = PoseStamped()
        pose_goal.header.frame_id = "world"
        pose_goal.pose.position.x = 1.142
        pose_goal.pose.position.y = 0.283
        pose_goal.pose.position.z = 1.618
        # pose_goal.pose.orientation.x = -0.021
        # pose_goal.pose.orientation.y = 0.998
        # pose_goal.pose.orientation.z = 0.056
        # pose_goal.pose.orientation.w = 0.009

        # pose_goal = PoseStamped()
        # pose_goal.header.frame_id = "base_link"
        # pose_goal.pose.position.x = -0.087
        # pose_goal.pose.position.y =  0.448
        # pose_goal.pose.position.z =  0.510
        # pose_goal.pose.orientation.x = 0.997
        # pose_goal.pose.orientation.y = 0.031
        # pose_goal.pose.orientation.z = 0.000
        # pose_goal.pose.orientation.w =  0.067
        
        # Convert pose into a constraint
        constraint = Constraints()

        # Position Constraint
        position_constraint = PositionConstraint()
        position_constraint.header.frame_id = "world"
        position_constraint.link_name = "wrist_3_link"  # Ensure this is your end-effector link
        position_constraint.target_point_offset.x = 1.142
        position_constraint.target_point_offset.y = 0.283
        position_constraint.target_point_offset.z = 1.618

        constraint.position_constraints.append(position_constraint)

        # Orientation Constraint
        orientation_constraint = OrientationConstraint()
        orientation_constraint.header.frame_id = "world"
        orientation_constraint.link_name = "wrist_3_link"
        orientation_constraint.orientation = pose_goal.pose.orientation
        orientation_constraint.absolute_x_axis_tolerance = 0.1
        orientation_constraint.absolute_y_axis_tolerance = 0.1
        orientation_constraint.absolute_z_axis_tolerance = 0.1
        orientation_constraint.weight = 1.0

        constraint.orientation_constraints.append(orientation_constraint)

        request.goal_constraints.append(constraint)

        goal_msg.request = request

        # Minimal planning options
        planning_options = PlanningOptions()
        planning_options.planning_scene_diff.is_diff = True
        planning_options.planning_scene_diff.robot_state.is_diff = True
        goal_msg.planning_options = planning_options

        self.get_logger().info(f"Sending goal to MoveIt with planning group: {request.group_name}")

        # Send the goal asynchronously
        future = self._move_action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        """Called whenever MoveGroup sends intermediate feedback."""
        self.get_logger().info(f"Feedback: {feedback_msg.feedback}")

    def goal_response_callback(self, future):
        """Called once the MoveGroup server has accepted/rejected our goal."""
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error("Goal was rejected by MoveGroup!")
            self.done = True
            return

        self.get_logger().info("Goal accepted; waiting for result...")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        """Called once the MoveGroup action has a final result (success/fail)."""
        result = future.result().result
        if result.error_code.val == 1:
            self.get_logger().info("Motion planning succeeded!")
        else:
            self.get_logger().error(f"Motion planning failed with error code: {result.error_code.val}")

        # Signal that we're completely done
        self.done = True


class ConditionalNode(Node):
    def __init__(self):
        super().__init__('conditional_node')
        self.get_logger().info("Conditional node launched. Press 'x' to plan, anything else to skip...")

    def run(self):
        # Wait for user input (blocking)
        key = input("Press 'x' to run motion planning action, or any other key to do nothing: ")
        if key.lower() == 'x':
            self.get_logger().info("Key 'x' pressed -> sending motion plan goal.")
            mg_client = MoveGroupActionClient()
            mg_client.send_goal()

            # Spin “manually” until mg_client.done is True
            while rclpy.ok() and not mg_client.done:
                rclpy.spin_once(mg_client, timeout_sec=0.1)

            mg_client.destroy_node()
        else:
            self.get_logger().info("Key not recognized -> no motion plan.")


def main(args=None):
    rclpy.init(args=args)
    node = ConditionalNode()
    node.run()
    # Clean up
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

















# import rclpy
# from rclpy.node import Node
# from rclpy.action import ActionClient

# # Standard ROS messages
# from geometry_msgs.msg import PoseStamped, Pose
# from shape_msgs.msg import SolidPrimitive
# # MoveIt messages
# from moveit_msgs.msg import Constraints, PositionConstraint, OrientationConstraint
# from moveit_msgs.msg import MotionPlanRequest, PlanningOptions
# from moveit_msgs.action import MoveGroup
# from moveit_msgs.action import ExecuteTrajectory

# class PoseGoalHelper:
#     @staticmethod
#     def make_pose_goal_constraints(link_name, pose_stamped, pos_tolerance=0.01, ori_tolerance=0.01):
#         """
#         Creates a Constraints object with a small bounding region for position
#         and orientation tolerances around 'pose_stamped'.
#         """
#         c = Constraints()

#         # PositionConstraint with a small sphere
#         pc = PositionConstraint()
#         pc.header = pose_stamped.header
#         pc.link_name = link_name
#         pc.weight = 1.0

#         # The bounding region around the desired point in "world" frame
#         sphere = SolidPrimitive()
#         sphere.type = SolidPrimitive.SPHERE
#         # A radius of pos_tolerance
#         sphere.dimensions = [pos_tolerance]

#         # Pose of that sphere center = the desired end-effector position
#         sphere_pose = Pose()
#         sphere_pose.position = pose_stamped.pose.position
#         # Keep orientation at identity for the region
#         sphere_pose.orientation.w = 1.0

#         pc.constraint_region.primitives.append(sphere)
#         pc.constraint_region.primitive_poses.append(sphere_pose)

#         # OrientationConstraint
#         oc = OrientationConstraint()
#         oc.header = pose_stamped.header
#         oc.link_name = link_name
#         oc.orientation = pose_stamped.pose.orientation
#         oc.absolute_x_axis_tolerance = ori_tolerance
#         oc.absolute_y_axis_tolerance = ori_tolerance
#         oc.absolute_z_axis_tolerance = ori_tolerance
#         oc.weight = 1.0

#         c.position_constraints.append(pc)
#         c.orientation_constraints.append(oc)
#         return c

# class MoveGroupActionClient(Node):
#     def __init__(self):
#         super().__init__('pose_goal_client')
#         self._move_action_client = ActionClient(self, MoveGroup, '/move_action')
#         self._execute_action_client = ActionClient(self, ExecuteTrajectory, '/execute_trajectory')
#         self.done = False

#     def send_goal(self):
#         # Wait for servers
#         self.get_logger().info("Waiting for /move_action server...")
#         self._move_action_client.wait_for_server()
#         self.get_logger().info("Waiting for /execute_trajectory server...")
#         self._execute_action_client.wait_for_server()

#         # Build the MoveGroup goal
#         goal_msg = MoveGroup.Goal()
#         request = MotionPlanRequest()
#         request.group_name = "ur_manipulator"

#         # Pose we want
#         pose_goal = PoseStamped()
#         pose_goal.header.frame_id = "world"
#         pose_goal.pose.position.x = 1.142
#         pose_goal.pose.position.y = 0.283
#         pose_goal.pose.position.z = 1.618
#         pose_goal.pose.orientation.x = -0.021
#         pose_goal.pose.orientation.y =  0.998
#         pose_goal.pose.orientation.z =  0.056
#         pose_goal.pose.orientation.w =  0.009

#         # Convert that pose into a constraint
#         # Tolerances are in meters/radians
#         constraints = PoseGoalHelper.make_pose_goal_constraints(
#             link_name="wrist_3_link",  # or "tool0", etc.
#             pose_stamped=pose_goal,
#             pos_tolerance=0.01,        # 1cm
#             ori_tolerance=0.1          # ~5.7 degrees
#         )
#         request.goal_constraints.append(constraints)

#         # Allow more planning time
#         request.allowed_planning_time = 5.0

#         # Minimal planning options
#         planning_options = PlanningOptions()
#         planning_options.planning_scene_diff.is_diff = True
#         planning_options.planning_scene_diff.robot_state.is_diff = True

#         goal_msg.request = request
#         goal_msg.planning_options = planning_options

#         self.get_logger().info("Sending MoveGroup goal with a PoseConstraint")
#         future = self._move_action_client.send_goal_async(
#             goal_msg,
#             feedback_callback=self.feedback_callback
#         )
#         future.add_done_callback(self.goal_response_callback)

#     def feedback_callback(self, feedback):
#         self.get_logger().info(f"Feedback: {feedback.feedback}")

#     def goal_response_callback(self, future):
#         goal_handle = future.result()
#         if not goal_handle.accepted:
#             self.get_logger().error("Goal was rejected!")
#             self.done = True
#             return
#         self.get_logger().info("Goal accepted, waiting for result...")
#         result_future = goal_handle.get_result_async()
#         result_future.add_done_callback(self.get_result_callback)

#     def get_result_callback(self, future):
#         result = future.result().result
#         if result.error_code.val == 1:
#             self.get_logger().info("Motion planning succeeded and executed!")
#         else:
#             self.get_logger().error(f"Motion failed with error code: {result.error_code.val}")
#         self.done = True

# class ConditionalNode(Node):
#     def __init__(self):
#         super().__init__('conditional_node')
#         self.get_logger().info("Press 'x' to plan, anything else to skip...")

#     def run(self):
#         key = input("Press 'x' for motion plan: ")
#         if key.lower() == 'x':
#             mg_client = MoveGroupActionClient()
#             mg_client.send_goal()
#             while rclpy.ok() and not mg_client.done:
#                 rclpy.spin_once(mg_client, timeout_sec=0.1)
#             mg_client.destroy_node()
#         else:
#             self.get_logger().info("Skipping motion plan")

# def main(args=None):
#     rclpy.init(args=args)
#     node = ConditionalNode()
#     node.run()
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

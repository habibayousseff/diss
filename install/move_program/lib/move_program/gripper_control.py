#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import Float64
from control_msgs.action import GripperCommand

class GripperController(Node):
    def __init__(self):
        super().__init__('gripper_controller')
        
        # Direct position publisher (matches forward_command_controller)
        self.position_pub = self.create_publisher(
            Float64,
            '/gripper_controller/commands',
            10
        )
        
        # Action client (alternative approach)
        self.action_client = ActionClient(
            self,
            GripperCommand,
            '/gripper_controller/gripper_action'
        )
        
        self.get_logger().info("Gripper controller ready")

    def simple_move(self, position):
        """Direct position command (0.0=closed, 0.038=open)"""
        position = max(0.0, min(0.038, position))
        msg = Float64()
        msg.data = position
        self.position_pub.publish(msg)
        self.get_logger().info(f"Commanded position: {position}")

    async def action_move(self, position):
        """Action-based movement (similar to UR5 control)"""
        goal_msg = GripperCommand.Goal()
        goal_msg.command.position = position
        goal_msg.command.max_effort = 5.0
        
        self.action_client.wait_for_server()
        future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    controller = GripperController()
    
    try:
        while rclpy.ok():
            print("\nGripper Control:")
            print("1. Open gripper (0.038)")
            print("2. Close gripper (0.0)")
            print("3. Custom position")
            print("4. Exit")
            
            choice = input("Choose (1-4): ")
            
            if choice == '1':
                controller.simple_move(0.038)
            elif choice == '2':
                controller.simple_move(0.0)
            elif choice == '3':
                pos = float(input("Position (0.0-0.038): "))
                controller.simple_move(pos)
            elif choice == '4':
                break
            
            rclpy.spin_once(controller, timeout_sec=0.1)
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

def control_gripper(parent_node, position: float):
    """Helper function for integration with UR5 navigation"""
    node = GripperController()
    node.simple_move(position)
    
    # Simple blocking wait (no feedback handling)
    start_time = node.get_clock().now()
    while (node.get_clock().now() - start_time).nanoseconds < 2e9:  # 2 sec timeout
        rclpy.spin_once(node, timeout_sec=0.1)
    
    node.destroy_node()
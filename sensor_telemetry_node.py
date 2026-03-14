#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class UgvDiagnosticsNode(Node):

    def __init__(self):
        super().__init__("ugv_diagnostic_node")
        self.uptime_counter_ = 0
        self.get_logger().info("UGV Edge-Compute Diagnostics Initialized.")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # self.get_logger().info("Hello")
        self.get_logger().info("System health check sequence: " + str(self.uptime_counter_))
        self.uptime_counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = UgvDiagnosticsNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()




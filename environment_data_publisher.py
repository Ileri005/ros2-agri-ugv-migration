#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class AgriTelemetryPublisher(Node):
    def __init__(self):
        super().__init__("agri_telemetry_publisher")
        self.sensor_array_name = "UGV_Sensor_Array_Alpha"

        # Creating a publisher
        self.publisher_ = self.create_publisher(String, "enivronmental_telemetry", 10)
        self.timer_ = self.create_timer(0.5, self.publish_telemetry)
        self.get_logger().info("Robot News Station has been started.")

    def publish_telemetry(self):
        msg = String()
        # Simulating foundational telemetry before LiDAR integration
        msg.data = "Telemetry Active:  " + self.sensor_array_name + "checking hardware connections."
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = AgriTelemetryPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
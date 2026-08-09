import json
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from industrial_am_interfaces.msg import MeltpoolTelemetry

class AdvancedEdgeController(Node):
    def __init__(self):
        super().__init__('advanced_edge_controller')
        
        # Subscribe to custom structured message types
        self.telemetry_sub = self.create_subscription(
            MeltpoolTelemetry,
            '/sensor_optical_coherence_node',
            self.process_structured_feedback,
            10
        )
        self.laser_pub = self.create_publisher(Float32, '/motor_actuator_driver_node/laser_power', 10)

    def process_structured_feedback(self, msg):
        """Uses structural telemetry fields to handle real-time override logic."""
        if msg.porosity_index > 0.35:
            override_power = Float32()
            override_power.data = 280.0 # Boost laser energy level
            self.laser_pub.publish(override_power)
            self.get_logger().warn(f"Anomaly detected at frame {msg.frame_id}. Triggering real-time override.")

def main(args=None):
    rclpy.init(args=args)
    node = AdvancedEdgeController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

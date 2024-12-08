import rclpy
from rclpy.node import Node

class ManipulatorNode(Node):
    def __init__(self):
        super().__init__('manipulator_node')
        self.get_logger().info('Manipulator Node started')

def main(args=None):
    rclpy.init(args=args)
    node = ManipulatorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

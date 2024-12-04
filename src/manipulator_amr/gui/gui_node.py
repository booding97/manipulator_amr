import rclpy
from rclpy.node import Node

class GUINode(Node):
    def __init__(self):
        super().__init__('gui_node')
        self.get_logger().info('GUI Node started')

def main(args=None):
    rclpy.init(args=args)
    node = GUINode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

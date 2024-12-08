import rclpy
from rclpy.node import Node

class AMRNode(Node):
    def __init__(self):
        super().__init__('amr_node')
        self.get_logger().info('AMR Node started')

def main(args=None):
    rclpy.init(args=args)
    node = AMRNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

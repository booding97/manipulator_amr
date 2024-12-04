import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import threading

class ServerNode(Node):
    def __init__(self):
        super().__init__('server_node')
        self.get_logger().info('Server Node started')

class ConveyorController(Node):
    def __init__(self):
        super().__init__('conveyor_controller')
        self.subscription = self.create_subscription(
            String,
            'conveyor_test',
            self.listener_callback,
            10
        )
        self.serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # 시리얼 포트 설정
        self.get_logger().info(f"Serial port opened: {self.serial_port.name}")  # Should print the serial port name
        self.get_logger().info('Conveyor Controller Node Started')

    def listener_callback(self, msg):
        command = msg.data.strip()  # 토픽에서 문자열 데이터 가져오기 및 공백 제거
        self.get_logger().info(f"Received command: {command}")
        if command == "Conveyor Start":
            self.send_serial_command(755)  # Send "START" to Arduino
        elif command == "Conveyor Stop":
            self.send_serial_command(0)  # Send "STOP" to Arduino
        else:
            self.get_logger().warn(f"Unknown command received: {command}")

    def send_serial_command(self, command):
        try:
            command_str = f"{command}\n"  # 명령 뒤에 종료 문자 추가
            self.serial_port.write(command_str.encode())
            self.get_logger().info(f"Sent command to Arduino: {command_str.strip()}")
        except Exception as e:
            self.get_logger().error(f"Failed to send command: {str(e)}")

def main(args=None):
    rclpy.init(args=args)

    # Create nodes
    server_node = ServerNode()
    conveyor_controller_node = ConveyorController()

    # Create a MultiThreadedExecutor
    executor = rclpy.executors.MultiThreadedExecutor()

    # Add nodes to the executor
    executor.add_node(server_node)
    executor.add_node(conveyor_controller_node)

    try:
        # Run the executor (this will handle both nodes concurrently)
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up when done
        server_node.destroy_node()
        conveyor_controller_node.destroy_node()
        conveyor_controller_node.serial_port.close()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

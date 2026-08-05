import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(
            String, '/chatter', self.on_msg, 10)
        self.get_logger().info('Listener ready — waiting for messages…')

    def on_msg(self, msg):
        self.get_logger().info(f'Heard: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(Listener())
    rclpy.shutdown()
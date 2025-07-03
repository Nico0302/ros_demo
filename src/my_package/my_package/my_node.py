import rclpy
from rclpy.node import Node
from my_cpp_package.msg import TestMsg


class MyNode(Node):
    def __init__(self):
        super().__init__("my_node")

        self.test_publisher_ = self.create_publisher(TestMsg, "test", 10)


def main():
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

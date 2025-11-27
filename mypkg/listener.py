import rclpy #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person


rclpy.init()
node = Node("listener")

def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)

def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)

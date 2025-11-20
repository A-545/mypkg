import rclpy #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数

rclpy.init()
node = Node("listener")

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

def main():
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)

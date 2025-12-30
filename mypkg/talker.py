import rclpy #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型

class Talker():
    def __init__(self): 
        self.pub = node.create_publisher(Int16, "countup", 10) 
        self.n = 0 #カウント用変数

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
talker = Talker()

def cb():          #20行目で定期実行されるコールバック関数
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = talker.n
    talker.pub.publish(msg)        #pubの持つpublishでメッセージ送信
    talker.n += 1

node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）

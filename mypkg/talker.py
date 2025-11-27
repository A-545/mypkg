import rclpy #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person #変更

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10) #変更
n = 0 #カウント用変数


def cb():          #20行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Person()         #送信するデータの型を変更
    msg.name = "大島康太朗"
    msg.age = n
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1


def main():
    node.create_timer(0.5, cb)  #タイマー設定
    rclpy.spin(node)            #実行（無限ループ）

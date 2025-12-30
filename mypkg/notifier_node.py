#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kotaro Oshima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PomodoroNotifier(Node):
    def __init__(self):
        super().__init__('pomodoro_notifier')
        # timer_nodeのトピックを購読
        self.subscription = self.create_subscription(
            String,
            '/pomodoro_timer/state',
            self.listener_callback,
            10)
        self.last_state = "IDLE"

    def listener_callback(self, msg):
        current_state = msg.data
        
        # 状態が変わった瞬間だけメッセージを表示
        if current_state != self.last_state:
            if current_state == "FOCUS":
                self.get_logger().info("Work Time. Focus for 25 mins.")
            elif current_state == "BREAK":
                self.get_logger().warn("Time for a break. Rest for 5 mins.")
            
            self.last_state = current_state

def main():
    rclpy.init()
    node = PomodoroNotifier()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

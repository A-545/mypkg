#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kotaro Oshima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class PomodoroTimer(Node):
    def __init__(self):
        super().__init__('pomodoro_timer')

        # パラメータ
        self.focus_duration = self.declare_parameter('focus_mins', 25).value * 60
        self.break_duration = self.declare_parameter('break_mins', 5).value * 60

        self.state = "FOCUS"
        self.time_left = self.focus_duration

        self.state_pub = self.create_publisher(String, '~/state', 10)
        self.time_pub = self.create_publisher(Int32, '~/time_remaining', 10)

        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.state_pub.publish(String(data=self.state))

        if self.time_left > 0:
            self.time_left -= 1
        else:
            if self.state == "FOCUS":
                self.state = "BREAK"
                self.time_left = self.break_duration
            else:
                self.state = "FOCUS"
                self.time_left = self.focus_duration

        self.time_pub.publish(Int32(data=self.time_left))

def main(args=None):
    rclpy.init(args=args)
    node = PomodoroTimer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Kotaro Oshima
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    timer = launch_ros.actions.Node(
        package='mypkg',          
        executable='timer_node', 
        output='screen'
    )

    notifier = launch_ros.actions.Node(
        package='mypkg',
        executable='notifier_node',
        output='screen'
    )

    return launch.LaunchDescription([timer, notifier])


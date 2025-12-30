#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kotaro Oshima
# SPDX-License-Identifier: BSD-3-Clause

source /opt/ros/humble/setup.bash
dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1

colcon build || exit 1
source install/setup.bash

res=0
fail () {
    res=1
}

# launch 起動
ros2 launch mypkg timer_notifier.launch.py &
LAUNCH_PID=$!

sleep 5

# /pomodoro_timer/state を5秒待って受信
state=$(timeout 5 ros2 topic echo /pomodoro_timer/state --once)

if [ $? -ne 0 ]; then
    echo "Error: /pomodoro_timer/state did not respond"
    fail
else
    echo "Received state:"
    echo "$state"
    echo "$state" | grep -q "data:" || echo "$state" | grep -Eq "^[0-9]+$" >/dev/null 2>&1 || fail
fi

# launch プロセス終了
kill $LAUNCH_PID 2>/dev/null

# 結果判定
if [ "$res" -eq 0 ]; then
    echo "OK"
else
    exit 1
fi


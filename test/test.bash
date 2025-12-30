#!/bin/bash 
# SPDX-FileCopyrightText: 2025 Kotaro Oshima
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1

colcon build || exit 1
source install/setup.bash

res=0
fail () {
    res=1
}

ros2 launch mypkg timer_notifier.launch.py &
LAUNCH_PID=$!

sleep 5

# /pomodoro_timer/state を5秒待って受信
state=$(timeout 5 ros2 topic echo /pomodoro_timer/state --once)
if [ $? -ne 0 ]; then
    echo "Error: /pomodoro_timer/state did not respond"
    fail
fi

echo "state:"
echo "$state"

# FOCUS を含むか確認
echo "$state" | grep "data: FOCUS" >/dev/null 2>&1 || fail

# /pomodoro_timer/time_remaining を5秒待って受信
time_left=$(timeout 5 ros2 topic echo /pomodoro_timer/time_remaining --once)
if [ $? -ne 0 ]; then
    echo "Error: /pomodoro_timer/time_remaining did not respond"
    fail
fi

echo "time_remaining:"
echo "$time_left"

# data: が含まれているか確認
echo "$time_left" | grep "data:" >/dev/null 2>&1 || fail

# launch プロセスを終了
kill $LAUNCH_PID 2>/dev/null

# 結果判定
if [ "$res" -eq 0 ]; then
    echo "OK"
else
    exit 1
fi

exit $res


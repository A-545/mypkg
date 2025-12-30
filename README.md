# mypkg - Pomodoro Timer ROS2 Package

## 概要
ROS2 上で動作するポモドーロタイマーです。  

## クローン方法
```
$git clone https://github.com/A-545/mypkg ~/ros2_ws/src/mypkg
$cd mypkg
```

## 実行例
```
$cd ~/ros2_ws
$colcon build
$source install/setup.bash
# ノードを起動
$ros2 launch mypkg timer_notifier.launch.py
[notifier_node-2] [INFO] [1767123089.467671444] [pomodoro_notifier]: Work Time. Focus for 25 mins.
[notifier_node-2] [INFO] [1767123089.468561270] [pomodoro_notifier]: Time left: 24:59
[notifier_node-2] [INFO] [1767123090.445315854] [pomodoro_notifier]: Time left: 24:58
[notifier_node-2] [INFO] [1767123091.443460805] [pomodoro_notifier]: Time left: 24:57
[notifier_node-2] [INFO] [1767123092.440687042] [pomodoro_notifier]: Time left: 24:56
[notifier_node-2] [INFO] [1767123093.439053978] [pomodoro_notifier]: Time left: 24:55
```

## 動作環境
### ソフトウェア
- Python
    - 3.7 ~ 3.10 テスト済み
### テスト環境
- Ubuntu 24.04.3 動作確認済み

## 備考
このリポジトリは大学講義（robosys2025）の課題として作成されたものです。

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Kotaro Oshima


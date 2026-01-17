# mypkg - Pomodoro Timer ROS2 Package
[![test](https://github.com/A-545/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/A-545/mypkg/actions/workflows/test.yml)

## 概要
ROS2 上で動作するポモドーロタイマーです。  

25分間カウントした後、5分の休憩時間がありその後カウントを繰り返します。

## ノード一覧
### **timer_node.py**（ノード名：`/pomodoro_timer`）
- ポモドーロタイマーのメインノード  
- 作業時間（25分）と休憩時間（5分）をカウントし、状態を管理  
- 1秒ごとにカウントダウンを実行し、残り時間が 0 になると FOCUS↔BREAK を切り替える  
- 現在状態と残り時間をトピックとして配信する  

---

### **notifier_node.py**（ノード名：`/pomodoro_notifier`）
- `timer_node.py`（`/pomodoro_timer`）のトピックを購読して動作  
- 状態が変わった瞬間に INFO/WARN でメッセージを表示  
- 残り時間を mm:ss 形式でログに出力する通知ノード  

---
## トピック一覧  
### **/pomodoro_timer/state**
- **型：** `std_msgs/msg/String`  
- **配信元：** `/pomodoro_timer`  
- **購読者：** `/pomodoro_notifier`  
- **内容：**  
  - `"FOCUS"`（作業時間）  
  - `"BREAK"`（休憩時間）  

---

### **/pomodoro_timer/time_remaining**
- **型：** `std_msgs/msg/Int32`  
- **配信元：** `/pomodoro_timer`  
- **購読者：** `/pomodoro_notifier`  
- **内容：** 残り時間（秒）を整数値で通知  

---

### その他のシステムトピック
**/parameter_events** ノードのパラメータ変更通知（標準） 
**/rosout** ログ出力（標準） 

---

## クローン方法
```
$git clone https://github.com/A-545/mypkg ~/ros2_ws/src/mypkg
```

## 実行例
```
# 任意の場所でクローンした ROS2 ワークスペースへ移動
$ cd <your_ros2_ws>/src
$ colcon build
$ source install/setup.bash
# ノードを起動
$ ros2 launch mypkg timer_notifier.launch.py
[notifier_node-2] [INFO] [1767123089.467671444] [pomodoro_notifier]: Work Time. Focus for 25 mins.
[notifier_node-2] [INFO] [1767123089.468561270] [pomodoro_notifier]: Time left: 24:59
[notifier_node-2] [INFO] [1767123090.445315854] [pomodoro_notifier]: Time left: 24:58
[notifier_node-2] [INFO] [1767123091.443460805] [pomodoro_notifier]: Time left: 24:57
[notifier_node-2] [INFO] [1767123092.440687042] [pomodoro_notifier]: Time left: 24:56
[notifier_node-2] [INFO] [1767123093.439053978] [pomodoro_notifier]: Time left: 24:55
...
[notifier_node-2] [WARN] [pomodoro_notifier]: Time for a break. Rest for 5 mins.
```

## 動作環境
### ソフトウェア
- Python 3.13.5テスト済み
### テスト環境
- Ubuntu 24.04.3 動作確認済み

## 備考
このリポジトリはロボットシステム学の課題として作成されたものです。

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Kotaro Oshima


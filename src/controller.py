# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> main
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-02 14:47
    @Desc   :主控制函数
            负责启动雷达扫描，运动目标识别
-------------------------------------------------
   Change Activity:
                   2022-03-02 14:47:
-------------------------------------------------
"""
__author__ = 'bobi'

import queue

from pynput import keyboard

from src.Method import *


class controller:

    def __init__(self):
        self.flag = [True]
        self.MaxL = 99999999999
        # 雷达扫描数据队列
        self.dataQueue = queue.Queue(maxsize=self.MaxL)
        self.objectQueue = queue.Queue(maxsize=200)

    # 启动线程
    def startThread(self):
        scanning(dataQueue=self.dataQueue, flag=self.flag)
        clustering(dataQueue=self.dataQueue, flag=self.flag, objectQueue=self.objectQueue)

    # 退出监听程序
    def on_press(self, key):
        # 按下按键时执行。
        try:
            print('alphanumeric key {0} pressed , stop scanning'.format(
                key.char))
            self.flag[0] = False
        except AttributeError:
            print('special key {0} pressed '.format(
                key))

        # 通过属性判断按键类型。


if __name__ == '__main__':
    # 控制台
    controller = controller()
    controller.startThread()
    # Collect events until released
    with keyboard.Listener(
            on_press=controller.on_press) as listener:
        # listener.setDaemon(True)
        listener.join()
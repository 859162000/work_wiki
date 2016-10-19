#! $PATH/python

# file name: tuopan_logic.py
# author: lianghy
# time: 2016-6-21 15:29:58

import re
import logging


"""
类似硬件的时钟同步机制，进行仿真。每个模块都有全局虚拟控制时钟。
update 更新。function计算。
每个模块延时为一个周期。
gvclk 全局虚拟时钟
在时钟为低时，模块进行功能运算；
在时钟为高时，模块更新状态（将结果输出）。
数值的大小用int来表示。
控制过程：
c0 s d
循环1：
c0 s1 d1 -> 判断是否有效
有效或无明显变化：以c0为基础，进行扰动，得到c1
    c1 s2 d2 -> 判断是否效果是否更好或更差
    更好：以c1为基础
    更差：以c0为基础
    无明显差别：扩展c0 c1
    返回循环1
效果更差：则反转c0
    返回循环1

todo：
    模仿
"""

class C:
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {}
        self.pout = {}
        return
    def _parameter(self):
        return
    def update(self):
        return
    def function(self):
        return

class Ccontrol:
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {}
        self.pout = {}
        return
    def _parameter(self):
        return
    def update(self):
        return
    def function(self):
        return

class Crecord:
    """ (strength, target_distance) <==> (s,Dd) """
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {}
        self.pout = {}
        return
    def _parameter(self):
        self._waitResult = 0
        return
    def update(self):
        self.pout["mapping"] = self.mapping
        return
    def function(self):
        # add push strength and result
        if (self.pin["push_strength"]!=0):
            self.mapping.append([self.pin["push_strength"],0])
            self._waitResult = 1
        if (self._waitResult):
            if (self.pin["target_distance"]!=0):
                self.mapping[-1][1] = self.pin["target_distance"]
            elif (self.pin["push"]):
                self._waitResult = 0
        return

class Caction:
    """
    三个输入：
    推 push
    增加力量 0，减小力量 1 changeStrength
    值 strength
    """
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {"push":0,"changeStrength":0,"strength":0}
        self.pout = {"push_strength":""}
        return
    def _parameter(self):
        self.lstrength = "1"
        self._push_strength = 0
        return
    def update(self):
        self.pout["push_strength"] = self._push_strength
        return
    def function(self):
        if (self.pin["push"]):
            self._push_strength = self.lstrength
        else:
            self._push_strength = 0
        if (self.pin["changeStrength"]):
            self.lstrength += self.pin["strength"]
        else:
            self.lstrength -= self.pin["strength"]
        return

class Cresponse:
    def __init__(self):
        self._port()
        self._parameter()
        return
    def _port(self):
        self.pin = {}
        self.pout = {}
        return
    def _parameter(self):
        return
    def update(self):
        self.pout = self._pout
        return
    def function(self):
        self._pout = self.pin
        return

class Cinspire:
    def __init__(self):
        self._port()
        self._parameter()
        return
    def _port(self):
        self.pin = {"push":0,"target_distance":0}
        self.pout = {}
        return
    def _parameter(self):
        return
    def update(self):
        self.pout = self._pout
        return
    def function(self):
        self._pout = self.pin
        return

class tuopan:
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {}
        self.pout = {}
        return
    def update(self):
        return
    def _parameter(self):
        return

if __name__=="__main__":
    print("Hi")

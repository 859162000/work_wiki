#! $PATH/python

# file name: follower.py
# author: lianghy
# time: 2016-10-13 16:19:04

"""顶层模块"""

import dyVerilog as dv
import receptor
class follower(dv.module):
    def __init__(self):
        dv.module.__init__()
        self.key_in = self.receptor.key_in
    def _define(self):
        self.receptor = receptor.receptor()
        pass
    def _func(num):
        try:
            for x in range(num):
                for y in self.subModule():
                    y()
                for y in self.subNet():
                    y()
        except Exception as exc:
            raise(exc)
    def subModule(self):
        return([self.receptor])
    def subNet(self):
        return([])

top = follower()

if __name__=="__main__":
    print("follower.py")

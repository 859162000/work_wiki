#! $PATH/python

# file name: leftright.py
# author: lianghy
# time: 2016-6-29 14:02:14

"""功能：建立映射
单元有两个动作：左、右。
根据指令，可以执行相应动作。
指令L，对应动作左
指令R，对应动作右
"""

class C:
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
        return
    def function(self):
        return

class Clink:
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
        return
    def function(self):
        """命令激发，
        每个新命令生成一条新的记录，不停记录接下来的动作和结果。"""
        if (self.pin['command']):
            pass
        return

class Caction:
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        self.pin = {'command':'', 'commandList':[], 'resultList':[]}
        self.pout = {'action':''}
        return
    def _parameter(self):
        return
    def update(self):
        return
    def function(self):
        return

class CcommandIn:
    """当输入命令由空变为有效时，认为接收到命令。
    当输入命令由有效到空时，认为命令结束，输出命令。
    """
    def __init__(self):
        self._port()
        self._parameter()
        return
    def _port(self):
        self.pin = {'command':''}
        self.pout = {'command':''}
        return
    def _parameter(self):
        self._state = 0
        self._command = ''
        return
    def update(self):
        if (not self._state):
            self.pout['command'] = self._command
            self._command = ''
        return
    def function(self):
        if (not self._state and self.pin['command']!=''):
            self._state = 1
            self._command = self.pin['command']
        elif (self._state and self.pin['command']==''):
            self._state = 0
        return

class CleftRight:
    def __init__(self):
        self._port()
        self._parameter()
        pass
    def _port(self):
        """command=''/L/R, result=''/'y'/'n', action=''/'left'/'right' """
        self.pin = {'command':'','result':''}
        self.pout = {'action':''}
        return
    def _parameter(self):
        return
    def update(self):
        return
    def function(self):
        return

if __name__=="__main__":
    print("Hi")

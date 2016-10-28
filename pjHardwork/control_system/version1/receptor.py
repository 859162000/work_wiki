#! $PATH/python

# file name: receptor.py
# author: lianghy
# time: 2016-10-11 17:27:28

import os
import sys
home = os.environ['HOME']
sys.path.append(os.path.join(home,'work_wiki','pjHardwork','dyVerilog'))
import dyVerilog as dv

class digitalBus(dv.module):
    def __init__(self, width,input_count):
        dv.module.__init__(self)
        self.port_in = []
        for x in range(input_count):
            self.port_in.append(dv.port(width,'input'))
        self.port_out = dv.port(width,'output')
    def _func(self):
        for x in self.port_in:
            self.port_out.set_value(
            bin(int(self.port_out._value,2)|int(x._value,2)))

#TODO:
class receptor(dv.module):
    def __init__(self):
        dv.module.__init__(self)
        self.key_in = self.digital_bus.port_in[0]
        self.feedback_in = self.digital_bus.port_in[1]
        self.accumulate_value = self.digital_bus.port_out
    def _define(self):
        self.digital_bus = digitalBus(8,2)
        pass
    def _func(self):
        pass
    def _module(self):
        self.digital_bus()
        print(self.digital_bus.port_out._value)
        pass

class testbench(dv.testbench):
    def __init__(self):
        self.top = receptor()
    pass

def simu():
    testbench().interactive()


if __name__=="__main__":
    simu()
    print("receptor.py")

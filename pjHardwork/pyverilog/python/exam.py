#! $PATH/python

# file name: exam.py
# author: lianghy
# time: 2016/7/19 21:53:34

#import dyDebug
import dyVerilog as dv

class adder(dv.module):
    def __init__(self,parrent='',name=''):
        dv.module.__init__(self,parrent,name)
        self.adder1 = dv.port(self,'in1',4,'input')
        self.adder2 = dv.port(self,'in2',4,'input')
        self.result = dv.port(self,'out',4,'output')
        self._zero = { }
        self._table = { 
            '0b0001':{'0b0001':'0b0010','0b0010':'0b0011','0b0011':'0b0100',
                '0b0100':'0b0101','0b0101':'0b0110','0b0110':'0b0111',
                '0b0111':'0b1000','0b1000':'0b1001','0b1001':'0b1010'},
            '0b0010':{'0b0001':'0b0011','0b0010':'0b0100','0b0011':'0b0101',
                '0b0100':'0b0110','0b0101':'0b0111','0b0110':'0b1000',
                '0b0111':'0b1001','0b1000':'0b1010','0b1001':'0b1011'},
            '0b0011':{'0b0001':'0b0100','0b0010':'0b0101','0b0011':'0b0110',
                '0b0100':'0b0111','0b0101':'0b1000','0b0110':'0b1001',
                '0b0111':'0b1010','0b1000':'0b1011','0b1001':'0b1100'},
            '0b0100':{'0b0001':'0b0101','0b0010':'0b0110','0b0011':'0b0111',
                '0b0100':'0b1000','0b0101':'0b1001','0b0110':'0b1010',
                '0b0111':'0b1011','0b1000':'0b1100','0b1001':'0b1101'},
            '0b0101':{'0b0001':'0b0110','0b0010':'0b0111','0b0011':'0b1000',
                '0b0100':'0b1001','0b0101':'0b1010','0b0110':'0b1011',
                '0b0111':'0b1100','0b1000':'0b1101','0b1001':'0b1110'},
            '0b0110':{'0b0001':'0b0111','0b0010':'0b1000','0b0011':'0b1001',
                '0b0100':'0b1010','0b0101':'0b1011','0b0110':'0b1100',
                '0b0111':'0b1101','0b1000':'0b1110','0b1001':'0b1111'},
            '0b0111':{'0b0001':'0b1000','0b0010':'0b1001','0b0011':'0b1010',
                '0b0100':'0b1011','0b0101':'0b1100','0b0110':'0b1101',
                '0b0111':'0b1110','0b1000':'0b1111','0b1001':16},
            '0b1000':{'0b0001':'0b1001','0b0010':'0b1010','0b0011':'0b1011',
                '0b0100':'0b1100','0b0101':'0b1110','0b0110':'0b1110',
                '0b0111':'0b1111','0b1000':16,'0b1001':17}
                }
    def __call__(self):
        # 1 输入Pin连接到内部信号
        # 2 功能定义
        # 3 输出Pin连接到内部信号
        pin_adder1 = self.adder1.get_value()
        pin_adder2 = self.adder2.get_value()
        if (int(pin_adder2,2) and int(pin_addr1,2)):
            pou_result = self._table[pin_adder1][pin_adder2]
        else:
            if int(pin_adder2,2):
                pou_result = pin_adder1
            else:
                pou_result = pin_adder2
        self.result.set_value(pou_result)

class testbench(dv.testbench):
    def __init__(self):
        dv.testbench.__init__(self)
    def define(self):
        self.a = dv.port(self,'a',4,"output")
        self.b = dv.port(self,'b',4,"output")
        self.c = dv.port(self,'c',4,"input")
        ladder = adder(self,'adder')
        self._module.append(ladder)
        self._net.append(dv.net(self,'neta',self.a,[ladder.adder1]))
        self._net.append(dv.net(self,'netb',self.b,[ladder.adder2]))
        self._net.append(dv.net(self,'netc',ladder.result,[self.c]))
    def test(self):
        self.run(10)
        print(self.c.get_value())
        self.a.set_value(3)
        self.b.set_value(3)
        print(self.c.get_value())
        self.run(1)
        print(self.c.get_value())

def test():
    tb = testbench()
    tb.define()
    tb.test()

if __name__=="__main__":
    print("Hi嗨")
    test()

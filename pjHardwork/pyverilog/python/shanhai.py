#! $PATH/python

# file name: regfile.py
# author: lianghy
# time: 2016/7/4 21:08:27

import logging

"""pin 定义和引用。定义后，不可更改，保存在__pin中。在连接后，pin指向reg对象。"""
class Cmodule:
    """redine functions : pin_in, pin_ou, function
       pin = {'a':'value'/link,}"""
    def __init__(self,pin,pou,**key):
        #self.pin = [('adder1',4),('adder2',4)]
        #self.pou = [('result',4)]
        logging.info("build module: %s", self.__name__)
        self.__pin = self.pin
        self.__pou = self.pou
        self.check_connection(pin,pou)
        return
    def check_connection(self):
        if (len(self.__pin)>0):
            if (len(pin)>0):
                for x in self.__pin:
                    try:
                        tpin_name = x['name']
                        tcon_value = self._pin[tpin_name]
                        x['value'] = tcon_value
                        tpin_width = len(x['width'])
                        tcon_width = len(tcon_value)
                        if (tcon_width > tpin_width):
                            logging.error("Width mismatch: net %s is %s, pin %s is
                                    %s .",)
                    except KeyError:
                        logging.warning("pin %s is floating.",x['name'])
            else:
                logging.warning("input pins are floating.")
        elif (len(pin)>0):
            logging.error("No input pin to connected.")
            exit(0)
        if (len(self.pou_list)>0):
            for x in self.pou_list:
                try:
                except KeyError:
                    logging.warning("pin %s is floating.",x['name'])
        return
    def update(self):
        self.pout['value'] = self._output
        return
    def function(self):
        self.a = {'width':4, 'connect':[{'name':'x','bit':[2,1]}]}
        try:
            pass
        except KeyError as e:
            print("Error: input pin is changed by other class. pin: "+e)
            exit(0)
        return

class Cdecoder:
    def __init__(self,pin,pout,**key):
        self.pin = pin
        self.pout = pout
        return
    def update(self):
        self.pout['value'] = self._output
        return
    def function(self):
        try:
            tcommand = self.pin['command']
            pass
        except KeyError as e:
            print("Error: input pin is changed by other class. pin: "+e)
            exit(0)
        toperator = tcommand[0:DATA_WIDTH]
        tres_addr = tcommand[DATA_WIDTH:(2*DATA_WIDTH)]
        tsource0  = tcommand[(2*DATA_WIDTH):(3*DATA_WIDTH)]
        tsource1  = tcommand[(3*DATA_WIDTH):(4*DATA_WIDTH)]
        if (toperator == 'c0'):
            # 加 next
            self._output['alu_op'] = '1'
            self._output['data_reg_read_addr0'] = tsource0
            self._output['data_reg_read_addr1'] = tsource1
            self._output['data_reg_writ_addr0'] = tres_addr
            self._output['data_reg_writ_addr1'] = tres_addr+1
            self._output['dir_data'] = 0
            self._output['result'] = 'operator'
            self._output['next_ir_addr'] = self.pin['cur_addr']+1
            pass
        return

class Cregfile:
    """function : read, write, 
    pin list : 
        read_addr : 8'b, 0~99. R,output = reg[addr]
        writ_addr : 8'b, 0~99. W,reg[addr] = data
        data : 4x8'b=32'b, 0x0. 
    pout list :
        _output : 8'b, 0~255
    """
    def __init__(self,pin,pout,**key):
        self.pin = pin
        self.pout = pout
        self.__reg = {}
        self._output = ''
        pass
    def update(self):
        self.pout['value'] = self._output
        return
    def function(self):
        try:
            tread_addr = self.pin['read_addr']
            twrit_addr = self.pin['writ_addr']
            tdata = self.pin['data']
        except KeyError as e:
            print("Error: input pin is changed by other class. pin: "+e)
            exit(0)
        self.__reg[twrit_addr] = tdata
        self._output = self.__reg[tread_addr]
        return

class Cadder(Cmodule):
    """out = in1+in2"""
    def __init__(self,pin,pou,**key):
        self.pin = [('adder1',4),('adder2',4)]
        self.pou = [('result',4)]
        Cmodule.__init__(self,pin,pou)
        self.__table = { 
                0:{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9},
                1:{0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10},
                2:{0:2,1:3,2:4,3:5,4:6,5:7,6:8,7:9,8:10,9:11},
                3:{0:3,1:4,2:5,3:6,4:7,5:8,6:9,7:10,8:11,9:12},
                4:{0:4,1:5,2:6,3:7,4:8,5:9,6:10,7:11,8:12,9:13},
                5:{0:5,1:6,2:7,3:8,4:9,5:10,6:11,7:12,8:13,9:14},
                6:{0:6,1:7,2:8,3:9,4:10,5:11,6:12,7:13,8:14,9:15},
                7:{0:7,1:8,2:9,3:10,4:11,5:12,6:13,7:14,8:15,9:16},
                8:{0:8,1:9,2:10,3:11,4:12,5:14,6:14,7:15,8:16,9:17},
                9:{0:9,1:10,2:11,3:12,4:13,5:14,6:15,7:16,8:17,9:18}
                }
        return
    def update(self):
        print("inter value is: ",self._out)
        self.pout['value'] = self._out
    def fucntion(self):
        try:
            tadder1 = self.pin['adder1']
            tadder2 = self.pin['adder2']
            self._out = self.__table[tadder1][tadder2]
        except KeyError as e:
            print("Error: input pin is changed by other class. pin: "+e)
            exit(0)
        return
        
def testbench():
    pin = {}
    pout = {}
    add = Cadder(pin,pout)
    pregIn = {}
    pregOu = {}
    pregfile = Cregfile(pregIn,pregOu)
    # initial
    pin['adder1'] = 8
    pin['adder2'] = 3
    pregIn['read_addr'] = 0
    for x in range(0,10):
        pregIn['writ_addr'] = x
        pregIn['data'] = x
        pregfile.function()
        pregfile.update()
    #print(pregfile.__reg)
    pregIn['writ_addr'] = 0
    for x in range(0,10):
        pregIn['read_addr'] = x
        pregfile.function()
        pregfile.update()
        print(pregOu)
    # funciton
    add.fucntion()
    # update
    add.update()
    print(pout)

def main():
    logging.basicConfig(filename="run.log",filemode='w',level=logging.DEBUG)
    testbench()

if __name__=="__main__":
    main()
    print("Hi")

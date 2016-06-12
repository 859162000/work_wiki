#! $PATH/python

# file name: circuit_structure.py
# author: lianghy
# time: 2016-6-12 13:28:45

import re
import logging
 
""" 
所有实体先创建，再定义。未经定义(define)的实体是空。
模块定义结构：
[模块名，
【端口方向，端口名】，

]
"""

def checkNameVality(lname):
    valideName = re.compile("[a-z,A-Z,0-9]+")
    if (valideName.fullmatch(lname)):
        return(1)
    else:
        return(0)

class CircuitPin:
    """ 
    逻辑 circuit_pin：
      direction = 'input, output, inout'
      connection = 'pin hierarchy name'
      values = 1, 0
    物理 CTerminal：
      
     """
    def __init__(self):
        self.name = 'empty'
        self.hierName = 'empty'
        self.direction = "input"
        self.connection = 'empty'
        self.values = 0
    def define(self,lpin):
        """[pinDir, pinName] """
        tpn = sorted(x[1] for x in lpin)
        y = "empty"
        for x in tpn[1:]:
            if (x==y):
                logging.error("pin name is defined: %s", x)
                exit(0)
            else:
                y = x
        for x in lpin:
            if (checkNameVality(lpin[0])):
                self.moduleName = lpin[0]
            else:
                logging.error("pin name is invalid: %s",lpin[0])
                exit(0)
            self.direction = x[0]
            self.name = x[1]
    def update(self):
        if (self.connection == 'empty'):
            pass
        else:
            try:
                self.values = getPinValue(self.connection)
            except 'cir_nfpin':
                pass

class CircuitNet:
    def __init__(self):
        self.driverPin = "empty"
        self.loaderPin = []
        self.delay = 0

class CircuitModule:
    """define pinList, function and delay time """
    def __init__(self):
        self.pinList = []
        self.delayTime = 1
        pass
    def define(self,lpin):
        for x in lpin[1]:
            tpin = CircuitPin()
            tpin.define(x)
            self.addPin(tpin)
    def addPin(self,lpin):
        # check pin name todo
        self.pinList.append(tpin)
        pass
    def function(self):
        print("empty function")
        return(1)
    def createInstance(self,linst):
        if (checkNameVality(linst[0])):
            tinstance = linst[0]
        else:
            logging.error("inst name is invalid: %s",linst[0])
            exit(0)
        #check instance name unique todo
        tpn = sorted(x[1] for x in lpin)
        y = "empty"
        for x in tpn[1:]:
            if (x==y):
                logging.error("pin name is defined: %s", x)
                exit(0)
            else:
                y = x

class CircuitException:
    """ 例外列表：
    cir_nfpin 没有找到端口(pin)
    """

class Instance():
    def __init__(self,instanceName):
        self.Name = instanceName
        self.hierName = instanceName
        self.depth = 0
        self.structureI = []
        self.updateChildrenInst()
    def getPinValue(self,pinname):
        #### todo
        return("0")
    def addModule(self,module_instance,module_path):
        #### todo
        return(1)
    def connectPin(self,pin1,pin2)
        #### todo
        # 增加层次名
        return(1)

if __name__=="__main__":
    print("Hi")

#! $PATH/python

# file name: circuit_structure.py
# author: lianghy
# time: 2016-6-12 13:28:45

import re
import logging
 
""" 
工作流程：
 设计模块：定义
 实例化顶层：从上而下，检查每个模块，生成检查表，时间+状态。
 仿真顶层：确认实例化正确，开始仿真。

模块是基本结构。线也是模块。
模块结构：
  模块名，
  端口列表：【端口方向，端口名】，
  功能函数

模块设计：
 class myModulea(CircuitModule):
    def __init__(self):
        moduleName="moda",
        self.pinDefine = "
        input a;
        input [10:0] b;
        input [2:1] c;
        output d;
        "
    def function(self):
        myFunction
模块实例化步骤：
 insta = myModulea().createInstance(parent="top",instName="empty")
        self._pinList = ({pinDir:"i",pinName="a",pinWidth=10},{})
 module
"""

def checkNameVality(lname):
    """名字只有字母和数字"""
    valideName = re.compile("[a-z,A-Z,0-9]+")
    if (valideName.fullmatch(lname)):
        return(1)
    else:
        raise Exception("NameInvalid")
        return(0)

class CircuitException:
    """ 例外列表：
    cir_nfpin 没有找到端口(pin)
    NameInvalid 命名不合法
    PinDuplicated 端口名重命名
    """

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
        self.moduleName = 'empty'
        self.pinDefine = ""
        self.delayTime = 1
        pass
    def addPin(self,lpin):
        # check pin name todo
        self.pinList.append(tpin)
        pass
    def function(self):
        print("empty function")
    def createInstance(self,parent="top",instName="empty",*args):
        try:
            checkNameVality(self.moduleName))
            checkPinUnique(self.modulePinDefine))
            checkInstanceNameUnique(parent,instName)
            linst = Instance(parent,instName)
        except Exception as lexcept:
            if (lexcept.args == "NameInvalid"):
                logging.error("inst name is invalid: %s", self.moduleName)
            elif (lexcept.args == "PinDuplicated"):
                logging.error("pin name is redefined: module %s, pin %s",
                        self.moduleName, x)
        #check instance name unique todo ##########
        tpn = sorted(x[1] for x in lpin)
        y = "empty"
        for x in tpn[1:]:
            if (x==y):
                logging.error("pin name is defined: %s", x)
                exit(0)
            else:
                y = x

class Instance(CircuitModule):
    def __init__(self,parent="top",instName="empty",*args):
        """ 
        self.instName = instName
        self.hierName = hierarchy instanceName
        """
        self.instName = instName
        self.hierName = parent+'/'+instName
        #self.depth = 0
        #self.structureI = []
        # initial Instance
        if (checkNameVality(instName)):
            tinstance = linst[0]
        else:
            logging.error("inst name is invalid: %s",linst[0])
            exit(0)
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
    def _generatePin(self):
        for x in lpin[1]:
            tpin = CircuitPin()
            tpin.define(x)
            self.addPin(tpin)

class CircuitSimulator:
    def __init__(self,topInstance,logfile="run.log"):
        self.topInst = topInstance
        logging.basicConfig(filename=logfile,filemode='w',level=logging.DEBUG())


if __name__=="__main__":
    print("Hi")

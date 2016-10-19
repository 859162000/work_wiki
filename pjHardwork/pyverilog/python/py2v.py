#! $PATH/python

# file name: regfile.py
# author: lianghy
# time: 2016/7/4 21:08:27

import dyDebug

class Cport:
    """提供单点初始值。可以初始化，可以在运行过程中被改变。"""
    pass

class Cnet:
    """由于net不存储值，所以不区分入口与出口。"""
    # ????????
    def __init__(self,name,width):
        self.__name = name
        self.__width = width
        self.conna = ''
        self.connb = ''
        self.vtype = "net"
        return
    def name(self):
        return(self.__name)
    def width(self):
        return(self.__width)
    def connect(self,**key):
        return
    def function(self):
        # 如果延时是0，则更新时，在所有更新完成后，再更新一次延时为0的单元。
        return

class CpinIn:
    """pin 引用时，将连接对象作为参数进行传递。如果是对象（net），则是全连接。
    否则应该使用列表【】进行定义。
    【（对象，字节、位宽）】 == [(net,'1:2'),(net,'3')]. 
    未连接的线（悬空），统一连接到 class:悬空类 :nexc"""
    def __init__(self,width='0b1',connection=''):
        self.__direc = 'input'
        self.__width = width
        self.__value = ''
        try:
            self._check()
        except Exception as exc;
            dyDebug.error('定义。'+exc,self.__name__)
        try:
            connect_type = _check_con_type(connection)
            combine_conn = self.check(connect_type)
            self.connection = combine_conn
        except Exception as exc;
            dyDebug.error("连接。"+exc,self.__name__)
    def name(self):
        return(self.__name__)
    def width(self):
        return(self.__width)
    def _check(self):
        if (self.__width>0 and isinstance(self.__width,(int))):
            return(True)
        else:
            raise Exception("参数有误。{}")
    def _check_con_type(self,tar):
        if (isinstance(tar,'list')):
            if (self._check_width()):
                self.connetcion = tar
            else:
                raise Exception("位宽不对。 {}")
        elif (isinstance(tar,'net')):
            if (tar.width == self.__width):
                self.connetcion = tar
            else:
                raise Exception("位宽不对。{}")
        else:
            raise Exception("未知连接类型：{}。 \{\}".format(type(tar)))
    def _check_width(self,tar):
        # 本函数仅检查拼接连接的情况
        twidth = 0
        try:
            for onetar in tar:
                twidth += self._add_width(onetar)
            return(True)
        except:
            raise Exception("连接拼接不正确。{}")
    def _add_width(self):
        try:
            if (':' in x[1]):
                tstr = x[1].split(':')
                if (len(tstr[1])>0):
                    return(int(tstr[1])-int(tstr[0]))
                else:
                    return(x[0].width()-int(tstr[0]))
        except Exception as exc:
            #dyDebuge.debug(exc)
            raise Exception

class CpinOu:
    def __init__(self):
        self.__inner = "0bxxxxxxxx"
        self.__outer = "0bxxxxxxxx"
        return
    def value(self,''):
        """get output value """
    def assign(self,''):
        """set output value """
    def update(self):
        self.__outer = self.__inner
        
class module:
    """redine functions : pin_in, pin_ou, function
       pin = {'a':'value'/link,}
       pin_net/pou_net : the net pin connected with, out of module"""
    def __init__(self,pin,pou,**key):
        dyDebug.inof("build module %s", self.__name__)
        return
    def update(self):
        """ move data from assign() to value() """
        return
    def function(self):
        self.a = {'width':4, 'connect':[{'name':'x','bit':[2,1]}]}
        try:
            pass
        except KeyError as e:
            print("Error: input pin is changed by other class. pin: "+e)
            exit(0)
        return
    def check_width(self,width):
        return(1)

def Cadder(Cmodule):
    def __init__(self,adder1='',adder2='',result='',*argc):
        #Cmodule.__init__(adder1,adder2,result,*argc)
        self.adder1 = CpinIn(4,adder1)
        self.adder2 = CpinIn(4,adder2)
        self.result = CpinOu(4,result)
        pass

def testbench():
    pin = {}
    pout = {}
    port_adder1 = Cport()
    port_adder2 = Cport()
    nadd_out = Cnet()
    add = Cadder(adder1=port_adder1,port_adder2,nadd_out)
    result_mux = Cmux(nadd_out)
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
    dyDebug.basicConfig(filename="run.log",filemode='w',level=dyDebug.DEBUG)
    testbench()

if __name__=="__main__":
    main()
    print("Hi")

"""
端口：当传递的连接对象为空时，不进行连接。需要连接时，调用connect函数
类分为逻辑类和物理类。逻辑类引用物理类的数据。逻辑类不能修改数据。
逻辑类分为仿真类和描述类。仿真类在仿真时，参与计算，描述类只是指引建立连接关系。
器件从Pin的指引地点取值，将结果写入指引地点'0bxxxxxxxx'。写入时，通过改变其中某位的值，而不是直接改变引用地址。【11111111】。
:next
双向的net，连接到双向的pin。
双向pin必然有状态指示：驱动或者接收。
"""

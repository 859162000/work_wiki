#! $PATH/python

# file name: dyVerilog.py
# author: lianghy
# time: 2016/7/4 21:08:27

#import dyDebug
#import dyTool

def checkName(name):
    # TODO: 增加名称检查。例外
    if name:
        print("创建模块 {}".format(name))
        return(name)
    else:
        print("创建模块失败")
        raise Exception("未命名")
        return(None)

def addMaster(master):
    try:
        if (master):
            master = master._master+master._insName
            return(master)
        else:
            return(None)
    except Exception as exp:
        raise(exp)

def changeDataFormat(tar,data):
    """当外部（仿真时）输入十进制int型数据时，转换成二进制字符串
    并检查位宽。"""
    if (isinstance(data,(int))):
        value = bin(data)
    elif (isinstance(data,(str)) and data[0:2]=='0b'):
        value = data
    else:
        raise(Exception('data type'))
    tv_length = len(value)
    # int 和 bin类型数据长度都大于0
    if (tv_length > tar):
        raise(Exception('位长错误'))
    elif (tv_length < tar):
        # 补全位长，高位补0。有可能是负数(x)。
        tv = value[0:2]
        for x in range(tar-tv_length):
            tv += '0'
        tv += value[2:]
        return(tv)
    else:
        return(value)

class module:
    def __init__(self,master=None,name=None,*args,**kwargs):
        try:
            self._master = addMaster(master)
            self._insName = checkName(name)
        except:
            raise Exception("Module {} initial ".format(name))

class port():
    def __init__(self,master=None,name=None,width=1,direc='input',
            *args,**kwargs):
        print(master._master)
        try:
            self._master = addMaster(master)
            self._insName = checkName(name)
            self._direc = (lambda x,y : y[y.index(x)])(direc,['input','output'])
            print("port {} initial succeed!".format(name))
        except Exception as exp:
            print("port {} initial failed!".format(name))
            raise(exp)
        self._width = width
        self._value = '0b0'
        pass
    def get_value(self):
        """返回port的值"""
        return(self._value)
    def set_value(self,value='0b0'):
        """供仿真时，由外部人工设置值"""
        try:
            self._value = changeDataFormat(self._width,value)
        except Exception as exc:
            raise exc
    def _pass_value(self,value):
        """在仿真时，由net传递而来的值。由于其值都是经过检查的，所以不再进行检查。"""
        self._value = value

class net:             
    """ 
    loader is list such as: [port,]"""
    def __init__(self,master=None,name=None,driver=None,loader=None,
            *args,**kwargs):
        self._loader = []
        try:
            self._master = addMaster(master)
            self._insName = checkName(name)
            self._driver = driver
            if loader:
                self._loader += loader
            self._checkMatch()
            print("net {} initial succeed!".format(name))
        except Exception as exp:
            print("Net {} initial failed!".format(name))
            raise(exp)
    def _checkMatch(self):
        try:
            self.__checkDriver()
            self.__checkLoader()
            self.__checkWidth()
        except Exception as exp:
            raise(exp)
    def __checkDriver(self):
        if (self._driver):
            if (isinstance(self._driver,(port)) 
                    and (self._driver._direc == 'output')):
                return(True)
            else:
                raise(Exception("driver type error: {}".format(
                    self._driver._insName)))
    def __checkLoader(self):
        for x in self._loader:
            if isinstance(x,(port)):
                if (x._direc == 'input'):
                    continue
                else:
                    raise(Exception("loader type error: {}".format(
                        self._driver._insName)))
            else:
                raise(Exception("loader type error"))
    def __checkWidth(self):
        if (self._driver and self._loader):
            dwidth = self._driver._width
            for x in self._loader:
                if (dwidth != x._width):
                    raise(Exception(
                        "width mismatch: driver {0} vs loader {1}".format(
                        dwidth,x._width)))
    def set_driver(self,driver=None):
        if (driver):
            if (self._driver):
                raise Exception("driver has defined")
            elif self._loader:
                self._checkWidth(self._loader[0],driver)
            else:
                self._driver=driver
    def add_loader(self,loader=None):
        """loader must be list"""
        self._loader += loader
        self._checkWidth()
    def __call__(self):
        # 延时最小为1， TODO:增加延时。
        for x in self._loader:
            x._pass_value(self._driver.get_value())
                 
class testbench():
    def __init__(self):
        self._master = "TOP"
        self._insName = "testbench"
        self._module = []
        self._net = []
    def run(self,ltime):
        for x in range(ltime):
            self.function()
    def function(self):
        for x in self._module:
            x()
        for x in self._net:
            x()

def test():
    #dyDebug.basicConfig(filename="run.log",filemode='w',level=dyDebug.DEBUG)
    print('newtest')
    #testbench()

if __name__=="__main__":
    test()
    print("pyVerilog")


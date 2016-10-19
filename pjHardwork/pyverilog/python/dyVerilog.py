#! $PATH/python

# file name: dyVerilog.py
# author: lianghy
# time: 2016/7/4 21:08:27

def changeDataFormat(tar_width,data):
    """当外部（仿真时）输入十进制int型数据时，转换成二进制字符串
    并检查位宽。
    当位宽超过目标值时，取高位位宽"""
    if (isinstance(data,(int))):
        value = bin(data)
    elif (isinstance(data,(str)) and data[0:2]=='0b'):
        value = data
    else:
        raise(Exception('data type'))
    tv_length = len(value)-2
    # int 和 bin类型数据长度都大于0
    if (tv_length > tar_width):
        #raise(Exception('位长错误'))
        tv = value[0:tar_width+2]
    elif (tv_length < tar_width):
        # 补全位长，高位补0。有可能是负数(x)。
        tv = value[0:2]
        for x in range(tar_width-tv_length):
            tv += '0'
        tv += value[2:]
    else:
        tv = value
    return(tv)

class module:
    def __init__(self,*args,**kwargs):
        self._define()
        pass
    def __call__(self,run_times=1):
        """先逻辑计算，再调子模块，再传递值.
        run_times: 运行时长。"""
        print(self.__class__)
        for x in range(run_times):
            self._func()
            self._module()
            self._net()
    def _define(self):
        pass
    def _func(self):
        pass
    def _module(self):
        pass
    def _net(self):
        pass

class port():
    def __init__(self,width=1,direc='input', *args,**kwargs):
        """初始化为0"""
        try:
            self._direc = (lambda x,y : y[y.index(x)])(direc,['input','output'])
            print("port initial succeed!")
        except Exception as exp:
            print("port initial failed!")
            raise(exp)
        self._width = width
        self._value = '0b'+'0'*width
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
    def __init__(self,driver=None,loader=None,
            *args,**kwargs):
        self._loader = []
        try:
            self._driver = driver
            if loader:
                self._loader += loader
            self._checkMatch()
            print("net initial succeed!")
        except Exception as exp:
            print("Net initial failed!")
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
                 
def test():
    #dyDebug.basicConfig(filename="run.log",filemode='w',level=dyDebug.DEBUG)
    print('newtest')
    #testbench()

if __name__=="__main__":
    test()
    print("pyVerilog")


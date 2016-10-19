#! $PATH/python

# file name: test.py
# author: lianghy
# time: 2016-8-3 16:49:52

def check_name(name):
    # TODO: 增加名称检查。例外
    def fcheck(f):
        if name:
            print(name)
        else:
            raise Exception("未命名")
        return(f)
    return(fcheck)

@check_name("hello")
class pin():
    def __init__(self,name=None):
        self.__name = name
        self.ok = "work"
        pass

a = pin("b")
print(dir(pin))
print(a.ok)

print("hello")
print("\b\b")
if __name__=="__main__":
    print("test.py")

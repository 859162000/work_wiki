#! $PATH/python

# file name: dyDebug.py
# author: lianghy
# time: 2016-7-22 14:13:39

def error(info, *args):
    tstr = "print(\"Error:"+info+"\".format("
    for x in args:
        tstr += x+','
    tstr = tstr[0:-1]+'))'
    exec(tstr)
    exit(0)

def debug(info):
    print('Debug:'+info)

if __name__=="__main__":
    error("a {}, b{}", '1','2')
    print("dyDebug.py")

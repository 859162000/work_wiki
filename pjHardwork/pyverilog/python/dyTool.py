#! $PATH/python

# file name: dyTool.py
# author: lianghy
# time: 2016-7-27 14:46:13

def CdataFormat(data):
    if (isinstance(data,(int))):
        return(bin(data))
    elif (isinstance(data,(bin))):
        return(data)
    else:
        raise Exception('Error data type')

if __name__=="__main__":
    print("dyTool.py")

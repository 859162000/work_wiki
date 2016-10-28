#! $PATH/python

# file name: recognise.py
# author: lianghy
# time: 2016-9-18 16:07:57

class recognise():
    def __init__(self):

        with open(self.savePicture(),'r') as f:
            tl = f.readline()
            while(tl):
                if (tl.startswith("%%Page:")):
                    # next : while else语法
                    self.anaGetPageSize(tl)
                    break
                tl = f.readline()
            else:
                raise(Exception("无法编译图形文件"))
    def anaGetPageSize(self,tl):
            while(tl):
                if (tl.startswith("%%Page:")):
                    self.anaGetPageSize(tl)
                    break
            else:
                raise(Exception("无法编译图形文件"))
    def savePicture(self):
        fname_list = fd.asksaveasfilename()
        if (isinstance(fname_list,(List))):
            self.input_canvas.postscript(file=fname_list[0])
            return(fname_list[0])
        elif (len(fname_list)>0)::
            self.input_canvas.postscript(file=fname_list)
            return(fname_list)

if __name__=="__main__":
    print("recognise.py")

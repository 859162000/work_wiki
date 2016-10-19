#! $PATH/python

# file name: drawIF.py
# author: lianghy
# time: 2016-9-19 16:55:03

import tkinter as tk
import os
#from tkinter import filedialog as fd

class inputCanvas:
    def __init__(self):
        tk_root = tk.Tk()
        self.main_frame = tk.Frame(tk_root,relief=tk.RIDGE, borderwidth=2)
        self.main_frame.pack(fill=tk.BOTH,expand=1)
        self.frameInit()
        self.confInit()
        tk_root.mainloop()
    def frameInit(self):
        self.input_canvas = tk.Canvas(self.main_frame,relief=tk.RIDGE, borderwidth=2)
        self.input_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
        self.toolbar = tk.Frame(self.main_frame, relief=tk.RIDGE,
                borderwidth=2, width=100)
        self.toolbar.pack(side=tk.RIGHT,fill=tk.Y,expand=1)
        self.saveCSButton = tk.Button(self.toolbar, text="生成图片",
                command=self.savePicture)
        self.saveCSButton.pack(side=tk.TOP)
        self.cvBind()
    def confInit(self):
        self.mouse_x = 0.0
        self.mouse_y = 0.0
        self.cv_draw_line_en = False
    def cvBind(self):
        #TODO：画布大小，不能画出图形画布。
        """ 
        # enter : set current mouse coordinate
        # Leave : stop setting coordinate
        # press : show the footprint
        # release : not show the footprint
        """
        self.input_canvas.bind('<Motion>',self.cvMotion)
        #self.input_canvas.bind('<Enter>',self.cvEnter)
        #self.input_canvas.bind('<Leave>',self.cvLeave)
        self.input_canvas.bind('<ButtonPress-1>',self.cvPressButtonLeftKey)
        self.input_canvas.bind('<ButtonRelease-1>',self.cvReleaseButtonLeftKey)
    def cvMotion(self,event):
        if (self.cv_draw_line_en):
            self.cvDrawLine(event.x,event.y)
        self.mouse_x = event.x
        self.mouse_y = event.y
    def cvEnter(self,event):
        if (self.cvDrawLine):
            self.cvDrawLine(event.x,event.y)
        self.mouse_x = event.x
        self.mouse_y = event.y
    def cvPressButtonLeftKey(self,event):
        self.cv_draw_line_en = True
    def cvReleaseButtonLeftKey(self,event):
        self.cv_draw_line_en = False
    def cvDrawLine(self,cx,cy):
        self.input_canvas.create_line(self.mouse_x,self.mouse_y,cx,cy)
    def savePicture(self):
        tfs = self.input_canvas.postscript()
        fl = os.listdir('.')
        fn = '.tmp0'
        while (fn in fl):
            fn = '.tmp'+str(int(fn[4:])+1)
        else:
            with open(fn,'w') as f:
                f.write(tfs)
                print('write file ',fn)


def test():
    app = inputCanvas()

if __name__=="__main__":
    print("drawIF.py")
    test()

#! $PATH/python
#-*- coding: utf-8 -*-

# file name: sparrow
# author: lianghy
# start at: 2016-06-15


import tkinter as tk
#from tkinter.constants import *
from tkinter import filedialog as tkfd
import re
import logging

class CtextWidget(tk.Text):
    def __init__(self,lroot,**kw):
        tk.Text.__init__(self,lroot,kw)
        self.__parent = lroot
        self.pstateBarStr = lroot.lstateBar.pstateBarStr
        self.pcommandStr = lroot.lcommandBar.pcommandStr
        self.pchInBarStr = lroot.lchineseInputBar.pchInBarStr
        #self.config(insertunfocused="solid" )
        #self.config(cursor="solid" )
        #self.insert
        self.parameterDefine()
        self.textKeyBind()
    def parameterDefine(self):
        """ parameter define:
            linputChCode : 中文输入模式下，输入汉字的编码"""
        ## todo : 限制命令长度，限制显示字符长度。
        self.ltextWigShow = tk.StringVar()
        self.pstateBarStr.set("只读")
    def textKeyBind(self):
        self.bind(":", self.textReadColon)
        self.bind("b", self.textReadB)
    ############# KeyCompile function list
    def textReadColon(self,event):
        """切换到命令输入模式"""
        #print("run here")
        self.__parent._editorState = "command"
        self.pstateBarStr.set("命令输入")
        self.config(state=tk.DISABLED)
        #self.pcommandStr.set("command_input")
        self.__parent.lchineseInputBar.focus_set()
    def textReadB(self,event):
        """切换到编辑模式"""
        self.__parent._editorState = "edit"
        self.pstateBarStr.set("编辑")
        self.config(state=tk.DISABLED)
        self.__parent.lchineseInputBar.focus_set()

class CcommandLabel(tk.Label):
    def __init__(self,lroot, **kw):
        tk.Label.__init__(self,lroot,kw)
        self.pcommandStr = tk.StringVar()
        self.config(textvariable=self.pcommandStr)
        self.config(state=tk.NORMAL)

class CchineseInputBar(tk.Label):
    def __init__(self,lroot, **kw):
        tk.Label.__init__(self,lroot,kw)
        self.pchInBarStr = tk.StringVar()
        self.__parent = lroot
        self.config(textvariable=self.pchInBarStr)
        self.config(anchor=tk.W)
        self.parameterDefine()
        self.textKeyBind()
    def parameterDefine(self):
        self.linputChCode = ""
        ## todo : chineseDict should read from a file
        self.pchineseDict = {'g':'一','b':'旦'}
    def textKeyBind(self):
        self.bind("<Key>", self.chineseInput)
        self.bind("<Return>", self.commandReturn)
        self.bind("<Escape>", self.commandEsc)
        # 中文特殊字符 next
    def commandEsc(self,event):
        """退出命令/编辑，切换到只读模式"""
        if (len(self.linputChCode)!=0):
            self.linputChCode = ""
            self.lchineseSearchResult = []
        else:
            self.__parent._editorState = "read"
            self.__parent.lstateBar.pstateBarStr.set("只读")
            self.__parent.ltextWig.focus_set()
    def commandReturn(self,event):
        """执行命令"""
        if (len(self.linputChCode)!=0):
            self.linputChCode = ""
            self.lchineseSearchResult = []
        elif (self.__parent._editorState=="command"):
            # todo
            pass
        else:
            self.lchineseSearchResult = ["\n"]
            self.insertWord()
        return
    def searchChWord(self):
        """查找汉字"""
        self.lchineseSearchResult = []
        for (k,v) in self.pchineseDict.items():
            if (self.linputChCode==k[:len(self.linputChCode)]):
                self.lchineseSearchResult.append(v)
        if (len(self.lchineseSearchResult)==0):
            self.pchInBarStr.set("{0:<10} : \
                1.没有找到对应的字符".format(self.linputChCode))
        else:
            # todo 只显示一个字符
            self.pchInBarStr.set("{0:<10} : \
                1.{1}".format(self.linputChCode,
                self.lchineseSearchResult[0]))
    def chineseInput(self,event):
        """中文输入。
        空格 输入第一个字
        <Escape>清空编码（在Esc中实现）
        todo ；   输入英文"""
        if (event.char==" "):
            self.insertWord()
        elif (len(self.linputChCode)==5):
            self.insertWord()
        else:
            # 输入字符非空，且编码长度小于5，继续
            self.linputChCode += event.char
            self.searchChWord()
    def insertWord(self):
        self.linputChCode = ""
        if (len(self.lchineseSearchResult) == 0):
            return
        elif (self.__parent._editorState == "edit"):
            self.__parent.ltextWig.config(state=tk.NORMAL)
            self.__parent.ltextWig.insert(tk.END,self.lchineseSearchResult[0])
            self.__parent.ltextWig.config(state=tk.DISABLED)
                    # todo 在命令输入模式下，如果鼠标点击了text区域，
                    #或任何方式切换了焦点对象，
                    #则任何输入都自动切换command为焦点，
                    #并将输入值传递给command的字符变量。
        elif (self.__parent._editorState == "command"):
            self.__parent.lcommandBar.pcommandStr.set(
                    self.__parent.lcommandBar.pcommandStr.get() + \
                    self.lchineseSearchResult[0])
        else:
            return

class CstateBar(tk.Label):
    def __init__(self,lroot, **kw):
        tk.Label.__init__(self,lroot,kw)
        self.__parent = lroot
        self.pstateBarStr = tk.StringVar()
        self.config(textvariable=self.pstateBarStr)
        self.config(anchor=tk.W)
        self.KeyBind()
    def KeyBind(self):
        self.bind(":", self.readColon)
        self.bind("b", self.readB)
    ############# KeyCompile function list
    def readColon(self,event):
        """切换到命令输入模式"""
        #print("run here")
        self.__parent._editorState = "command"
        self.pstateBarStr.set("命令输入")
        self.__parent.lchineseInputBar.focus_set()
        #self.__parent.ltextWig.config(state=tk.NORMAL)
    def readB(self,event):
        """切换到编辑模式"""
        self.__parent._editorState = "edit"
        self.pstateBarStr.set("编辑")
        # next ? 如何显示光标在何处？
        #self.__parent.ltextWig.config(state=tk.NORMAL)
        self.__parent.lchineseInputBar.focus_set()

class CmainFrame(tk.Frame):
    """主窗口有两个：内容，输入。对应的变量是ltextWigShow, pcommandStr
    """
    def __init__(self,lroot, **kw):
        tk.Frame.__init__(self,lroot,kw)
        self.pack(fill=tk.BOTH, expand=1)
        self._editorState = "read"
        self.widgetDefine()
        #root.protocol("WM_DELETE_WINDOW", callback)
    def widgetDefine(self):
        """ widgets define"""
        self.lchineseInputBar = CchineseInputBar(self)
        self.lcommandBar = CcommandLabel(self) 
        self.lstateBar = CstateBar(self)
        self.ltextWig = CtextWidget(self)
        self.ltextWig.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.lcommandBar.pack(side=tk.TOP, fill=tk.X, expand=0)
        self.lchineseInputBar.pack(side=tk.TOP, fill=tk.X, expand=0)
        self.lstateBar.pack(side=tk.TOP, fill=tk.X, expand=0)
        self.lstateBar.focus_set()

def sMenu(lroot):
    """菜单"""
    lMenu = tk.Menu(lroot)
    tfile = tk.Menu(lMenu)

def main():
    """键盘映射命名规则是，状态名+按键名"""
    root = tk.Tk()
    #menu = sMenu(root)
    CmainFrame(root, relief=tk.RIDGE, borderwidth=2)
    root.mainloop()

if (__name__ == "__main__"):
    print("这是中文文本编辑器。欢迎试用！")
    main()

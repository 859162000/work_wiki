    def keyCompile(self):
        """命令解析
        { mode:{ string : command_function}, }
        """
        self.keyDict = {
                "read":{
                    ":" : self.textReadColon,
                    "b" : self.textReadB
                    },
                "edit":{
                    # ctrl+
                    },
                "command_input":{
                    # todo 在此模式下，如果鼠标点击了text区域，
                    #或任何方式切换了焦点对象，
                    #则任何输入都自动切换command为焦点，
                    #并将输入值传递给command的字符变量。
                    }
                }

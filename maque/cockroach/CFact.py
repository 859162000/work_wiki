
import random

class CFact:
    """generate action number according to generic info"""
    def Fact(self):
        return(random.randint(self.lgen['stop'],self.lgen['move']))

if __name__=="__main__":
    print("Hi")

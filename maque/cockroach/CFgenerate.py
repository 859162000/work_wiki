
import random

class CFgenerate:
    """random change generic info"""
    def Fgenerate(self,istate):
        if (self.lstate['birth_time']==10):
            tstop = self.lgen['stop']
            tmove = self.lgen['move']
            if (random.randint(0,100)<50):
                if (tstop>0):
                    tnstop = tstop-1
                    tnmove = tmove-1
                else:
                    tnstop = tstop
                    tnmove = tmove
            else:
                if (tmove<100):
                    tnstop = tstop+1
                    tnmove = tmove+1
                else:
                    tnstop = tstop
                    tnmove = tmove
            istate['new_gen']['stop'] = tnstop
            istate['new_gen']['move'] = tnmove
            istate['new_children'] = True
            self.lstate['birth_time'] = 0
        else:
            return

if __name__=="__main__":
    print("Hi")

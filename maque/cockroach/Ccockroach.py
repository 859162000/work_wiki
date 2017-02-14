
from Cfoot import Cfoot
from CFact import CFact
from CFdie import CFdie
from CFgenerate import CFgenerate

class Ccockroach(Cfoot,CFact,CFdie,CFgenerate):
    """
    lgen : for Fact
        -> stop is 0 - 50
        -> move is 50 -100
    life_time : alive state, is set 54
    birth_time : new children
    """
    def __init__(self,mother_croach_lgen):
        self.lgen = mother_croach_lgen.copy()
        self.lstate = {'life_time':0, 'birth_time':0}
        self._max_life = 54

    def Flive(self,istate):
        """如果死亡，则返回False"""
        if (self.Fdie(istate)):
            return(False)
        else:
            self.lstate['life_time'] += 1
            self.lstate['birth_time'] += 1
            self.Fgenerate(istate)
            self.Ffoot(self.Fact(),istate)
            return(True)

if __name__=="__main__":
    print("Hi")

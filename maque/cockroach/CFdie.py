
class CFdie:
    def Fdie(self,istate):
        """当达到死亡条件时，返回True"""
        istate['alive'] = (self.lstate['life_time']<self._max_life)
        return(not istate['alive'])

if __name__=="__main__":
    print("Hi")

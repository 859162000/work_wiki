
from Ccockroach import Ccockroach
import logging
import copy

temp_state = {
        'movement':True,
        'alive':True,
        'new_children':False,
        'new_gen':{'stop':30,'move':70}}

class Cenv:
    """
    以时间触发动作。每秒动作一次。
    """
    def __init__(self):
        self.ptimer = 0
        self.pcroach_list = []
        self.pnew_croach_list = []
        self.lns_time = 0
        self.lkilled_num = 0
        self.lnew_num = 0
        self.ldied_num = 0
        self._killed_margin = 100
        logging.info("start running:")
        # 参数说明：
        # lns_time 自然选择间隔
        # lkilled_num 每轮杀死的个数
        # _killed_margin 对象数量门槛


    def Fcroach_info(self):
        logging.info("%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s",
                "life","birth","stop","move",
                "movement","alive","new_children",
                "stop","move")
        for x in self.pcroach_list:
            logging.info("%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s \t%s",
                    x['croach'].lstate['life_time'],
                    x['croach'].lstate['birth_time'],
                    x['croach'].lgen['stop'],
                    x['croach'].lgen['move'],
                    x['state']['movement'],
                    x['state']['alive'],
                    x['state']['new_children'],
                    x['state']['new_gen']['stop'],
                    x['state']['new_gen']['move']
                    )
    def Ftimer(self):
        self.Freset()
        self.ptimer += 1
        self.lns_time += 1
        for tx in self.pcroach_list:
            # cockroach action
            tx['croach'].Flive(tx['state'])
            # 处理环境变化
            self.Fadd(tx)
            if self.Fdel(tx):
                continue
            elif self.Fnature_seletion(tx):
                continue
            else:
                self.pnew_croach_list.append(tx)
        self.pcroach_list = self.pnew_croach_list
        self.pnew_croach_list = []
        self.Freport()

    def Fadd(self,tx):
        """each time generate 9 children"""
        global temp_state
        if tx['state']['new_children']:
            tx['state']['new_children'] = False
            self.pnew_croach_list.append(tx)
            self.lnew_num += 1
            for x in range(9):
                tcroach = Ccockroach(tx['state']['new_gen'])
                self.pnew_croach_list.append({'croach':tcroach,'state':copy.deepcopy(temp_state)})
            return(True)
        else:
            return(False)

    def Fdel(self,tx):
        if tx['state']['alive']:
            return(False)
        else:
            self.ldied_num += 1
            return(True)

    def Fnature_seletion(self,tx):
        if (len(self.pcroach_list) > self._killed_margin):
            if tx['state']['movement']:
                return(False)
            else:
                self.lkilled_num += 1
                return(True)
        else:
            return(False)

    def Freport(self):
        # 报告环境情况
        if (self.lnew_num > 0):
            logging.info("generate new children %s",str(self.lnew_num))
        if (self.lkilled_num > 0):
            logging.info("killed count is %s",str(self.lkilled_num))
        if (self.ldied_num > 0):
            logging.info("died count is %s",str(self.ldied_num))
        if (self.lnew_num > 0 or self.lkilled_num > 0 or self.ldied_num > 0):
            logging.info("the cockroach count now is %s",
                    str(len(self.pcroach_list)))
            self.Fcroach_info()

    def Freset(self):
        # 将每次处理的临时变量清零
        self.lnew_num = 0
        self.lkilled_num = 0 
        self.ldied_num = 0
        if (len(self.pcroach_list) > self._killed_margin):
            self.lns_time = 0

if __name__=="__main__":
    print("Hi")


from Ccockroach import Ccockroach
from Cenv import *
import logging
import copy


def main():
    global temp_state
    logging.basicConfig(filename="run.log",
            filemode='w',level=logging.INFO)
    env = Cenv()
    cockroach = Ccockroach({'stop':30,'move':70})
    logging.info("first cockroach")
    env.pcroach_list.append({'croach':cockroach,
        'state':copy.deepcopy(temp_state)})
    while (env.ptimer<100):
        logging.info("time is %s",str(env.ptimer))
        env.Ftimer()
    with open("./result.txt",'w') as ff:
        ff.write(str(len(env.pcroach_list))+'\n')
        for x in env.pcroach_list:
            ff.write(str(x['croach'].lgen)+'\n')


if __name__=="__main__":
    main()

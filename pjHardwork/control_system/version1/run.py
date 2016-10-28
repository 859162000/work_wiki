#! $PATH/python

# file name: run.py
# author: lianghy
# time: 2016-10-11 17:11:23

import receptor
import memoryCenter
import inforCenter
import motorCenter
import effector

def main():
    module_input = receptor.receptor()
    module_memory = memoryCenter.memoryCenter()
    module_analyse = inforCenter.inforCenter()
    module_action = motorCenter.motorCenter()
    module_output = effector.effector()


if __name__=="__main__":
    print("run.py")
    main()

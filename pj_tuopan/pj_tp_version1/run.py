#! $PATH/python

# file name: run.py
# author: lianghy
# time: 2016-6-12 16:02:07

def main():
    logging.basicConfig(filename="run.log",filemode='w',level=logging.DEBUG())
if __name__=="__main__":
    print("Hi")

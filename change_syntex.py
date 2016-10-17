#! $PATH/python

# file name: change_syntex.py
# author: lianghy
# time: 2016-8-30 14:15:04

import os

source_type = 'md'
target_type = 'wiki'
dirlist = ['.']
while (len(dirlist)>0):
    cur_dir = dirlist.pop()
    for x in os.listdir(cur_dir):
        oldfile = os.path.join(cur_dir,x)
        if os.path.isdir(oldfile):
            dirlist.append(oldfile)
        elif x[0] == '.':
            continue
        elif x[-1*len(source_type):] == source_type:
            newfile = os.path.join(cur_dir,x[:-1*len(source_type)]+target_type)
            print("rename {} to {}".format(x,newfile))
            os.rename(oldfile,newfile)

if __name__=="__main__":
    print("change_syntex.py")

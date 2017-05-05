#! $PATH/python

# file name: change_name.py
# author: lianghy
# time: 2017-4-20 10:55:24
"""批量修改文件名。
使用方法：

1. 设置输入文件名规则
2. 设置输出文件名规则"""

import os,re

RULE = { r"^eID_(.*)":r"xroad_\1"
        }

for one_file in os.listdir('.'):
    for key,value in RULE.items():
        print(key, value)
        new_name = re.sub(key,value, one_file)
        print(new_name)
        os.rename(one_file, new_name)

print('done')

if __name__ == "__main__":
    print("change_name.py")

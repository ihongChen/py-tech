#encoding:utf8

import sys
def console_input(prompt):
    sys.stdout.write(prompt) # 使用標準輸出
    sys.stdout.flush() # 出清資料
    return sys.stdin.readline() #使用標準輸入讀一行

name = console_input('請輸入名稱:')
print('哈嚕',name)

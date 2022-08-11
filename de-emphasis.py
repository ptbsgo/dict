# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 20:31
# @Author  : ptbs
# @File    : de-emphasis.py
# @Software: PyCharm
# ---------CODE-------------
def openfile():
    filename = input("请输入文件路径：")
    try:
        f = open(filename,"r",encoding="utf-8")
        content = f.readlines()
        f.close()
        dict = []
        for i in range(0,len(content)):
            dict.append(content[i].rstrip('\n'))
        # print(dict)
        emphasis = []
        for i in dict:
            if i not in emphasis:
               emphasis.append(i)
               write_file(i)
        # print(emphasis)
    except FileNotFoundError:
        print("文件没找到.")
    except PermissionError:
        print("你没有权限访问此文件.")

def write_file(word):
    import os,time,calendar
    ts = calendar.timegm(time.gmtime())
    dirs = "./tmp"
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    else:
        f = open('./tmp/tmp' + str(ts) + '.txt','a',encoding="utf-8")
        f.write(word + "\n")
        f.close()


if __name__ == '__main__':
    openfile()
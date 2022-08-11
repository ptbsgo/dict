# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 20:03
# @Author  : ptbs
# @File    : top200.py
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
        num =1
        top200 = []
        while num <= 200:
            for i in range(0,len(dict)):
                if str(num) == dict[i]:
                    top200.append(dict[i+1])
                    write_file(dict[i+1])
            num +=1
        print(top200)
    except FileNotFoundError:
        print("文件没找到.")
    except PermissionError:
        print("你没有权限访问此文件.")

def write_file(word):
    import os
    dirs = "./tmp"
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    else:
        f = open('./tmp/top200.txt','a',encoding="utf-8")
        f.write(word + "\n")
        f.close()

if __name__ == '__main__':
    openfile()
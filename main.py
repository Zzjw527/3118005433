# _*_ coding:utf-8 _*_
"""
Created on Mon Sep 21 17:16:17 2020

@author: hp
"""



import time
import re
import sys

def main(): 
    try:
        orig_path, add_path, answer_path= sys.argv[1:4]
    except BaseException:
        print("Error: 输入命令错误")
    else:
        # 判断命令行参数有没有错误
        try:
            orig = open(orig_path,'r',encoding='UTF-8')
            orig_context = orig.read()   
        except IOError:
            print("Error: 没有从该路径：{}找到文件/读取文件失败".format(orig_path))
            conditio_one=0
        else:
            conditio_one=1
            orig.close()

        # 判断抄袭文件路径等是否出错
        try:
            orig_add = open(add_path,'r',encoding='UTF-8')
            add_context = orig_add.read()  
        except IOError:
            print("Error: 没有从该路径：{}找到文件/读取文件失败".format(add_path))
            conditio_two=0
        else:
            conditio_two=1
            orig_add.close()

        # 判断答案文件路径等是否出错
        try:
            answer_txt=open(answer_path,'w',encoding='UTF-8')
        except BaseException:
            print("Error: 创建文件：{}失败".format(answer_path))
            conditio_three=0
        else:
            conditio_three=1
    normal_leven(remove_symbol(orig_context),remove_symbol(add_context))
def normal_leven(str1, str2):
    
    
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
      # 创建矩阵
    matrix = [0 for n in range(len_str1 * len_str2)]
      #矩阵的第一行
    for i in range(len_str1):
        matrix[i] = i
      # 矩阵的第一列
    for j in range(0, len(matrix), len_str1):
        if j % len_str1 == 0:
            matrix[j] = j // len_str1
      # 根据状态转移方程逐步得到编辑距离
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
        matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
        matrix[j*len_str1+(i-1)]+1,
        matrix[(j-1)*len_str1+(i-1)] + cost)
     
    return matrix[-1]  # 返回矩阵的最后一个值，也就是编辑距离

def remove_symbol(context): # 利用正则除去标点符号等等的影响
    remove_rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")  #只保留数字，大小写字母以及中文
    result = remove_rule.sub('', context)
    return result 

if __name__ == '__main__':
    main()
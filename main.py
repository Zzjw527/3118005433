# _*_ coding:utf-8 _*_
"""
Created on Mon Sep 21 17:16:17 2020

@author: hp
"""



import time
import re
import sys

def main(): 
    s1=r'C:\Users\hp\Desktop\大三上\test\orig.txt'
    s1=r'C:\Users\hp\Desktop\大三上\test\orig_0.8_add.txt'
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
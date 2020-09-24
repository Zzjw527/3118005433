第一次个人编程作业
=================
|  这个作业属于哪个课程   | [软件工程](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812)  |
|  ----  | :----:  |
| 这个作业要求在哪里  | [作业要求](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/homework/11155) |
| 这个作业的目标  | 论文查重个人项目 + 单元测试 + PSP表格 + Git管理 + 性能测试 |


# 作业代码连接
* GitHub：[地址](https://github.com/Zzjw527/3118005433)



# 实现思路
1、命令行接收参数，判断是否出错
2、对文档进行处理，除去标点符号的影响
3、利用Levenshtein算法算出相似度
4、写入文件
* python包：Levenshtein,re,time,sys


#核心算法
Levenshtein距离：两个字符之间，有一个转变成另一个所需的最少编辑操作次数
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924012724797-1720105488.png)
* 即数出转换所需要的步数，然后根据得到步数算相似度
* 和余弦算两者距离相似，只不过Levenshtein算法注重的是编辑距离
## 关键函数流程图
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924110954776-1575971289.png)


# 性能改进
## 改进前（动态规划）
```c
def normal_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
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
```
可以看到，运行时间较长且占用很多系统资源
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924105202096-1159572344.png)

## 改进后（利用包Levenshtein将时间复杂度优化，提高准确率的同时，大大缩减了运行所需时间）
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924011221331-805591937.png)

![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924010931888-1616656607.png)

![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924010439851-1390337361.png)

# 异常处理
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924011015929-1647723672.png)
效果图：
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924103740974-731800409.png)
* 可以看到当输入命令错误/路径错误/文件不存在时，都会报错显示出原因
* 在读取指定文件路径时，如果文件路径不存在，程序将会出现异常并且报出相应错误，因此可以在读取指定文件内容之前先判断文件是否存在，若不存在则做出响应并且结束程序。

# 测试其他文件（单元测试结果）
在pycharm的Edit Configuration中添加Python test进行单元测试
代码覆盖率：100

```c
源文件:orig.txt
抄袭文件:orig_copy.txt（同一份文件）
转换所需步长：0
查重率：1.00

源文件:orig.txt
抄袭文件:orig_other.txt（其他文件）
转换所需步长：8316
查重率：0.03

源文件:orig.txt
抄袭文件:orig_0.8_add.txt
转换所需步长：1763
查重率：0.91

源文件:orig.txt
抄袭文件:orig_0.8_del.txt
转换所需步长：1656
查重率：0.89

源文件:orig.txt
抄袭文件:orig_0.8_dis_1.txt
转换所需步长：429
查重率：0.97

源文件:orig.txt
抄袭文件:orig_0.8_dis_10.txt
转换所需步长：1562
查重率：0.84

源文件:orig.txt
抄袭文件:orig_0.8_dis_15.txt
转换所需步长：3123
查重率：0.67
```
# PSP表格
|  PSP2.1   | Personal Software Process Stages  |  预估耗时（分钟）  |  实际耗时（分钟）  |  
|  ----  | :----:  | :----:  | :----:  |  
|  Planning   | 计划  |  40  |  30  | 
|  · Estimate   | · 估计这个任务需要多少时间  |  5  |  10  |  
|  Development   | 开发  |  200  |  250  |  
|  · Analysis   | · 需求分析 (包括学习新技术)  | 40  |  35  |   
|  · Design Spec   | · 生成设计文档  |  25  |  20  |  
|  · Design Review   | · 需求分析 (包括学习新技术)  |  45  |  30  |  
|  · Coding Standard  | · 代码规范 (为目前的开发制定合适的规范)  |  15  |  10  |  
|  · Design   | · 具体设计  |  35  |  30  |  
|  · Coding   | · 具体编码  |  200  |  180  |  
|  · Code Review   | · 代码复审  |  60  |  60  |  
|  · Test   | · 测试（自我测试，修改代码，提交修改）  |  80  |  60  |  
|  Reporting   | 报告  |  50  |  80  |  
|  · Test Repor   | · 测试报告  |  35  |  20  |  
|  · Size Measurement   | · 计算工作量  |  25  |  20  |  
|  · Postmortem & Process Improvement Plan   | · 事后总结, 并提出过程改进计划  |  45  |  60  |  
|     | · 合计  |  900  |  895  |


# 拓展
1、尝试过许多种办法，包括利用jieba分词，余弦算出距离得出相似度，gensim.dictionary.doc2bow等等，但是结果过于夸张(接近1)感觉不对劲
且当用在更大的文本数据时，所耗费的时间占用的系统资源结果不理想，改用Levenshtein算法

2、对于Levenshtein动态规划
中文解析
![](https://img2020.cnblogs.com/blog/2148345/202009/2148345-20200924110513920-851484902.png)

3、通过多次复制粘贴（扩大数据）做对照试验可得出，Levenshtein距离算法相比其他算法对数据较大得优化处理得更快更好

'''
KNN算法的实现，首先将数据文件转化成txt文件，比较容易处理，通过查询微软的表格文档也是可以处理的
但是还要包含很多模块，配置环境比较复杂，所以这次就直接将表格导出为txt
'''

import codecs
from math import sqrt
from numpy import *

#将训练数据导入准备进行训练
def importData():
    with codecs.open('C:\\Users\\田宇\\Desktop\\实验3\\train.txt','r') as file:
        data=[]
        for i in range(0,200):
            d=file.readline().replace('\t',' ').replace('\n','')
            data.append(d)   

    return data

#进行训练  
def classify(testData,data,k):
    dist=[]
    #欧氏距离的计算
    for i in range(0,200):
        d0=data[i].split(' ')
        distance=sqrt((testData[0]-float(d0[0]))**2+(testData[1]-float(d0[1]))**2)
        dist.append(distance)

    sortedDistIndex = argsort(dist)

    #选择标签
    n1,n2=0,0
    for i in range(0,k):
        if sortedDistIndex[i] in range(100):
            n1+=1
        else:
            n2+=1

    if n1>n2:
        label0=1
    else:label0=2

    return label0

#将测试文件包含进去
t_data=[]
with codecs.open('C:\\Users\\田宇\\Desktop\\实验3\\test.txt','r') as f:
    for i in range(0,10):
        d=f.readline().replace('\t',' ').replace('\n','')
        t_data.append(d)

test=[]
for i in range(0,10):
    d0=t_data[i].split(' ')
    test.append(d0)
testData=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    testData[i]=[float(n) for n in test[i]]

#start test

data=importData()
for i in range(10):
    label0=classify(testData[i],data,5)
    print('testData:',testData[i],'label:',label0)


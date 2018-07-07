#这个脚本需要从头设计从遍历文件到计算tfidf的过程
#写一个函数A，对一个文件生成分词后的一行
#写一个函数B，输入是一行一行的文件的列表，输出是tfidf对象
#写一个函数，对A列表和B结果生成需要统计的东西
#比方说高tf-idf值的（关键词）低idf的（停用词、背景词）
#那么需要一个停用词集合（暂时不需要）
#输入是大学计算机基础吧

import codecs
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

dataPath = '../data/smk/'
lecName = '大学计算机基础'
suffix = '.seg2'

f1p = dataPath + lecName + suffix

def f2list(fp):
    #这个函数把fp这个文件中的每一行读出来
    #遇到====开头的时候就换一行，把现有字符串放进rst
    #====开头的也有用，也要存
    #记得结束的时候字符串里的东西要存
    lines = list(codecs.open(fp, "r", "utf-8"))
    prst = []
    crst = []

    str = ''
    for l in lines:
        if l.startswith('===='):
            if len(str):
                crst.append(str)
                str = ''
            prst.append(l)
        else:
            str += l.strip('\n')

    return prst, crst

p, r = f2list(f1p)
for i in p[:5]:
    print(i)
for i in r[:5]:
    print(i)


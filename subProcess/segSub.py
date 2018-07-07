#coding:utf-8

import os

import jieba

import sys


#这个脚本将递归地读取文件夹下的所有文件
#把一个句子写成一行
#把根目录和文件名区分开
#打印到根目录下,文件名+.txt的文件中

cn1 = '大学计算机基础'
cn2 = '大学物理'
cn3 = '高等数学一'
cn4 = '高等数学二'

rootdir = "../data/smk/"
# dirList = os.listdir(rootdir)

def segFile(inp, oup):
    lineArray = list(open(inp, "r").readlines());
    output = open(oup, 'w')
    i = 0

    for line1 in lineArray:
        i += 1
        if (i % 100 == 0):
            print("Jiebad " + str(i) + " sents in " + inp)
        if line1.startswith("===="):
            segLine = line1
        else:
            seg_list = jieba.cut_for_search(line1)
            segLine = " ".join(seg_list)
        output.write(segLine)

    output.close()


def main():

    segFile(rootdir + cn1 + '.txt2', rootdir + cn1 + '.seg2')
    segFile(rootdir + cn2 + '.txt2', rootdir + cn2 + '.seg2')
    segFile(rootdir + cn3 + '.txt2', rootdir + cn3 + '.seg2')
    segFile(rootdir + cn4 + '.txt2', rootdir + cn4 + '.seg2')




if __name__ == "__main__":
    main()






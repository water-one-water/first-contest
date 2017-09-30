import csv
import pymysql
import os
import re

#lines = [line.split(',') for line in open('matchDataTrain.csv',encoding='latin-1')]

#df = [[int(x) for x in line[:2]] for line in lines[1:]]

#ds = [[str(x)for x in line[2:3]] for line in lines[1:]]






def standard(filename):
    with open(filename, 'r',encoding = 'latin-1') as f1:
        temp = list(f1.readlines())
        first = [x.split(',') for x in temp]

#

        length = len(first[1])
        file = []

        for num in range(1, len(first)):
            # 去除数据中的噪点
            first[num][length - 1] = first[num][length - 1].replace('\n', '')

            file.append([int(item) for item in first[num]])
            # 将球队编号，球员编号化为整形
            #file[num - 1][0] = int(file[num - 1][0])
            #file[num - 1][1] = int(file[num - 1][1])
    return file

def win_rate(file):

    match_home = [0]*208
    match_total = [0]*208

    win_home   = [0]*208
    win_total  = [0]*208
    win_away = [0]*208
    for index in range(len(file)):
        match_home[file[index][0]] = match_home[file[index][0]] + 1
        match_total[file[index][1]] = match_total[file[index][1]] + 1

        if file[index][2]>file[index][3]:
            win_total[file[index][0]] = win_total[file[index][0]]+1
            win_away[file[index][0]] = win_away[file[index][0]]+1

        else:
            win_home[file[index][1]] = win_home[file[index][1]]+1

    win_rate_home = [0]*208
    win_rate_total = [0]*208
    win_rate_away = [0]*208

    for index in range(len(match_total)):
        if match_total[index]!=0:
            win_rate_total[index] = win_total[index]/match_total[index]
        else:
            index=index+1
        if match_home[index]!=0:
            win_rate_home[index] = win_home[index]/match_home[index]
        else:
            index = index + 1
        if (match_total[index]>match_home[index]):
            win_rate_away[index] = win_away[index]/(match_total[index]-match_home[index])
        else:
            index=index+1

    print(win_rate_total)
    print(win_rate_home)
    print(win_rate_away)





file=standard('matchDataTrain-simple.csv')
#print(file[0])
win_rate(file)

#print(file[0])
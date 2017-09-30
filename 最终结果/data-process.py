import csv
import pymysql
import os
import re
import numpy
# 整体结果均是基于teamData-simple

# 将数据标准化
def standard(filename):
    with open(filename, 'r',encoding='latin-1') as f1:
        temp = list(f1.readlines())
        first = [x.split(',') for x in temp]
        length = len(first[1])
        file = []

        for num in range(1, len(first)):
            # 去除数据中的噪点
            first[num][length - 1] = first[num][length - 1].replace('\n', '')
            first[num][length - 1] = first[num][length - 1].replace('#DIV/0!', '0')
            file.append([float(item) for item in first[num]])
            # 将球队编号，球员编号化为整形
            file[num - 1][0] = int(file[num - 1][0])
            file[num - 1][1] = int(file[num - 1][1])
    return file

# 计算单个球员的分数
def cal_score(player):
    time = (player[4] / 40.0) * 100  # 出场时间
    shot = (player[-1] / 0.7) * 100  # 投篮命中率
    point = (player[-2] / 30.0) * 100  # 得分
    block = (player[-3] / 2.0) * 100  # 盖帽
    backboard = (player[-4] / 15) * 100  # 篮板
    score = time * 0.1 + shot * 0.3 + point * 0.35 + block * 0.1 + backboard * 0.15
    return score

# 获得所有球员的分数
def memberScore(file):
    member = {}

    for player in file:
        teamNum = player[0]
        member.setdefault(teamNum, [])
        score = cal_score(player)
        member[teamNum].append(score)
    return member

#计算单个球员的重要程度
def cal_importance(player):
    showtime = (player[2] / 90) * 100
    first = (player[3] / 90) * 100
    time = (player[4] / 40) * 100
    score = showtime * 0.4 + first * 0.2 + time * 0.4
    return score


# 计算所有球员重要程度
def importance(file):
    important = {}
    for player in file:
        teamNum = player[0]
        important.setdefault(teamNum, [])
        score = cal_importance(player)
        important[teamNum].append(score)
    return important


# 根据球员重要程度给球员排序(由低到高)
def my_sort(memberScore, importance):
    for index in range(len(memberScore)):
        item1 = memberScore[index]
        item2 = importance[index]
        length = len(memberScore[index])

        for i in range(length - 1):
            for j in range(length - 1 - i):
                if item2[j] > item2[j + 1]:
                    temp = item2[j]
                    item2[j] = item2[j + 1]
                    item2[j + 1] = temp

                    temp = item1[j]
                    item1[j] = item1[j + 1]
                    item1[j + 1] = temp

        memberScore[index] = item1
        importance[index] = item2

# 计算球队实力
def teamScore(memberScore):
    teamPower = {}
    for index in range(len(memberScore)):
        temp1 = memberScore[index][-5:]
        temp2 = memberScore[index][-10:-5]
        score = (sum(temp1)/5.0)*1.2 + (sum(temp2)/5.0)*0.7
        teamPower[index] = score
    return teamPower


#测试
file = standard('/home/geniusrabbit/PycharmProjects/MyCode/SeedCup/teamData-simple.csv')
s1 = memberScore(file)
s2 = importance(file)
# print(s1[0])
my_sort(s1, s2)
# print(s1[2])
res = teamScore(s1)
#print(res)

def standard1(filename):
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

def win_rate(file,first):

    match_home = [0]*208
    match_away = [0]*208

    win_home   = [0]*208
    win_total  = [0]*208
    win_away = [0]*208
    for index in range(1,len(file)):
        match_home[file[index][0]] = match_home[file[index][0]] + 1
        match_away[file[index][1]] = match_away[file[index][1]] + 1

        if file[index][2]>file[index][3]:
            win_total[file[index][0]] = win_total[file[index][0]]+1
            win_away[file[index][0]] = win_away[file[index][0]]+1

        else:
            win_home[file[index][1]] = win_home[file[index][1]]+1

    win_rate_home = [0]*208
    win_rate_total = [0]*208
    win_rate_away = [0]*208

    for index in range(len(match_away)):
        if match_away[index]!=0:
            win_rate_total[index] = win_total[index]/match_away[index]
        else:
            index=index+1
        if match_home[index]!=0:
            win_rate_home[index] = win_home[index]/match_home[index]
        else:
            index = index + 1


    #print(win_rate_total)
    #print(win_rate_home)
    #print(win_rate_away)
    #print(file[0][0])


        rate = []
        # x=0.05
        for index in range(1,len(first)):
        #print(win_rate_home[file[index][1]])

            rate.append( 0.5 + (win_rate_home[first[index][1]]-win_rate_away[first[index][0]])*0.2+(res[first[index][1]]-res[first[index][0]])*0.02 )
       #rate[index] = 0.5 + (win_rate_home[file[index][1]]-win_rate_away[file[index][0]])+(res[file[index][1]]-res[file[index][0]])

    return rate



    #with open('test.csv', 'r', encoding='latin-1') as f2:





file1=standard1('matchDataTrain-simple.csv')
first=standard1('test.csv')
#print(file[0])
rate=win_rate(file1,first)

#print(file[0])
numpy.savetxt('result.csv', rate, delimiter=',')



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


def zhixin(file):
    rate [0]*300
    for index in range(300):
        rate[index]=0.5+(file[index][1])








file=standard('matchDataTrain-simple.csv')
zhixin(file)
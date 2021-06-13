from Vsual.vsual import chinaMap
from pandas import DataFrame
from pandas import read_table
from pandas import read_csv
import pandas
import numpy
import sys
sys.path.append('../Vsual/vsual.py')

collectTxt = read_table('../Collect/collect.txt',sep="\t",header=0)
collectCsv = read_csv('../Collect/collect.csv',sep=',',encoding='utf8',header=0,names=['单词','释义'])
direction = read_csv('../Collect/direction.csv',sep=',',encoding='utf8',header=0,names=['地区','报考人数'])

# 去除重复单词
collectCsv = collectCsv.drop_duplicates('单词')

# 去除重复地区
direction = direction.drop_duplicates('地区')

# 去除数据值为空的数据
collectCsv = collectCsv.dropna()
direction = direction.dropna()

# 报考地区总数
directionSum = direction.报考人数.count()

# 报考人数平均值
peopleAve = direction.报考人数.mean()

# 报考人数最少地区
peopleMin = direction.报考人数.min()

# 报考人数最多地区
peopleMax = direction.报考人数.max()

# 报考总人数
peopleSum = direction.报考人数.sum()

# 分组分析
# groupAnalyze = direction.groupby(by=['地区'])['报考人数'].agg({'报考地区总数': directionSum,'报考人数最少': peopleMin,'平均值':peopleAve,'报考人数最多':peopleMax,'报考总人数':peopleSum})

groupAnalyze = direction.groupby(['地区','报考人数'])['报考人数'].agg(['count'])

# 分布分析
bins = [peopleMin-1,15,30,peopleMax+1]
labels=['人数未到15万','15到30','人数超过30万']
人数分层 = pandas.cut(direction.报考人数,bins,labels=labels,right=False)
direction['人数分层'] = 人数分层
group = direction.groupby(['人数分层'])['地区'].agg([numpy.size])

# 数据抽取，将每个单词的首字母抽取出来
initial = collectCsv['单词'].str.slice(0,1)

# 单词总数
totalWord = initial.sum()

# 首字母为w的单词最多
maxWord = initial.max()

# 首字母为a的单词最少
minWord = initial.min()

chinaMap(direction)


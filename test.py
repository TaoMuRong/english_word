import numpy as np
from pandas import read_csv

direction = read_csv('test.csv',sep=',',encoding='utf8',header=0,names=['地区','报考人数'],index_col="报考人数")

y = direction.index
y = np.array(y)
x = np.array(direction).T
print(x.tolist())
import pandas as pd

'''创建一个Series对象'''
'''
创建Series时，主要使用Pandas的Series方法，语法如下：
s = pd.Series(data, index=index)
参数说明：
data: 表示数据，支持python字典、多维数组、标量值（即只有大小没有方向的量）。
index: 表示行标签（索引）
返回值：Series对象
说明：
当data参数是多维数组时，index长度必须与data长度一致。
如果没有指定index参数，将自动创建数值型索引（从0~data的数据长度减1）
'''
s1 = pd.Series([88, 60, 75])
s2 = pd.Series(5)
print(s2)

'''通过pandas引入Series对象'''
from pandas import Series
s3 = Series([88, 60, 75])
print(s3)

s4 = pd.Series([88, 60, 75], name='语文')  # Series也是可以有列名的
print(s4)

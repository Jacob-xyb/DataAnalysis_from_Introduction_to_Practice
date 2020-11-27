import pandas as pd

'''
DataFrame对象：
DataFrame是Pandas库中的一种数据结构，
它是由多种类型的列组成的二维表数据结构，
类似于Excel、SQL或Series对象构成的字典。
'''
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130]]
index = [0, 1, 2]
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
# df = pd.DataFrame(data=data, index=index)  # 列名不设置时，默认为RangeIndex
print(df)
# 遍历DataFrame表格数据的每一列
for col in df.columns:
    # print(col)  # col为一个个列名
    series = df[col]  # 将df一列变为Series
    print(series)

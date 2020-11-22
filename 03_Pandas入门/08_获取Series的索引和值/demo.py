import pandas as pd

s1 = pd.Series([88, 60, 75])
print(s1.index)  # 输出为：RangeIndex(start=0, stop=3, step=1)
print(s1.values)

s2 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
print(s2.index)  # 输出为：Index(['明日同学', '高同学', '七月流火'], dtype='object')
print(s2.values)

import pandas as pd

s1 = pd.Series([88, 60, 75])
print(s1)
print('===')
print(s1[0])  # 通过一个标签索引获取索引值

'''
注意：
Series对象不能使用[-1]定位索引。
'''

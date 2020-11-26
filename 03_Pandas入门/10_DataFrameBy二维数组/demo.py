import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130]]
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, columns=columns)
print(df)
print(df.transpose())

df_1 = pd.DataFrame(data=data)
print(df_1)

df_2 = pd.DataFrame(data)
print(df_2)
# df, df_1, df_2 结果形式是一样的 是将列表按照矩阵的形式输入dataframe

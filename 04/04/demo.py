import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
index = [1,2,3,4]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
# new = df.min()
#增加一行数据（语文、数学和英语的最小值,忽略索引）
# df = df.append(new,ignore_index=True)
print(df)

# 按列相加
# param：axis: =1,表示按行相加；=0，表示按列相加，默认=0
new = df.min(axis=1)
# print(new)
# 增加一列
df['min'] = new
print(df)

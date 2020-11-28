import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
name = ['明日', '七月流火', '高袁圆', '二月二']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print(df, '\n', '='*50)

"""按指定条件抽取数据"""
# print(df.loc[(df['语文'] > 105) & (df['数学'] > 88)])
# print(df.loc[(df['语文'] > 105) & (df['数学'] > 110)])
'''剖析过程'''
# print(df['语文'] > 105)       # 返回一个bool型的DataFrame
# print(df[df['语文'] > 105])   # 返回语文大于105的全部语数外成绩
# 意思就是说 df[] 可以接受一个列的bool型DataFrame。
# # print(df[[df['语文'] > 105, df['数学'] > 110]])  # ValueError: Item wrong length 2 instead of 4.
# # print(df[[df['语文'] > 105, df['数学'] > 88]])   # ValueError: Item wrong length 2 instead of 4.
# # print(df.loc[(df['语文'] > 105) and (df['数学'] > 110)])    # & 换成 and 也是不行的
# print(df.loc[(df['语文'] == 112) & (df['数学'] > 110)])         # == 等于判定也是成立的
# print(df.loc[(df['语文'] == 112) & (df['数学'] > 120)])         # Empty DataFrame 没有满足条件的不会报错
# # df1 = pd.DataFrame()
# # if df.loc[(df['语文'] == 112) & (df['数学'] > 120)] == df1:
# #     print("hello")
# #     # ValueError: Can only compare identically-labeled DataFrame objects

# print(df.loc[(df['语文'] > 105) & (df['数学'] > 88), ['语文', '数学']])  # 只提取了语文数学两列
# # 因为df.loc[(df['语文'] > 105) & (df['数学'] > 88)] == df.loc[(df['语文'] > 105) & (df['数学'] > 88), :]
# print(df[['语文', '数学']][(df['语文'] > 105) & (df['数学'] > 88)])  # 与前面结果相同，得出结论如下。
# # df.loc[(df['语文'] > 105) & (df['数学'] > 88), ['语文', '数学']] == df[['语文', '数学'][(df['语文'] > 105) & (df['数学'] > 88)]]
'''常用的条件判断(& | ~ ：与或非)'''
print(df.loc[(df['语文'] > 109) | (df['数学'] > 105)])  # | 或 满足其一即可
print(df.loc[~((df['语文'] > 109) | (df['数学'] > 105))])  # ~ 非 补集


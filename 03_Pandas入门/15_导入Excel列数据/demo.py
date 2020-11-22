import pandas as pd

'''
参数: 
usecols: int,list,字符串，默认为None.
    None: 解析所有列.
    int: 解析最后一列、  # 已失效
    

'''
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_excel('1月.xlsx', usecols=[0])                  # 通过指定列索引号导入第0列
# df1 = pd.read_excel('1月.xlsx', usecols=0)
# ValueError: Passing an integer for `usecols` is no longer supported.
#              Please pass in a list of int from 0 to `usecols` inclusive instead.
print(df1.head())
df1 = pd.read_excel('1月.xlsx', usecols=[0, 3])            # 通过指定列索引号导入第0列、第3列
print(df1.head())
df1 = pd.read_excel('1月.xlsx', usecols=['买家会员名', '宝贝标题'])   # 通过指定列名导入指定列
print(df1.head())

df2 = pd.read_excel('1月.xlsx', usecols='A:D')      # 包头包尾,连续3列
print(df2.head())

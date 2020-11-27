import pandas as pd

'''
同样是用pandas.read_csv导入.txt
但是需要指定sep参数(如制表符\t)
'''

# 设置数据显示的列数和宽度
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_csv('../../data/0317.txt', sep='\t', encoding='gbk')
# df1 = pd.read_csv('1月.txt', encoding='gbk')  # 不指定sep就会全部贴在一起
print(df1.head())

df2 = pd.read_csv('../../data/0317.txt', sep='\t', encoding='gbk', header=None)
print(df2.head())

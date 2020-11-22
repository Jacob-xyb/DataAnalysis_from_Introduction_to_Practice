import pandas as pd       # 导入pandas模块

'''解决数据输出时列名不对齐的问题'''
pd.set_option('display.unicode.east_asian_width', True)  # 列名对齐
# pd.set_option('display.unicode.ambiguous_as_wide', True)
'''行列显示不全'''
# pd.set_option('display.max_rows', 1000)  # 修改默认输出最大行数
# pd.set_option('display.max_columns', 1000)  # 修改默认输出最大列数

df = pd.read_excel(r'..\..\data\0301.xlsx')  # 读取Excel文件
print(df.head())  # 显示前5条数据
# print(df)

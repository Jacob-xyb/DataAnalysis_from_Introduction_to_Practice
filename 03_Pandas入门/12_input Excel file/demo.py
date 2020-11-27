import pandas as pd

"""语法参数说明"""
'''
pd.read_excel(io,sheet_name=0,header=0,names=None)
Args:
    io: 字符串，xls或xlsx文件路径或类文件对象.
    sheet_name: 获取工作表，默认值为0.
            sheet_name=[0,1,'Sheet3'] 第一个，第二个和名为'Sheet3'的Sheet页.
    header: 指定作为列名的行，默认值为0.数据为除列名以外的数据，设置header=None(此时列索引为数字).
    names: 默认值为None,要使用的列名列表.
    index_col: 指定列为索引列，默认值为None，索引0是DataFrame对象的行标签。
    usecols: int,list,字符串，默认为None.
            None: 解析所有列.
            int: 解析最后一列、  # 已失效!!!  # 必须是[int]
            list: 解析列号和列表的列。
            str: "A:E" or "A,C,E:F"     # 范围包括前后
'''
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel(r'..\..\data\0312.xlsx')
print(df.head(), '\n', "="*50)  # 输出前5条数据
"""================================================================================================================"""
'''sheet_name'''
# 获取工作表，默认值为0.
# sheet_name=[0,1,'Sheet3'] 第一个，第二个和名为'Sheet3'的Sheet页.
# df1= pd.read_excel(r'..\..\data\0312.xlsx',sheet_name=[0, "明日"])  # sheet为多页时 输出成字典类型
# print(df1, '\n')  # 输出前5条数据

'''names'''
# df2 = pd.read_excel(r'..\..\data\0312.xlsx', names=[0, 1, 2, 3])  # names会直接覆盖excel第0行
# print(df2.head())
# df2_1 = pd.read_excel(r'..\..\data\0312.xlsx', names=[0, 1, 2, 3], header=None)  # header=None 就不会覆盖了
# print(df2_1.head())

'''header'''
# header: 指定作为列名的行，默认值为0.数据为除列名以外的数据，设置header=None(此时列索引为数字).
# names: 默认值为None,要使用的列名列表.
# df3 = pd.read_excel(r'..\..\data\0312.xlsx', header=None)  # 列索引为数字 # 相当于保留了第一行
# print(df3.head())
# df3_1 = pd.read_excel(r'..\..\data\0312.xlsx', header=2)    # 设置第2行为列索引 # 前面的行就没有了
# print(df3_1.head())

# 通过索引快速检索数据
# print(df3_1[0])
# print(df3_1.loc['mrhy1'])
'''index_col'''
# index_col: 指定列为索引列，默认值为None，索引0是DataFrame对象的行标签。
# df4 = pd.read_excel(r'..\..\data\0312.xlsx', index_col=0)       # 设置“买家会员名”为行索引
# print(df4.head())
# df4_1 = pd.read_excel(r'..\..\data\0312.xlsx', index_col=1)     # 不会覆盖其他列
# print(df4_1.head())
# df4_2 = pd.read_excel(r'..\..\data\0312.xlsx', header=None, index_col=1)        # header 优先级比index_col高
# # header 和 index_col 一起用格式就会比较混乱
# print(df4_2.head())

'''usecols'''       # 输出指定列
# df5 = pd.read_excel(r'..\..\data\0312.xlsx', usecols=[2])
# # ValueError: Passing an integer for `usecols` is no longer supported.
# #              Please pass in a list of int from 0 to `usecols` inclusive instead.
# df5 = pd.read_excel(r'..\..\data\0312.xlsx', usecols='C')
# df5 = pd.read_excel(r'..\..\data\0312.xlsx', usecols='收货人姓名')       # 错误的写法
# df5 = pd.read_excel(r'..\..\data\0312.xlsx', usecols=['收货人姓名'])       # 正确的写法
# print(df5.head())

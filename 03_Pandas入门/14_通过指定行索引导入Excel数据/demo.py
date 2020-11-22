import pandas as pd

'''
pd.read_excel(io,sheet_name=0)
Args:
    io: 字符串，xls或xlsx文件路径或类文件对象.
    sheet_name: 获取工作表，默认值为0.
        sheet_name=[0,1,'Sheet3'] 第一个，第二个和名为'Sheet3'的Sheet页.
    header: 指定作为列名的行，默认值为0.数据为除列名以外的数据，设置header=None.
    name: 默认值为None,要使用的列名列表.
'''
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_excel('1月.xlsx', index_col=0)  # 设置“买家会员名”为行索引
print(df1.head())                            # 输出前5条数据
df2 = pd.read_excel('1月.xlsx', header=1)    # 设置第1行为列索引
print(df2.head())
df3 = pd.read_excel('1月.xlsx', header=None)  # 列索引为数字
print(df3.head())
# 通过索引快速检索数据
print(df3[0])
print(df1.loc['mrhy1'])

df4 = pd.read_excel('1月 - 副本.xlsx', index_col=0)  # 设置“买家会员名”为行索引
print(df4.head())                                   # 输出前5条数据


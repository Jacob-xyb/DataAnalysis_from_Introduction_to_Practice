import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel('1月.xlsx')
print(df.head(), '\n')  # 输出前5条数据

'''
pd.read_excel(io,sheet_name=0,header=0,names=None)
Args:
    io: 字符串，xls或xlsx文件路径或类文件对象.
    sheet_name: 获取工作表，默认值为0.
        sheet_name=[0,1,'Sheet3'] 第一个，第二个和名为'Sheet3'的Sheet页.
    header: 指定作为列名的行，默认值为0.数据为除列名以外的数据，设置header=None(此时列索引为数字).
    names: 默认值为None,要使用的列名列表.
'''

# test
# df1 = pd.read_excel('1月.xlsx', sheet_name=[0, 2])
# print(df1)  # 输出是一个字典

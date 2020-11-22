import pandas as pd

'''
pandas.read_csv(filepath_or_buffer,encoding=None)
    filepath_or_buffer: 字符串，文件路径，也可以是URL链接.
    encoding: 字符串，默认值为None，文件的编码格式.
'''

# 设置数据显示的最大列数和宽度
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_csv('1月.csv', encoding='gbk')  # 导入csv文件，并指定编码格式
print(df1.head())  # 输出前5条数据

'''
注意：python常用的编码格式是UTF-8和GBK格式，默认编码格式为UTF-8。
导入.csv文件时，需要通过encoding参数指定编码格式。
当我们将Excel文件另存为.csv文件时，默认编码格式为GBK。
因此导入.scv文件时，需要保持编码格式保持一致。
'''

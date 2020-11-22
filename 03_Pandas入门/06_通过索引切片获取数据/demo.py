import pandas as pd

# 用标签索引做切片，包头包尾
pd.set_option('display.unicode.east_asian_width', True)  # 列名对齐
s1 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
print(s1['明日同学':'七月流火'])  # 通过切片获取索引值


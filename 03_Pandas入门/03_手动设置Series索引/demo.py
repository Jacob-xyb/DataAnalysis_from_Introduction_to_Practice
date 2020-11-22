import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)  # 列名对齐
s1 = pd.Series([88, 60, 75], index=[1, 2, 3])
s2 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
print(s1)
print(s2)

'''
说明：
结果中输出的dtype，是DataFrame数据的数据类型，int为整型，后面的数字表示位数。
'''

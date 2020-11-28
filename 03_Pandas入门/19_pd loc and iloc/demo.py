import pandas as pd

'''
loc是指location的意思，iloc中的i是指integer。这两者的区别如下：
loc：works on labels in the index.
iloc：works on the positions in the index (so it only takes integers).
也就是说loc是根据index来索引，比如下边的df定义了一个index，那么loc就根据这个index来索引对应的行。
iloc并不是根据index来索引，而是根据行号来索引，行号从0开始，逐次加1。
'''
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
name = ['明日', '七月流火', '高袁圆', '二月二']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
print(df, '\n', '='*50)
print(df.loc['明日'])
print(df.iloc[0])

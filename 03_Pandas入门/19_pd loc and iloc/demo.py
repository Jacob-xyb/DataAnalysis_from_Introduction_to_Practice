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


"""抽取行"""
'''抽取多行'''
# print(df.loc[['明日', '高袁圆']])        # == print(df.iloc[[0, 2]])
'''连续抽取指定列'''
# print(df.loc['明日':'高袁圆'])        # == print(df.iloc[0:2])
# print(df.loc[:'高袁圆'])       # 从第一行到'高袁圆'  # == print(df.loc[:'高袁圆':]) == print(df.loc[:'高袁圆':1])
# print(df.loc[:'高袁圆':1])       # 1是步长

"""抽取列"""
'''直接使用列名'''
# print(df[['语文', '数学']])
# print(df['语文'])     # 可直接输出列名，但是df['语文':'英语']报错
# # print(df[0])        # 不能直接用列号输出，会报错，但是iloc可以。
'''使用loc和iloc'''
# 第一个参数代表行，第二个参数代表列，指定列抽取时，行参数不能省略。
# print(df.loc[:, ['语文', '数学']])      # 抽取'语文'和'数学'
# print(df.iloc[:, [0, 1]])     # 抽取第1列和第2列
# print(df.loc[:, '语文':])     # 抽取从“语文”开始到最后一列
# print(df.iloc[:, :2])        # 连续抽取从1列开始到第3列
# print(df.iloc[:, -1:100])       # iloc列参数也是可以超出范围的，输出了英语一个列

"""抽取行列"""
# print(df.loc['七月流火', '英语'])              # “英语”成绩
# # 由于df.loc['七月流火', '英语']没有使用[]，导致输出的数据不是DataFrame对象
# print(df.iloc[1, 2])        # 输出的也是'七月流火'的英语成绩
# print(df.iloc[[1, 2]])      # 输出的就是'七月流火', '高袁圆'两行的成绩
# exit()
# print(df.iat[1, 2], type(df.iat[1, 2]))     # 抽取其中一个元素                # numpy.float64对象，浮点数
# # !!print(df.iat['七月流火', '英语'], type(df.iat[1, 2]))
# # ValueError: iAt based indexing can only have integer indexers
# print(df.loc['七月流火', '英语'], type(df.loc['七月流火', '英语']))          # numpy.float64对象，浮点数
# print(df.loc[['七月流火'], '英语'], type(df.loc[['七月流火'], '英语']))      # Series对象，标签在'七月流火'上
# print(df.loc['七月流火', ['英语']], type(df.loc[['七月流火'], '英语']))      # Series对象，标签在'英语'上
# exit()
print(df.loc[['七月流火'], ['数学', '英语']])         # “七月流火”的“数学”和“英语”成绩
print(df.iloc[[1], [2]])                            # 第2行第3列
print(df.iloc[1:, [2]])                             # 第2行到最后一行的第3列
print(df.iloc[1:, [0, 2]])                          # 第2行到最后一行的第1列和第3列
print(df.iloc[:, 2])                                # 所有行，第3列

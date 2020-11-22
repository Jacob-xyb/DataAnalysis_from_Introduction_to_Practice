import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.DataFrame({'原日期':['14_通过指定行索引导入Excel数据-Feb-20', '02_创建一个Series对象/14_通过指定行索引导入Excel数据/2020', '2020.02_创建一个Series对象.14_通过指定行索引导入Excel数据', '2020/02_创建一个Series对象/14_通过指定行索引导入Excel数据','20200214']})
df['转换后的日期']=pd.to_datetime(df['原日期'])
print(df)


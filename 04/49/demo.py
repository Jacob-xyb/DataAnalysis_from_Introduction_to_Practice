import pandas as pd
index = pd.date_range('02_创建一个Series对象/02_创建一个Series对象/2020', periods=9, freq='T')
series = pd.Series(range(9), index=index)
print(series)
print(series.resample('3T').sum())

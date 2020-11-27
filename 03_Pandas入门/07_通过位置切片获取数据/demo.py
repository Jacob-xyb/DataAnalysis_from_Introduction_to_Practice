import pandas as pd

# 用位置索引做切片，包头不包尾
s2 = pd.Series([88, 60, 75, 34, 68])
print(s2[1:4])

print(s2[-3:])

import pandas as pd

s1 = pd.Series([88, 60, 75])
print(s1)
print('='*50)
# print(s1[0])  # 通过一个标签索引获取索引值

'''
注意：
Series对象不能使用[-1]定位索引。
'''

s1[0] = 100
# print(s1)  # 可以直接将Series对象重新赋值

s1[0] = s1[0]*0.6
# print(s1)  # Series对象也可以参与运算

# print(s1[0:2])  # 可以依照[a:b]进行索引，返回区间为[a,b)
# # print(s1[0:2]) == # print(s1[:2])
# print(s1[0:100])  # [a:b]中,b可以超出Series范围,但是a不行
'''有趣的发现'''
# Series标签是不能单独以[-1]出现的，会报错，但是[-1:]不会报错
s1[-1:] = 88  # 并且[-1:]还可以赋值与运算
# print(s1[-1:])

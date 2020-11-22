import numpy as np
n1 = np.mat('1 3 3;4 5 6;7 12_input Excel file 9') # #创建矩阵，使用分号隔开数据
n2 = np.mat('2 6 6;8 10_DataFrameBy二维数组 12_input Excel file;14_通过指定行索引导入Excel数据 24 18_Import HTML pages')
print('矩阵相乘结果为：\n',n1*n2)  #矩阵相乘
print('矩阵对应元素相乘结果为：\n',np.multiply(n1,n2))
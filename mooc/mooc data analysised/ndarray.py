import numpy as np;
#ndarray的创建

#从列表元组创建ndarray
x = np.array([0, 1, 2, 3])#列表中创建
print('列表中创建:', x)
x = np.array((4, 5, 6, 7))#元组中创建
print('元组中创建:', x)
x = np.array([[1, 2], [9, 8], (0.1, 2.0)])
print('混合创建：')
print(x)

x = np.arange(10)
print('输出从0-n-1   arrange(10):')
print(x)

x = np.ones((3, 6))
print('根据shape（元组类型）生成一个全1数组 ones(3,6):')
print(x)

x = np.zeros((3, 6), dtype=np.int32)
print('根据shape（元组类型）生成一个全0数组 zeros((3, 6):')
print(x)

x = np.eye(5)
print('根据shape（元组类型）生成对角线为1的矩阵 eye(5):')
print(x)

x = np.ones((2, 3, 4))
print('最外层两个元素 ones((2, 3, 4)):')
print(x)

#用函数创建ndarray(ones_like(a),zeros)

a = np.linspace(1, 10, 4)
print('1到10中生成4个元素:')
print(a)

b = np.linspace(1, 10, 4, endpoint=False)
print('最后一个元素不为10：')
print(b)

c = np.concatenate((a, b))
print('合并')
print(c)

#数组的维度变换
a = np.ones((2, 3, 4), dtype=np.int32)
print('维度变换：')
print(a.reshape((3, 8)))#不改变原数组，返回
a = np.ones((2, 3, 4), dtype=np.int32)
print('维度变换：')
print(np.resize(a, (3, 8)))#直接改变原数组
a = np.ones((2, 3, 4), dtype=np.int32)
print('降维数组：')
print(a)
print(a.flatten())

#数组类型变换
a = np.ones((2, 3, 4), dtype=np.int)
print(a)
b = a.astype(np.float)
print('astype（）方法创建新数组（原始数据的一个拷贝），即两个类型一致')
print(b)
print("\n")

#数组向列表转换
a = np.full((2, 3, 4), 25, dtype=np.int32)
print("数组向列表转换:")
print(a)
print("\n")
print(a.tolist())
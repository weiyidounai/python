import numpy as np;

#数组的索引和切片
a = np.array([9, 8, 7, 6, 5])
print('a[2]:', a[2])
print('a[1:4:2]:array', a[1:4:2])
print('\n')
a = np.arange(24).reshape((2, 3, 4))
print('多维数组索引')
print(a)
print('a[1, 2, 3]:', a[1, 2, 3])
print('a[0, 1, 2]:', a[0, 1, 2])
print('a[-1, -2, -3]:', a[-1, -2, -3])
print('\n')
#多维数组的切片
a = np.arange(24).reshape((2, 3, 4))
print('a[:, 1, -3]:')
print(a[:, 1, -3])
print('a[:, 1:3, :]:' )
print(a[:, 1:3, :])
print('a[:, :, ::2(步长）]:')
print(a[:, :, ::2])
print('\n')

#数组与标量之间的计算
a = np.arange(24).reshape((2, 3, 4))
print('a.mean')
print(a/a.mean())
print('\n')

#一元函数
a = np.arange(24).reshape((2, 3, 4))
print(a)
print('square')
a = np.square(a)
print(a)
a = np.sqrt(a)
print('sqrt')
print(a)
a = np.modf(a)
print('modf')
print(a)

#二元函数
a = np.arange(24).reshape((2, 3, 4))
b = np.sqrt(a)
print(b.size, b.shape, b.ndim, b.itemsize)
print('a')
print(a)
print('b')
print(b)
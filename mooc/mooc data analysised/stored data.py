import numpy as np;

# CSV文件（是存储文件的一种格式）只能存储一维和二维数组
# np.savetxt(fram(文件、字符串、产生器如.gz  .bz2),array,fmt='%.18e'（文件格式）,delimiter=None（分割字符串默认空格）)
a = np.arange(100).reshape(5, 20)
np.savetxt('a.csv', a, fmt='%1f', delimiter=',')
b = np.loadtxt('a.csv', dtype=np.int,  delimiter=',')
print(b)
print('\n')
#任意维度的存取
a = np.arange(100).reshape(5, 10, 2)
print(a)
a.tofile("b.dat", sep=",", format='%d')
#从文本文件或者二进制文件还原数据
c = np.fromfile("b.dat", dtype=np.int, sep=",").reshape(5, 10, 2)#w文本
print('c:')
print(c)
c = np.fromfile("b.dat", )
print('\n')
#便捷文件存取
a = np.arange(100).reshape(5, 10, 2)
np.save("a.npy", a)
b = np.load("a.npy")
print("便捷文件存取:\n")
print(b)

# 随机数函数
a = np.random.rand(3, 4, 5)
print("随机函数：\n")
print(a)
print('\n')
b = np.random.randint(100, 200, (3, 4))
print(b)
np.random.seed(10)#数组不变
print(np.random.randint(100, 200, (3, 4)))


a = np.random.randint(100, 200, (3, 4))
print(a)
print('\n')
print('根据数组的第一轴进行随排序，改变数组a')
np.random.shuffle(a)
print(a)
print('\n')
print(a)

a = np.random.randint(100, 200,(3, 4))
print(a)
np.random.permutation(a)
print('根据数组a的第一轴产生一个新的乱序数组，不改变数组')
print(a)
print('\n')
print(a)

choice
b = np.random.randint(100, 200, (8,))
print(b)
print(np.random.choice(b, (3, 2)))
print(np.random.choice(b, (3, 2), replace=False))
print(np.random.choice(b, (3, 2), p=b/np.sum(b)))

#uniform normal poisson
u = np.random.uniform(0, 10, (3, 4))
print(u)
n = np.random.normal(1, 5, (2, 3))
print(n)


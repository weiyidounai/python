import numpy as np;


#梯度(连续值之间的变化率即斜率）函数np.gradient(f)p.gradient(a) ： 计算数组a中元素的梯度，f为多维时，返回每个维度的梯度
# 离散梯度： xy坐标轴连续三个x轴坐标对应的y轴值：a, b, c 其中b的梯度是（c-a）/2 而c的梯度是： (c-b)/1
# 当为二维数组时，np.gradient(a) 得出两个数组，第一个数组对应最外层维度的梯度，第二个数组对应第二层维度的梯度。
a = np.random.randint(1, 20, (5))
print(a)
print('gardient', np.gradient(a))
b = np.random.randint(0, 20, (5))
print(b)
print('gardient', np.gradient(b))
print('\n')
#二维
c = np.random.randint(0, 50, (3, 5))
print(c)
print('gardient')
print(np.gradient(c))





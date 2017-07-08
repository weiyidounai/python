import numpy as np;
# from scipy.sparse import csr_matrix
#
# indptr = np.array([0, 2, 3, 6])
# indices = np.array([0, 2, 2, 0, 1, 2])
# data = np.array([1, 2, 3, 4, 5, 6])
# a = csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
# print(a)

# numpy的统计函数
# sum(a, axis = None) : 依给定轴axis计算数组a相关元素之和，axis为整数或者元组
# mean(a, axis = None) : 同理，计算平均值
# average(a, axis =None, weights=None) : 依给定轴axis计算数组a相关元素的加权平均值
# std（a, axis = None） ：同理，计算标准差
# var（a, axis = None）: 计算方差
# eg： np.mean(a, axis =1) ： 对数组a的第二维度的数据进行求平均
# a = np.arange(15).reshape(3, 5)
# np.average(a, axis =0, weights =[10, 5, 1]) : 对a第一各维度加权求平均，weights中为权重，注意要和a的第一维匹配
#
# min(a) max(a) : 计算数组a的最小值和最大值
# argmin(a) argmax(a) : 计算数组a的最小、最大值的下标（注：是一维的下标）
# unravel_index(index, shape) : 根据shape将一维下标index转成多维下标
# ptp(a) : 计算数组a最大值和最小值的差
# median(a) : 计算数组a中元素的中位数（中值）
# eg：a = [[15, 14, 13],
# [12, 11, 10] ]
# np.argmax(a) –> 0
# np.unravel_index( np.argmax(a), a.shape) –> (0,0)
#mean根据给定轴axis计算数组a相关元素的期望axis整数和元组
# a = np.arange(15).reshape(3, 5)
# print(a)
# print('sum', np.sum(a))
# print('mean', np.mean(a, axis=1))#axis=0，那么输出矩阵是1行，求每一列的平均（按照每一行去求平均）；axis=1，输出矩阵是1列，求每一行的平均（按照每一列去求平均）。还可以这么理解，axis是几，那就表明哪一维度被压缩成1。
# print('mean', np.mean(a, axis=0))
# print('averge', np.average(a, axis=0, weights=[10, 5, 1]))

a = np.arange(15, 0, -1).reshape(3, 5)
print(a)
print('max', np.max(a))
print('argmax',np.argmax(a))#扁平化后的下标
print('unravel_index', np.unravel_index(np.argmax(a), a.shape))#重塑成多维下标
print('ptp', np.ptp(a))#max-min
print('median', np.median(a))
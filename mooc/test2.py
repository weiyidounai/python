import random
import numpy as np;
from scipy.sparse import csr_matrix
from scipy import *
import time

#加载train数据集，转化为矩阵形式
def load_trainmatrix(filename,num_users,num_items):
    t0 = time.time()
    counts = np.zeros((num_users, num_items))
    total = 0.0
    num_zeros = num_users * num_items
    for i, line in enumerate(open(filename, 'r')):
        u_train, i_train, c_train = line.strip().split(',')
        u_train = int(u_train)
        i_train = int(i_train)
        c_train = float(c_train)
        if u_train >= num_users:
            continue
        if i_train >= num_items:
            continue
        if c_train != 0:
            counts[u_train, i_train] = c_train
            total += c_train
            num_zeros -= 1
        if i % 1000 == 0:
            print('loaded %i counts...' % i)
    counts = csr_matrix(counts)
    t1 = time.time()
    print('Finished loading matrix in %f seconds' % (t1 - t0))
    return counts

R = load_trainmatrix('D:\PycharmProjects\movielenswash_train.txt', 80472, 3)

# data = [[5.0, 3.0, 0.0, 1.0],
#         [4.0, 0.0, 0.0, 1.0],
#         [1.0, 1.0, 0.0, 5.0],
#         [1.0, 0.0, 0.0, 4.0],
#         [0.0, 1.0, 5.0, 4.0]]


# lines = open('D:\PycharmProjects\movielenswash_train.txt').readlines()  #打开文件，读入每一行
# fp = open('D:\PycharmProjects\movielenswash_train.txt', 'w')  #打开你要写得文件test2.txt
# for s in lines:
# # replace是替换，write是写入
#     fp.write(s.replace(',', ' '))
#     fp.close()  # 关闭文件


# strip(rm)：删除s字符串中开头、结尾处，rm字符。当rm为空时默认删除空白符（包括'\n', '\r',  '\t',  ' ')
# split(del)：通过指定分隔符（del）对字符串进行切片，如果参数num有指定值，则仅分隔num个子字符串。
# file = open("D:\PycharmProjects\movielenswash_train.txt", "r")
# list_arr = file.readlines()
#
# lists = []
#
# for index, x in enumerate(list_arr):
#     x = x.strip('\n')
#     x = x.split(",")
#     lists.append(x)
#
# a = np.array(lists)
# a = a.astype(int)
# print(a)
#
# data = a
# R = np.mat(data)
#找到分解后矩阵的行列
K = 2
# item_number = len(R[0])#输出矩阵的列
# user_number = len(R) #输出矩阵的行
item_number = R.shape[1]#输出矩阵的列
user_number = R.shape[0]#输出矩阵的行
#定义分解后的两个矩阵P(user_k)Q(k_item)
P = np.zeros((user_number, K))
Q = np.zeros((K, item_number))

#初始化P,Q矩阵i行j列
for i in range(user_number):
    for j in range(K):
        P[i, j] = random.uniform(0, 1)

for i in range(K):
    for j in range(item_number):
        Q[i, j] = random.uniform(0, 1)

#损失函数
steps = 0.0
loss = 40.0
loss_value = 0.001
alpha = 0.02
beta = 0.02
predict_R = np.zeros((user_number, item_number))
rmse = 0

while steps < 50000 and loss > loss_value:
    loss = 0
    predict_R = np.dot(P, Q)
    eij = R - predict_R
    for i in range(user_number):
        for j in range(item_number):

            loss += eij[i, j]
            print("loss^2:", loss * loss)
            rmse = np.sqrt(eij[i, j] * eij[i, j] / (i+j+1))

    predict_R = np.dot(P, Q)
    # 更新P和Q矩阵
    for i in range(user_number):
        for j in range(item_number):
            for k in range(K):
                P[i, k] += alpha*(2*eij[i, j]*Q[k, j] - beta*P[i, k])
                Q[k, j] += alpha*(2*eij[i, j]*P[i, k] - beta*Q[k, j])

    steps += 1

predict_R = np.dot(P, Q)
print("均方根误差（RMSE）：", rmse)
print(predict_R)

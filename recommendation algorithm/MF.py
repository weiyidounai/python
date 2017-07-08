import random

import numpy as np;


data = [[5.0, 3.0, 0.0, 1.0],
        [4.0, 0.0, 0.0, 1.0],
        [1.0, 1.0, 0.0, 5.0],
        [1.0, 0.0, 0.0, 4.0],
        [0.0, 1.0, 5.0, 4.0]]

# # R = np.matrix(data)
# f = open('D:\PycharmProjects\movielenswash_train.txt')
# data = f.read()
R = np.matrix(data)
#找到分解后矩阵的行列
K = 2
item_number = R.shape[1]#输出矩阵的列
user_number = R.shape[0]#输出矩阵的行

#定义分解后的两个矩阵P(user_k)Q(k_item)
P = np.zeros((user_number, K))
Q = np.zeros((K, item_number))

#初始化P,Q矩阵i行j列
for i in range(user_number):
    for j in range(K):
        P[i, j] = random.uniform(0, 1)
print("初始化分解后的用户矩阵：")
print(P)
for i in range(K):
    for j in range(item_number):
        Q[i, j] = random.uniform(0, 1)
print("初始化分解后的物品矩阵：")
print(Q)
#损失函数
steps = 0
loss = 50.0
loss_value = 0.001
alpha = 0.001
beta = 0.01
predict_R = np.zeros((user_number, item_number))
rmse = 1
while steps < 50000 and loss > loss_value:
    loss = 0
    predict_R = np.dot(P, Q)
    eij = R - predict_R
    for i in range(user_number):
        for j in range(item_number):
            if R[i, j] != 0:
                loss += eij[i, j]
                rmse = np.sqrt(eij[i, j] * eij[i, j] / (i+j+1))
    print("loss^2:", loss*loss)
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
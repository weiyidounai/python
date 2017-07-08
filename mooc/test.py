import random
import numpy as np;

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
# print(a)
#
# data = a
# R = np.mat(data)



file = open("D:\PycharmProjects\movielenswash_train.txt")

for line in file:
    data = line
    R = np.mat(data)
    K = 2
    item_number = len(R[0])  # 输出矩阵的列
    user_number = len(R)  # 输出矩阵的行

    # 定义分解后的两个矩阵P(user_k)Q(k_item)
    P = np.zeros((user_number, K))
    Q = np.zeros((K, item_number))

    # 初始化P,Q矩阵i行j列
    for i in range(user_number):
        for j in range(K):
            P[i, j] = random.uniform(0, 1)

    for i in range(K):
        for j in range(item_number):
            Q[i, j] = random.uniform(0, 1)

    # 损失函数
    steps = 0.0
    loss = 50.0
    loss_value = 0.01
    alpha = 0.02
    beta = 0.01
    predict_R = np.zeros((user_number, item_number))
    rmse = 0

    while steps < 50000 and loss > loss_value:
        loss = 0
        predict_R = np.dot(P, Q)
        eij = R - predict_R
        for i in range(user_number):
            for j in range(item_number):
                if R[i, j] != 0:
                    loss += eij[i, j]
                    print("loss^2:", loss * loss)
                    rmse = np.sqrt(eij[i, j] * eij[i, j] / (i + j + 1))

        predict_R = np.dot(P, Q)
        # 更新P和Q矩阵
        for i in range(user_number):
            for j in range(item_number):
                for k in range(K):
                    P[i, k] += alpha * (2 * eij[i, j] * Q[k, j] - beta * P[i, k])
                    Q[k, j] += alpha * (2 * eij[i, j] * P[i, k] - beta * Q[k, j])

        steps += 1

    predict_R = np.dot(P, Q)
    print("均方根误差（RMSE）：", rmse)
    print(predict_R)





# f = open("D:\PycharmProjects\movielenswash_train.txt")             # 返回一个文件对象
# data = f.readline()             # 调用文件的 readline()方法
# while data:
#     print(data)                 # 后面跟 ',' 将忽略换行符
#     data = f.readline()
#
# data = np.array(data)
#找到分解后矩阵的行列

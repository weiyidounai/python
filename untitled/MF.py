import random

import numpy as np;

#
# data = [[5.0, 3.0, 0.0, 1.0],
#         [4.0, 0.0, 0.0, 1.0],
#         [1.0, 1.0, 0.0, 5.0],
#         [1.0, 0.0, 0.0, 4.0],
#         [0.0, 1.0, 5.0, 4.0]]
#
# data_mat = np.matrix(data)
file = open("D:\PycharmProjects\movielenswash_train.txt", "r")
list_arr = file.readlines()

lists = []

for index, x in enumerate(list_arr):
    x = x.strip('\n')
    x = x.split(",")
    lists.append(x)

a = np.array(lists)
a = a.astype(int)
print(a)



data = a
data_mat = np.mat(data)
#定义属性数量，确定分解后矩阵大小
factor_number = 2
item_number = len(data[0])
user_number = len(data[:])

#定义分解后的矩阵
user_preference = np.zeros((user_number, factor_number))
character_item = np.zeros((factor_number, item_number))

#初始化分解后的矩阵
for i in range(user_number):
    for j in range(factor_number):
        user_preference[i][j] = random.uniform(0, 1)

for i in range(factor_number):
    for j in range(item_number):
        character_item[i, j] = random.uniform(0, 1)

#迭代次数
iters = 1
#学习率
learning_rate = 0.01
#预测m
loss = 50.0
eps = 0.0001
predict_item = np.zeros((user_number, item_number))
while iters < 50000 and loss > eps:
    loss = 0
    predict_item = np.dot(user_preference, character_item)
    error = data_mat - predict_item
    for i in range(user_number):
        for j in range(item_number):
            if data_mat[i, j] != 0:
                loss += error[i, j]
    print(loss*loss)
    #更新user_preference和character_item矩阵
    for i in range(user_number):
        for j in range(item_number):
            for k in range(factor_number):
                    if data_mat[i, j] != 0:
                        user_preference[i, k] += 2*learning_rate*(error[i, j]*character_item[k, j])
                        character_item[k, j] += 2*learning_rate*(error[i, j]*user_preference[i, k])
    iters += 1

predict_item = np.dot(user_preference, character_item)

print(predict_item)



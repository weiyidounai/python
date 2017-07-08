# import random
#
# #随机梯度下降y=theta0+theta1x  设置为y=3+2x
# x = [1, 2, -2, 5, -3]
# y = [5, 7, -1, 13, -3]
# loss = 50
# iters = 0
# theta0 = random.randint(0, 5)
# theta1 = random.randint(0, 5)
# a = 0.01#步长
# diff = 50
# print("theta0,theta1:", theta0, theta1)
#
# while loss > 0.001 and iters < 50000:
#
#     diff = 0
#     loss = 0
#     for i in range(len(x)):
#         diff = y[i]-(theta1 * x[i] + theta0)
#         loss += pow(diff, 2)/2
#         print("loss:", loss)
#
#         theta0 += a * diff * x[i]
#         theta1 += a * diff * x[i]
#         iters += 1
# print("theta0,theta1:", theta0, theta1)

import random
# matrix_A  训练集y = theta1*x1 +theta2*x2
matrix_A = [[1,4], [2,5], [5,1], [4,2]]
Matrix_y = [19,26,19,20]
theta = [2,5]
#学习速率
leraing_rate = 0.005
loss = 50
iters = 1
Eps = 0.0001
#随机梯度下降
while loss>Eps and iters <1000 :
    loss = 0
    i = random.randint(0, 3)
    h = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1]
    theta[0] = theta[0] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][0]
    theta[1] = theta[1] + leraing_rate*(Matrix_y[i]-h)*matrix_A[i][1]
    Error = 0
    Error = theta[0]*matrix_A[i][0] + theta[1]*matrix_A[i][1] - Matrix_y[i]
    Error = Error*Error
    loss = loss +Error
    iters = iters +1
print ('theta=',theta)
print ('iters=',iters)
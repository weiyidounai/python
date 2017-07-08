#字符串拼接。用户输入两个字符串，将他们组合后输出
# str1=input("请输入一个人的名字")
# str2=input("请输入一个国家的名字")
# print("世界这么大，{}想去{}看看。".format(str1,str2))

#整数序列求和。用户输入一个正整数N，计算从1到N相加后的结果
# n=input("请输入整数N：")
# sum=0
# for i in range(int(n)):
#     sum +=i+1
# print("1到N求和结果：",sum)

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={:2} ".format(j,i,i*j),end='')
#     print('')

#阶乘计算
# sum,tmp=0,1
# for i in range(1,11):
#     tmp*=i
#     sum+=tmp
# print("运算结果是：{}".format(sum))

#猴子偷桃
# n=1
# for i in range(5,0,-1):
#     n=(n+1)<<1
# print(n)

#j健康食谱输出
# diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
# for x in range(0,5):
#     for y in range(0,5):
#         if not (x==y):
#             print("{}{}".format(diet[x],diet[y]))

#五角星的绘制
# from turtle import *
# fillcolor("red")
# begin_fill()
# while True:
#     forward(200)
#     right(144)
#     if abs(pos())<1:
#         break
#     end_fill()

#太阳花的绘制
# from  turtle import *
# color ('red','yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(179)
#     if abs(pos())<1:
#         break
# end_fill
# done()

#螺旋线绘制
import turtle
import time
turtle.speed("fast")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(8)

#彩色螺旋线绘制
# import turtle
# import time
# turtle.pensize(2)
# turtle.bgcolor("black")
# colors=["red","yellow","purple","blue"]
# turtle.tracer(False)
# for x in range(400):
#     turtle.forward(2*x)
#     turtle.color(colors[x%4])
#     turtle.left(91)
# turtle.tracer(True)


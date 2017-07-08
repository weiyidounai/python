# matchSim.py
# from random import *
#
#
# def main():
#     printIntro()
#     probA, probB, n = getInputs()
#     winsA, winsB = simNGames(n, probA, probB)
#     PrintSummary(winsA, winsB)
#
#
# def printIntro():
#     print('This program simulates a game between two')
#     print('There are two players, A and B')
#     print('Probability(a number between 0 and 1)is used')
#
#
# def getInputs():
#     a = eval(input('What is the prob.player A wins?'))
#     b = eval(input('What is the prob.player B wins?'))
#     n = eval(input('How many games to simulate?'))
#     return a, b, n
#
#
# def simNGames(n, probA, probB):
#     winsA = 0
#     winsB = 0
#     for i in range(n):
#         scoreA, scoreB = simOneGame(probA, probB)
#         if scoreA > scoreB:
#             winsA = winsA + 1
#         else:
#             winsB = winsB + 1
#     return winsA, winsB
#
#
# def simOneGame(probA, probB):
#     scoreA = 0
#     scoreB = 0
#     serving = "A"
#     while not gameOver(scoreA, scoreB):
#         if serving == "A":
#             if random() < probA:
#                 scoreA = scoreA + 1
#             else:
#                 serving = "B"
#         else:
#             if random() < probB:
#                 scoreB = scoreB + 1
#             else:
#                 serving = "A"
#     return scoreA, scoreB
#
#
# def gameOver(a, b):
#     return a == 15 or b == 15
#
#
# def PrintSummary(winsA, winsB):
#     n = winsA + winsB
#     print('\nGames simulated:%d' % n)
#     print('Wins for A:{0}({1:0.1%})'.format(winsA, winsA / n))
#     print('Wins for B:{0}({1:0.1%})'.format(winsB, winsB / n))
#
#
# if __name__ == '__main__':
#     main()

# from math import pi, sin, cos, radians
#
#
# def main():
#     angle = eval(input("Enter the launch angle (in degrees):"))
#     vel = eval(input("Enter the initial velocity (in meters/sec):"))
#     h0 = eval(input("Enter the initial height (in meters):"))
#     time = eval(input("Enter the time interval: "))
#
#     xpos = 0
#     ypos = h0
#
#     theta = radians(angle)
#     xvel = vel * cos(theta)
#     yvel = vel * sin(theta)
#
#     while ypos >= 0:
#         xpos = xpos + time * xvel
#         yvell = yvel - time * 9.8
#         ypos = ypos + time * (yvel + yvell) / 2.0
#         yvel = yvell
#     print("\nDistance traveled:{0:0.1f}meters.".format(xpos))
#
#
# if __name__ == "__main__":
#     main()

# 找到GPA最高的学生

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def makeStudent(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    # 打开输入文件
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')
    # 设置文件中第一个学生的记录为best
    best = makeStudent(infile.readline())

    # 处理文件剩余行数据
    for line in infile:
        # 将每一行数据转换为一个记录
        s = makeStudent(line)
        # 如果该学生是目前GPA最高的，则记录下来
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    # 打印GPA成绩最高的学生信息
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())


if __name__ == '__main__':
    main()

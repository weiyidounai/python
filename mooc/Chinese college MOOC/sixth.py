# # 根据数据文件在窗口中动态路径绘制
# import turtle
#
#
# def main():
#     # 设置窗口信息
#     turtle.title('数据驱动的动态路径绘制')
#     turtle.setup(800, 600, 0, 0)
#     # 设置画笔
#     pen = turtle.Turtle()
#     pen.color("red")
#     pen.width(5)
#     pen.shape("turtle")
#     pen.speed(2)
#     # 读取文件
#     result = []
#     file = open("data.txt", "r")
#     for line in file:
#         result.append(list(map(float, line.split(','))))
#     print(result)
#     # 动态绘制
#     for i in range(len(result)):
#         pen.color((result[i][3], result[i][4], result[i][5]))
#         pen.forward(result[i][0])
#         if result[i][1]:
#             pen.rt(result[i][2])
#         else:
#             pen.lt(result[i][2])
#     pen.goto(0, 0)
#
# if __name__ == '__main__':
#     main()

#实例2
# 利用字符串和列表将两个通讯录文本合并为一个文本
# def main():
#     ftele1 = open('TeleAddressBook.txt', 'rb')
#     ftele2 = open('EmailAddressBook.txt', 'rb')
#
#     ftele1.readline()  # 跳过第一行
#     ftele2.readline()
#     lines1 = ftele1.readlines()
#     lines2 = ftele2.readlines()
#
#     list1_name = []
#     list1_tele = []
#     list2_name = []
#     list2_email = []
#
#     for line in lines1:  # 获取第一个文本中的姓名和电话信息
#         elements = line.split()
#         list1_name.append(str(elements[0].decode('gbk')))
#         list1_tele.append(str(elements[1].decode('gbk')))  # 将文本读出来的bytes转换为str类型
#
#     for line in lines2:  # 获取第二个文本中的姓名和邮件信息
#         elements = line.split()
#         list2_name.append(str(elements[0].decode('gbk')))
#         list2_email.append(str(elements[1].decode('gbk')))
#
#     ###开始处理###
#     lines = []
#     lines.append('姓名\t    电话   \t  邮箱\n')
#
#     # 按索引方式遍历姓名列表1
#     for i in range(len(list1_name)):
#         s = ''
#         if list1_name[i] in list2_name:
#             j = list2_name.index(list1_name[i])  # 找到姓名列表1对应列表2中的姓名索引位置
#             s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
#             s += '\n'
#         else:
#             s = '\t'.join([list1_name[i], list1_tele[i], str('   -----   ')])
#             s += '\n'
#         lines.append(s)
#
#     # 处理姓名列表2中剩余的姓名
#     for i in range(len(list2_name)):
#         s = ''
#         if list2_name[i] not in list1_name:
#             s = '\t'.join([list2_name[i], str('   -----   '), list2_email[i]])
#             s += '\n'
#         lines.append(s)
#
#     ftele3 = open('AddressBook.txt', 'w')
#     ftele3.writelines(lines)
#     ftele3.close()
#     ftele1.close()
#     ftele2.close()
#
#     print("The addressBooks are merged!")
#
#
# if __name__ == "__main__":
#     main()

#字典实例1
import turtle

##全局变量##
# 词频排列显示个数
count = 10
# 单词频率数组-作为y轴数据
data = []
# 单词数组-作为x轴数据
words = []
# y轴显示放大倍数-可以根据词频数量进行调节
yScale = 6
# x轴显示放大倍数-可以根据count数量进行调节
xScale = 30


################# Turtle Start  ####################
# 从点(x1,y1)到(x2,y2)绘制线段
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# 在坐标(x,y)处写文字
def drawText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text)


def drawGraph(t):
    # 绘制x/y轴线
    drawLine(t, 0, 0, 360, 0)
    drawLine(t, 0, 300, 0, 0)

    # x轴: 坐标及描述
    for x in range(count):
        x = x + 1  # 向右移一位,为了不画在原点上
        drawText(t, x * xScale - 4, -20, (words[x - 1]))
        drawText(t, x * xScale - 4, data[x - 1] * yScale + 10, data[x - 1])
    drawBar(t)


# 绘制一个柱体
def drawRectangle(t, x, y):
    x = x * xScale
    y = y * yScale  # 放大倍数显示
    drawLine(t, x - 5, 0, x - 5, y)
    drawLine(t, x - 5, y, x + 5, y)
    drawLine(t, x + 5, y, x + 5, 0)
    drawLine(t, x + 5, 0, x - 5, 0)


# 绘制多个柱体
def drawBar(t):
    for i in range(count):
        drawRectangle(t, i + 1, data[i])
        ################# Turtle End  ####################


# 对文本的每一行计算词频的函数
def processLine(line, wordCounts):
    # 用空格替换标点符号
    line = replacePunctuations(line)
    # 从每一行获取每个词
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


# 空格替换标点的函数
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, " ")
    return line


def main():
    # 用户输入一个文件名
    filename = input("enter a filename:").strip()
    infile = open(filename, "r")

    # 建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    # 从字典中获取数据对
    pairs = list(wordCounts.items())

    # 列表中的数据对交换位置,数据对排序
    items = [[x, y] for (y, x) in pairs]
    items.sort()

    # 输出count个数词频结果
    for i in range(len(items) - 1, len(items) - count - 1, -1):
        print(items[i][1] + "\t" + str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])

    infile.close()

    # 根据词频结果绘制柱状图
    turtle.title('词频结果柱状图')
    turtle.setup(900, 750, 0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)


# 调用main()函数
if __name__ == '__main__':
    main()
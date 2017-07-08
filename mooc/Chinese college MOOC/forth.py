


# height=float (input("请输入你的身高(kg)："))
# weight=float (input("请输入你的体重(m)："))
# BMI=0
# BMI=weight /(height*height)
# print("BMI=",BMI)
# if BMI<18.5:
#     print("你的体重过于偏瘦，正常的BMI范围在国际标准为18.5-25，国内标准18.5-24")
# if 18.5<=BMI<24:
#     print("正常范围")
# if 24<=BMI<30:
#     print("偏胖")
# if BMI>=30:
#     print("肥胖")
score=float(input("your score:"))
grade=0
if score>=60.0:
    grade='D'
if score>=70.0:
    grade='C'
if score>=80.0:
    grade='B'
if score>=90.0:
    grade='A'
print("grade:",grade)


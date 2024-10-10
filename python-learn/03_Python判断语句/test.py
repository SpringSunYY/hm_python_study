import random

# money = 10000
# for i in range(1, 21):
#     import random
#     score = random.randint(1, 10)
#     if score < 5:
#         print(f"员工{i}，绩效分{score}，低于5，不发工资，下一位。")
#         continue
#     else:
#         money -= 1000
#         print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元")
#         if money == 0:
#             print("工资发完了，下个月领取吧。")
#             break


score = int(input())
print(score)
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 判断年份
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

print(2100 / 4)
print(2100 / 100)

x = int(input())
y = int(input())
if x > y:
    x, y = y, x
elif x % 2 == 0 and y % 2 == 0:
    x += 1
    y += 1
else:
    x -= 1
    y -= 1

print(f"x:{x} y:{y}")
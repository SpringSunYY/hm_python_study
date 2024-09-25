class Student:
    __age_info = None
    name = None
    gender = None
    tel = None

    # 构造方法
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.study()
        self.sleep()

    def study(self):
        print(f"{self.name}在学习")

    def sleep(self):
        print(f"{self.name}在睡觉")

    def eat(self):
        print(f"{self.name}在吃饭")

    def __play(self):
        print(f"{self.name}在玩耍")


stu1 = Student("张三", "男", "123456789")

stu1.__age_info = 20
print(stu1.__age_info)


# stu1.__play()
# !/usr/bin/python3

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量

a = 80


def test():
    a = 20;
    print(a)


if (a <= 90 | a >= 80):
    print("a的值在90到80之间")
# test()

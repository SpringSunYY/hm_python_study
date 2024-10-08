# //设计一个类
class Student:
    name = None
    gender = None

    # self 访问成员变量
    def __init__(self):
        self.name = "YY"

    def say_hi(self):
        print("你好，我是学生,我的名字是：", self.name)

    def say_hi2(self, msg):
        print("你好，我是学生,我的名字是：", self.name, msg)


class Person:
    name = None
    gender = None
    student = Student()


# 创建对象
stu1 = Student()
print(type(stu1))
stu1.name = "苏心璐"
stu1.gender = "男"

stu1.say_hi()
stu1.say_hi2("你好")
print("------------------------")

person1 = Person()
print(type(person1))
person1.name = "YY"
person1.gender = "男"
person1.student.name = "YY"
person1.student.gender = "男"
print(person1.name, person1.gender, person1.student.name, person1.student.gender)

a = 4.7 / 56000000
b = 1.5 / 56000000
c = a - b
d = 3.2 / 56000000
print(c, d, c == d)

#tips:c,d在保留7位有效数字的情况下相等即可
c_rounded = round(c, 7)
d_rounded = round(d, 7)

print(c_rounded, d_rounded, c_rounded == d_rounded)

print((16/4-2**5*8/4%5//2))
print((5%2))
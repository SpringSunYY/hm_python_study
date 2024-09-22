# 只是推断，只是提示，不是强制性的
from typing import Union


class Student:
    name: str = ""
    gender: int = 0
    tel: str = ""
    age: int = 0

    # 构造方法
    def __init__(self, name, gender, tel, age):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.study()
        self.sleep()
        print(f"{self.name}的年龄是{self.age},年龄{self.age}的{self.gender}生")

    def study(self):
        print(f"{self.name}在学习")

    def sleep(self):
        print(f"{self.name}在睡觉")

    def eat(self):
        print(f"{self.name}在吃饭")

    def play(self):
        print(f"{self.name}在玩耍")


stu1 = Student("张三", "aaa", "123456789", 18)
stu1.name = 1
stu1.age = "10a"


def add(x: Union[int], y: int):
    return x + y


my_list: list[Union[int, str, list]] = [1, 2, 3, "a", "b", [1, 2, 3]]
for my in my_list:
    print(my)

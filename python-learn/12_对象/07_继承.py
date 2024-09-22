class Person:
    name = None
    gender = None
    def study(self):
        print(f"{self.name}不喜欢学习")

class Student (Person):
    tel = None
    age = None

    #构造方法
    def __init__(self, name, gender, tel, age):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.study()
        self.sleep()

    def study(self):
        print(f"{self.name}在学习")

    def sleep(self):
        print(f"{self.name}在睡觉")

    def eat(self):
        print(f"{self.name}在吃饭")

    def play(self):
        print(f"{self.name}在玩耍")


stu2= Student("李四", "女", "987654321", 19)
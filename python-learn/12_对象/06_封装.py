class Student:
    __age_info = 0
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

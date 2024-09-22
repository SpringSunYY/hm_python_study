class Student:
    name = None
    gender = None
    tel = None
    age = None

    # 构造方法
    def __init__(self, name, gender, tel, age):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.study()
        self.sleep()

    # 字符串方法
    def __str__(self):
        return f"姓名：{self.name}, 性别：{self.gender}, 电话：{self.tel}, 年龄：{self.age}"

    # 删除对象方法
    # def __del__(self):
    #     print(f"{self.name}对象被删除了")

    # 比较
    def __lt__(self, other):
        return self.age < other.age

    # eq
    def __eq__(self, other):
        return self.age == other.age

    # 拷贝
    def __copy__(self):
        return Student(self.name, self.gender, self.tel, self.age)

    def study(self):
        print(f"{self.name}在学习")

    def sleep(self):
        print(f"{self.name}在睡觉")

    def eat(self):
        print(f"{self.name}在吃饭")

    def play(self):
        print(f"{self.name}在玩耍")


stu1 = Student("张三", "男", "123456789", 18)

print("---------------------------------------------------------")
stu1Str = stu1.__str__()
print(stu1Str)

print("---------------------------------------------------------")
stu2 = stu1.__copy__()
stu2Str = stu2.__str__()
print(stu2Str)

print("---------------------------------------------------------")
print(stu1==stu2)

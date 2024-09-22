class Clock:
    id = None
    price = None

    def ring(self):
        print("ding ding ding")
        print(self.id, self.price)
        import winsound
        winsound.Beep(2000, 3000)


# 创建对象让其工作
clock1 = Clock()
clock1.id = 1
clock1.price = 100
clock1.ring()


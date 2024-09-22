class Animal:
    name = None

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print(f'{self.name} is meowing')


class Dog(Animal):
    def speak(self):
        print(f'{self.name} is barking')

animal= Animal('animal')
cat = Cat('cat')
dog = Dog('dog')
cat.speak()
dog.speak()

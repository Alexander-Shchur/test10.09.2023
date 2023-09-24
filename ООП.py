class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
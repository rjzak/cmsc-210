class Animal:
    def __init__(self, age, weight, name, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.breed = breed

    def feed(self):
        print(f"Feeding {self.name}...")

    def groom(self):
        print("Brushing")


class Cat(Animal):

    def change_litter(self):
        print(f"Changing litter for {self.name}...")


class Dog(Animal):
    def __init__(self, age, weight, name, breed, housebroken=True):
        super().__init__(age, weight, name, breed)
        self.housebroken = housebroken

    def groom(self):
        print("Wash")
        super().groom()

    def walk(self):
        print(f"Walking {self.name}...")


class Pen:

    def __init__(self):
        pass

    def add(self, animal):
        pass

    def remove(self, name):
        pass

    def feed(self):
        pass

    def groom(self):
        pass

    def walk(self):
        pass

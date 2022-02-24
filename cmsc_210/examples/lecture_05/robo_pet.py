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

    max_size = 4

    def __init__(self):
        self.animals = []

    def add(self, animal):
        if len(self.animals) >= self.max_size:
            print("Pen is full.")
        else:
            self.animals.append(animal)

    def remove(self, name):
        for idx, animal in enumerate(self.animals):
            if animal.name == name:
                return self.animals.pop(idx)
        print("Not in here")

    def feed(self):
        for animal in self.animals:
            animal.feed()

    def groom(self):
        pass

    def walk(self):
        for animal in self.animals:
            if isinstance(animal, Dog):
                animal.walk()

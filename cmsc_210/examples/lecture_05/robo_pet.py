import sys


class Animal:

    def __init__(self, age, weight, name, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.breed = breed

    def feed(self, scoops=1):
        print(f"Feeding {self.name}...")

    def groom(self):
        print("Bruching")


class Cat(Animal):

    def change_litter(self):
        print(f"Changing litter for {self.name}...")


class Dog:

    def __init__(self, age, weight, name, breed, housebroken=True):
        self.animal = Animal(age, weight, name, breed)
        super().__init__(age, weight, name, breed)
        self.housebroken = housebroken

    def groom(self):
        print("Wash")
        super().groom()

    def walk(self):
        print(f"Walking {self.name}...")



class Pen:

    def __init__(self):
        self.pen = []

    def add(self, animal):
        if len(self.pen) == 4:
            print("Pen is full.")
        else:
            self.pen.append(animal)

    def remove(self, name):
        for animal in self.pen:
            if animal.name == name:
                return  animal
        print("Animal not found.")

    def feed(self):
        for animal in self.pen:
            animal.feed()

    def groom(self):
        for animal in self.pen:
            animal.groom()

    def walk(self):
        for animal in self.pen:
            if isinstance(animal, Dog):
                animal.walk()


def read_csv(filename):
    print(f"File is {filename}")


if __name__ == "__main__":
    import csv
    filename = sys.argv[1]
    read_csv(filename)
    with open(filename) as filehandle:
        for row in csv.reader(filehandle):
           pass

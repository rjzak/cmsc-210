class Animal:

    def __init__(self, age, weight, name, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.breed = breed

    def feed(self, scoops=1):
        print(f"Feeding {self.name}...")
    
    def groom(self):
        raise NotImplementedError("Must implement this method on the child object.")


class Cat(Animal):

    def change_litter(self):
        print(f"Changing litter for {self.name}...")

    def groom(self):
        print(f"Brushing {self.name}...")


class Dog(Animal):

    def __init__(self, age, weight, name, breed, housebroken=True):
        super().__init__(age, weight, name, breed)
        self.housebroken = housebroken
    
    def groom(self):
        print(f"Washing and drying {self.name}...")

    def walk(self):
        print(f"Walking {self.name}...")


class Pen:

    def __init__(self):
        pass

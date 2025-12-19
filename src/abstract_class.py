from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        self.home = "Earth"

    @abstractmethod
    def eat(self):
        pass


class Mammal(Animal):
    def __init__(self):  # overriding constructor
        super().__init__()
        self.weight = 10

    def eat(self):
        print("This mammal is eating.")

    def walk(self):
        print("This mammal is walking.")


# animal = Animal()  # This will raise an error since Animal class is abstract
dog = Mammal()
dog.eat()  # Implemented in Mammal
dog.walk()
print("Home sweet home:", dog.home)

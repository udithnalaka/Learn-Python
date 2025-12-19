class Animal:
    def __init__(self):
        self.home = "Earth"

    def eat(self):
        print("This animal is eating.")


class Mammal(Animal):
    def __init__(self):  # overriding constructor
        super().__init__()
        self.weight = 10

    def walk(self):
        print("This mammal is walking.")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")


dog = Mammal()
dog.eat()  # Inherited from Animal
dog.walk()
print("Dog's home:", dog.home)

salmon = Fish()
salmon.eat()  # Inherited from Animal
salmon.swim()


print(isinstance(dog, Mammal))  # True
print(isinstance(dog, Animal))  # True
print(issubclass(Mammal, Animal))  # True
print(issubclass(Fish, Animal))  # True
print(issubclass(Animal, Mammal))  # False
print(issubclass(Fish, Mammal))  # False

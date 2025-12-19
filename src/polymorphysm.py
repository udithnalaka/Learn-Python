
class Mamal:
    def eat(self):
        print("Mamal is eating")


class Fish:
    def eat(self):
        print("Fish is eating")


def feed_animal(animals):
    for animal in animals:
        animal.eat()


dog = Mamal()
salman = Fish()
feed_animal([dog, salman])

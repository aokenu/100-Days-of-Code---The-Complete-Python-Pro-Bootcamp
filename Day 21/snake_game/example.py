class Animal:
    def __init__(self):
        pass

    def speak(self):
        return "Animal speaks"

class AnimalHealth:
    def __init__(self):
        pass

    def sick(self):
        return "Some animals are sick"

class Food(AnimalHealth):
    def __init__(self):
        pass

    def eat(self):
        return "Food is important"

class Dog(Animal, Food):
    def __init__(self):
        super().__init__()


    def bark(self):
        return "Dog barks"


my_animal = Animal()
my_dog = Dog()

print(my_dog.speak())
print(my_dog.eat())
print(my_dog.sick())
print(my_animal.speak())
# print(my_animal.eat())
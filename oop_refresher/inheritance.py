# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    # The constructor is inherited from the base class
    def speak(self):
        print(f"{self.name} barks.")

# Derived Class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog = Dog("Beatriz")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
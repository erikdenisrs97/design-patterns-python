class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")

# Solution

class Bird:
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class Penguin(NonFlyingBird):
    ...
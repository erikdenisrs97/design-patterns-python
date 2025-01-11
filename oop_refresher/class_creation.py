# Define the Greeting class
class Greeting:
    # Constructor for the class
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        # Print a personalized greeting message using the 'name' attribute
        return f"Hello, {self.name}!"
    
# Create an object of Greeting
greeting = Greeting("Wilson")

print(greeting.say_hello())
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):

    @abstractmethod
    def battery_life(self):
        pass

class Smartphone(ElectronicDevice):
    def battery_life(self):
        return "Smartphone battery life: 10 hours."
    # Implement the battery_life method for the Smartphone class

class Laptop(ElectronicDevice):
    def battery_life(self):
        return "Laptop battery life: 5 hours."
    # Implement the battery_life method for the Laptop class

class Smartwatch(ElectronicDevice):
    def battery_life(self):
        return "Smartwatch battery life: 24 hours."
    # Implement the battery_life method for the Smartwatch class

def display_battery_life(device: ElectronicDevice):
    print(device.battery_life())
    # Call the battery_life method of the given device object and print the returned string

# Test your implementation
smartphone = Smartphone()
laptop = Laptop()
smartwatch = Smartwatch()

display_battery_life(smartphone)
display_battery_life(laptop)
display_battery_life(smartwatch)

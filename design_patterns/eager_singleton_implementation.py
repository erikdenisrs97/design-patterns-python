class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        print("<super> init...")
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("initializing <child>...")
        self.attribute = "I am a Singleton"

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1.attribute)
print(singleton2.attribute)

print(singleton1 is singleton2)
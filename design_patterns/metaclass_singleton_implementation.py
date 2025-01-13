class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        print("Meta call...")
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__()

        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
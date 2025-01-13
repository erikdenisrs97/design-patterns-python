class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
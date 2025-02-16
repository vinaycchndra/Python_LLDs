from .abstractLogObserver import AbstractLogObserver

class ConsoleLogger(AbstractLogObserver):
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance    

    def log(self, message: str): 
        print(message)

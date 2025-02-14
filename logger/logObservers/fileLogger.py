from abstractLogObserver import AbstractLogObserver

class FileLogger(AbstractLogObserver):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance    

    def __init__(self, file_address): 
        self._file_address = file_address
    
    def log(self, message: str): 
        f = open(self._file_address, "a")
        f.write(message)
        f.write("\n")
        f.close()
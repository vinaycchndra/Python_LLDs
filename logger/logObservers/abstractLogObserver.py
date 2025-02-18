from abc import ABC, abstractmethod

class AbstractLogObserver(ABC):
    
    @abstractmethod
    def log(self, message): 
        pass
from enum import Enum
from abc import ABC, abstractmethod

class SymbolEnum(Enum): 
    cross = "×"
    circle = "o"   

class SymbolAbstract(ABC): 
    @abstractmethod
    def getSymbol():
        pass  

class Cross(SymbolAbstract): 
    def __init__(self): 
        self.sym_type = SymbolEnum.cross

    def getSymbol(self):
        return self.sym_type.value

class Circle(SymbolAbstract): 
    def __init__(self): 
        self.sym_type = SymbolEnum.circle

    def getSymbol(self):
        return self.sym_type.value

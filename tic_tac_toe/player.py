from symbol import SymbolAbstract
class Player: 
    def __init__(self, name: str, symbol: SymbolAbstract):
        self.name = name
        self.symbol = symbol 

    def getSymbolObject(self): 
        return self.symbol       
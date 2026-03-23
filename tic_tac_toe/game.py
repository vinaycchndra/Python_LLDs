from SingletonMeta import SingleTonMeta
from board import Board

class Game(metaclass=SingleTonMeta): 
    def __init__(self): 
        self.player1 = None 
        self.player2 = None 
        self.board =  Board()

    def printBoard(self): 
        self.board.printBoard()

    def checkWinnerSymbol(self): 
        res = None 
        for i in range(3): 
            res = self.board.checkRowCol(i, True) or self.board.checkRowCol(i, False)
            if res: 
                return res
        res = self.board.checkDiagonals()
        return res 
    
    def checkWinner(self): 
        symbol = self.checkWinnerSymbol()
        if symbol is None: 
            return None 
        if symbol == self.player1.getSymbolObject():
            return self.player1
        else: 
            return self.player2
        
    def assignPlayer1(self, player): 
        self.player1 = player

    def assignPlayer2(self, player): 
        self.player2 = player

    def move(self, x, y, player): 
        self.board.assignPlace(x, y, player) 

    
    

    
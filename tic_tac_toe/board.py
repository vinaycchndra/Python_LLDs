from player import Player

class Board: 
    def __init__(self): 
        self.board = [[None for _ in range(3)] for __ in range(3)]
    
    def printBoard(self): 
        for i in range(len(self.board)):
            row = [] 
            for j in range(len(self.board[0])): 
                symbol = self.board[i][j]
                
                if symbol: 
                    row.append(symbol.getSymbol())
                else: 
                    row.append(" ")

            print(" | ".join(row))
            if i != 2: 
                print("----------")
        print("\n"*4)

    def assignPlace(self, i, j, player: Player): 
        if  self.board[i][j]:
            raise Exception("Can not assign the already occupied space.......")
        self.board[i][j] =  player.getSymbolObject()

    # returns the symbol which won...
    def checkRowCol(self, k, row = False): 
        if row: 
            winner = self.board[k][0]
            if not winner: 
                return None 
             
            for i in range(3):
                if self.board[k][i] != winner: 
                    return None
        else: 
            winner = self.board[0][k] 
            if not winner: 
                return None 
            for i in range(3):
                if self.board[i][k] != winner: 
                    return None
        return winner                


    def checkDiagonals(self): 
        winner1 = self.board[0][0]
        winner2 = self.board[0][2]
        if winner1: 
            for i in range(3): 
                if winner1 != self.board[i][i]: 
                    winner1 = None 
                    break 
            
        if winner2: 
            for i in range(3): 
                if winner2 != self.board[i][2-i]: 
                    winner2 = None 
                    break 
        return winner2 or winner1


        





                        



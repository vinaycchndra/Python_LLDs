from game import Game 
from player import Player
from symbol import Cross, Circle

def main(): 
    game = Game() 
    player1 = Player('vcj1',Cross())
    player2 = Player('vcj2',Circle())
    game.assignPlayer1(player1)
    game.assignPlayer2(player2)
    start = player1

    while True: 
        try: 
            inp_ = input(f"input for the {start.name}")
            x, y =  list(map(int, inp_.split(",")))
            game.move(x, y, start)
            game.printBoard()
            winner = game.checkWinner()

            if winner:
                print(f"Player: {winner.name} has won the game")
                return
            if start == player1:
                start = player2 
            else: 
                start = player1 
        except Exception as e:
            print(e)

if __name__ == "__main__":  
    main()   

from board import Board

class Game:
    turn = 1
    no_winner = True

    def __init__(self, p1, p2):
        while(Game.no_winner):
            if Game.turn == 1:
                print("Player 1, it is your turn.", end='')
                Game.turn = 2
            elif Game.turn == 2:
                print("Player 2, it is your turn.", end='')
                Game.turn = 1
            choice = input(' Please input the case location (x and y) and value. e.g. "0 1 x": ')
            choice = choice.split()
            if int(choice[0]) < len(Board.values) and int(choice[1]) < len(Board.values[0]) and choice[2] in ['x', 'o'] and Board.values[int(choice[0])][int(choice[1])] == '_':
                Board.values[int(choice[0])][int(choice[1])] = choice[2]
            else:
                raise 'Error'
            Board.draw_board()
            Game.no_winner = False
    
   # def check_winner():

            

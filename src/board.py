
class Board:
    values = [['_', '_','_'],['_','_', '_'],['_', '_','_']]

    @staticmethod
    def draw_board():
        row = 3
        col = 3
        print(' _  _  _  ')
        for r in range(row):
            for c in range(col):
                print(f'|{Board.values[r][c]}|', end='')
            print('')
            
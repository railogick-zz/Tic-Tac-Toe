class TicTacToe:
    def __init__(self, field='         '):
        field = field.replace('_', ' ')
        self.row1 = list(field[0:3])
        self.row2 = list(field[3:6])
        self.row3 = list(field[6:9])
        self.board = [self.row1, self.row2, self.row3]
        self.board_rev = [self.row3, self.row2, self.row1]
        self.x_count = 0
        self.o_count = 0
        self.player = 'X'
        self.empty = 0
        self.x_wins = False
        self.o_wins = False

    def board_state(self):
        print('---------')
        print('|', *self.row1, '|')
        print('|', *self.row2, '|')
        print('|', *self.row3, '|')
        print('---------')

    def piece_wins(self, piece):
        return ((self.board[0][0] == piece and self.board[0][1] == piece and self.board[0][2] == piece) or  # across the top
                (self.board[1][0] == piece and self.board[1][1] == piece and self.board[1][2] == piece) or  # across the middle
                (self.board[2][0] == piece and self.board[2][1] == piece and self.board[2][2] == piece) or  # across the bottom
                (self.board[0][0] == piece and self.board[1][0] == piece and self.board[2][0] == piece) or  # down the left side
                (self.board[0][1] == piece and self.board[1][1] == piece and self.board[2][1] == piece) or  # down the middle
                (self.board[0][2] == piece and self.board[1][2] == piece and self.board[2][2] == piece) or  # down the right side
                (self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece) or  # diagonal
                (self.board[2][0] == piece and self.board[1][1] == piece and self.board[0][2] == piece))  # diagonal

    def get_winners(self):
        self.x_wins = self.piece_wins('X')
        self.o_wins = self.piece_wins('O')

    def play(self):
        while True:
            self.board_state()
            self.place_piece()
            self.get_winners()
            if self.x_wins:
                self.board_state()
                print('X wins')
                break
            elif self.o_wins:
                self.board_state()
                print('O wins')
                break
            else:
                print('Draw')
                break

    def piece_count(self):
        for i in range(len(self.board)):
            for j in self.board[i]:
                if j == 'X':
                    self.x_count += 1
                elif j == 'O':
                    self.o_count += 1
                else:
                    self.empty += 1

    def determine_outcome(self):
        self.get_winners()
        self.piece_count()
        if abs(self.x_count - self.o_count) > 1:
            print('Impossible')
        elif self.x_wins and self.o_wins:
            print('Impossible')
        elif not self.x_wins and not self.o_wins:
            if self.empty:
                print('Game not finished')
            else:
                print('Draw')
        else:
            if self.x_wins:
                print('X wins')
            elif self.o_wins:
                print('O wins')



    def place_piece(self):
        valid = [1, 2, 3]
        pieces = ['X', 'O']
        while True:
            try:
                pos_x, pos_y = input('Enter the coordinates: ').split(' ')
                pos_x = int(pos_x)
                pos_y = int(pos_y)
            except ValueError:
                print('You should enter numbers!')
                continue
            if pos_x not in valid or pos_y not in valid:
                print('Coordinates should be from 1 to 3!')
                continue
            elif self.board_rev[pos_y-1][pos_x-1] in pieces:
                print('This cell is occupied! Choose another one!')
            else:
                self.board_rev[pos_y-1][pos_x-1] = self.player
                if self.player == 'X':
                    self.player = 'O'
                else:
                    self.player = 'X'
                break


# new_field = input('Enter Cells: ')
game = TicTacToe()
game.play()

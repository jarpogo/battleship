
class Board():

    def __init__(self, size):
        self.board = [[' ' for j in range(size)] for i in range(size)]
        self.size = size

    def print_board(self):

        print([f'{x}' for x in range(self.size + 1)])

        alpha_chr = 65
        for row in self.board:

            print([chr(alpha_chr)] + row)
            alpha_chr += 1

    def update_tile(self, x: int, y: int, hit: bool):

        current_state = self.board[x][y]

        if current_state != ' ':
            print("This location has already been targeted")
            return

        if hit:
            self.board[x][y] = 'X'
        else:
            self.board[x][y] = 'O'

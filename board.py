

class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        # the winner's sign O or X
        self.winner = ""

    def get_size(self):
        return self.size
    # optional, return the board size (an instance size)

    def get_winner(self):
        return self.winner

    # return the winner's sign O or X (an instance winner)
    def set(self, cell, sign):
        self.board[cell] = sign

    def isempty(self, cell):
        if (self.board[cell] == " "):
            return True
        else:
            return False

    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
    # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        if self.board[0] == self.board[1] == self.board[2] != ' ':
            self.winner = self.board[0]
            done = True
        elif self.board[3] == self.board[4] == self.board[5] != ' ':
            self.winner = self.board[3]
            done = True
        elif self.board[6] == self.board[7] == self.board[8] != ' ':
            self.winner = self.board[6]
            done = True
        elif self.board[0] == self.board[3] == self.board[6] != ' ':
            self.winner = self.board[3]
            done = True
        elif self.board[1] == self.board[4] == self.board[7] != ' ':
            self.winner = self.board[1]
            done = True
        elif self.board[2] == self.board[5] == self.board[8] != ' ':
            self.winner = self.board[2]
            done = True
        elif self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            done = True
        elif self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            done = True
        if " " not in self.board:
            self.winner = ""
            done = True
        return done

    def show(self):

        print('   A   B   C')
        print(' +---+---+---+')
        print('1| %s | %s | %s |' % (self.board[0], self.board[1], self.board[2]))
        print(' +---+---+---+')
        print('2| %s | %s | %s |' % (self.board[3], self.board[4], self.board[5]))
        print(' +---+---+---+')
        print('3| %s | %s | %s |' % (self.board[6], self.board[7], self.board[8]))
        print(' +---+---+---+')

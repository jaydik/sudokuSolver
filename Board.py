import numpy as np


class Board:
    def __init__(self, size):
        self.nrows = size
        self.ncols = size
        self.boardarr = np.zeros((size, size))

    def __repr__(self):
        return str(self.boardarr)

    def __getitem__(self, index):
        return self.boardarr[index]

    def print_board(self):
        print(self.boardarr)

    def input_position(self, arr):
        self.boardarr = arr.reshape(self.nrows, self.ncols)

    def is_solved(self):

        for i in range(self.ncols):
            if np.all(np.sort(self.boardarr[:, i]) == np.array(range(self.nrows))+1):
                continue
            else:
                return False

        for i in range(self.nrows):
            if np.all(np.sort(self.boardarr[i, :]) == np.array(range(self.ncols))+1):
                continue
            else:
                return False

        for i in range(int(self.nrows/3)):
            if np.all(np.sort(self.boardarr[0:3, 0+i*3:i*3+3].reshape(9)) == np.array(range(self.ncols))+1):
                if np.all(np.sort(self.boardarr[3:6, 0+i*3:i*3+3].reshape(9)) == np.array(range(self.ncols))+1):
                    if np.all(np.sort(self.boardarr[6:9, 0+i*3:i*3+3].reshape(9)) == np.array(range(self.ncols))+1):
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False

        return True

    def solve(self):

        while not self.is_solved():
            continue
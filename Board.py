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

    def can_be(self, row, col):

        roffset = int(row / 3)
        coffest = int(col / 3)

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        return full_row.difference(set(self.boardarr[row, :]))\
                       .difference(set(self.boardarr[:, col]))\
                       .difference(set(self.boardarr[0+roffset*3:0+roffset*3+3, 0+coffest*3:0+coffest*3+3].reshape(9)))

    def solve(self):

        while not self.is_solved():
            for rix, row in enumerate(self.boardarr):
                for cix, col in enumerate(row):
                    if col == 0:
                        if len(self.can_be(rix, cix)) == 1:
                            self.boardarr[rix, cix] = next(iter(self.can_be(rix, cix)))
                            print(self.boardarr, rix, cix)




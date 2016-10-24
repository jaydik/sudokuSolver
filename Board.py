import numpy as np
from itertools import product


class Board:

    def __init__(self):
        self.board_arr = np.zeros((9, 9))

    def __repr__(self):
        return str(self.board_arr)

    def __getitem__(self, index):
        return self.board_arr[index]

    def print_board(self):
        print(self.board_arr)

    def input_position(self, arr):
        self.board_arr = arr.reshape(9, 9)

    def is_solved(self):

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for row in range(9):
            if len(full_row.difference(set(self.board_arr[row]))) > 0:
                return False

        for col in range(9):
            if len(full_row.difference(set(self.board_arr[:, col]))) > 0:
                return False

        for i in range(3):
            for j in range(3):
                if len(full_row.difference(set(self.board_arr[3*i:3*(i+1), 3*j:3*(j+1)].reshape(1, 9)[0]))) > 0:
                    return False

        return True

    def can_be(self, row, col):

        if self.board_arr[row, col] != 0:
            return set([self.board_arr[row, col]])

        roffset = int(row / 3)
        coffset = int(col / 3)

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        return full_row.difference(set(self.board_arr[row, :]))\
                       .difference(set(self.board_arr[:, col]))\
                       .difference(set(self.board_arr[roffset*3:(roffset+1)*3, coffset*3:(coffset+1)*3].reshape(9)))

    def row_needs(self, row):

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return full_row.difference(set(self.board_arr[row]))

    def col_needs(self, col):

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        return full_row.difference(set(self.board_arr[:, col]))

    def sq_needs(self, row, col):

        full_row = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        roffset = int(row / 3)
        coffset = int(col / 3)

        return full_row.difference(set(self.board_arr[roffset*3:(roffset+1)*3, coffset*3:(coffset+1)*3].reshape(9)))

    def rest_of_row_can_be(self, row_ix, col_ix):

        output = set()

        for col in range(9):
            if col == col_ix:
                continue
            if self.board_arr[row_ix, col] == 0:
                output = output.union(self.can_be(row_ix, col))

        return output

    def rest_of_col_can_be(self, row_ix, col_ix):

        output = set()

        for row in range(9):
            if row == row_ix:
                continue
            if self.board_arr[row, col_ix] == 0:
                output = output.union(self.can_be(row, col_ix))

        return output

    def rest_of_sq_can_be(self, row_ix, col_ix):

        output = set()

        roffset = int(row_ix / 3)
        coffset = int(col_ix / 3)

        for row in range(3):
            for col in range(3):
                if row == row_ix and col == col_ix:
                    continue
                if self.board_arr[roffset*3 + row, coffset*3 + col] == 0:
                    output = output.union(self.can_be(roffset*3 + row, coffset*3 + col))

        return output

    def solve(self):

        while not self.is_solved():
            iters = 0
            for row in range(9):
                for col in range(9):
                    roffset = int(row / 3)
                    coffset = int(col / 3)
                    if self.board_arr[row, col] == 0:
                        print(self.board_arr)
                        print('cell', row, col)
                        print('can be', self.can_be(row, col))
                        print('row needs', self.row_needs(row))
                        print('rest of row can be', self.rest_of_row_can_be(row, col))
                        print('col needs', self.col_needs(col))
                        print('rest of col can be', self.rest_of_row_can_be(row, col))
                        print('sq needs', self.sq_needs(row, col))
                        print('rest of sq can be', self.rest_of_sq_can_be(row, col))
                        print('my row', self.board_arr[row, :])
                        print('my col', self.board_arr[:, col])
                        print('my sq', self.board_arr[roffset*3:(roffset+1)*3, coffset*3:(coffset+1)*3].reshape(9))


                        if len(self.can_be(row, col)) == 1:
                            print('Solved one type1')
                            print('making it ', self.can_be(row, col))
                            self.board_arr[row, col] = self.can_be(row, col).pop()
                            continue

                        if len(self.row_needs(row).difference(self.rest_of_row_can_be(row, col))) == 1:
                            if len(self.can_be(row, col).intersection(self.row_needs(row).difference(self.rest_of_row_can_be(row, col)))) == 1:
                                print('Solved one type 2')
                                print('making it ', self.row_needs(row).difference(self.rest_of_row_can_be(row, col)))
                                self.board_arr[row, col] = self.row_needs(row).difference(self.rest_of_row_can_be(row, col)).pop()
                                continue

                        if len(self.col_needs(row).difference(self.rest_of_col_can_be(row, col))) == 1:
                            if len(self.can_be(row, col).intersection(self.col_needs(col).difference(self.rest_of_col_can_be(row, col)))) == 1:
                                print('solved one type 3')
                                print('making it ', self.col_needs(col).difference(self.rest_of_col_can_be(row, col)))
                                self.board_arr[row, col] = self.col_needs(col).difference(self.rest_of_col_can_be(row, col)).pop()
                                continue

                        if len(self.sq_needs(row, col).difference(self.rest_of_sq_can_be(row, col))) == 1:
                            if len(self.can_be(row, col).intersection(self.sq_needs(row, col).difference(self.rest_of_sq_can_be(row, col)))) == 1:
                                print('solved one type 4')
                                print('making it ', self.sq_needs(row, col).difference(self.rest_of_sq_can_be(row, col)))
                                self.board_arr[row, col] = self.sq_needs(row, col).difference(self.rest_of_sq_can_be(row, col)).pop()
                                continue
                        if row == 1 and col == 2:
                            return False
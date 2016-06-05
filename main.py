from Board import Board
from tests.testboards import solved_puzzle, unsolved_puzzle
import numpy as np


def main():

    my_board = Board(9)
    my_board.input_position(np.array(unsolved_puzzle))

    print(my_board.is_solved())

    for idx in range(my_board.nrows):
        print(my_board[idx, :])

if __name__ == '__main__':
    main()

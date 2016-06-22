from Board import Board
from tests.testboards import solved_puzzle, unsolved_puzzle, hard_puzzle
import numpy as np


def main():

    my_board = Board(9)
    my_board.input_position(np.array(hard_puzzle))
    my_board.print_board()
    print('\n\n')

    my_board.solve()

if __name__ == '__main__':
    main()

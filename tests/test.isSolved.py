from Board import Board
from tests.testboards import solved_puzzle, wrong_puzzle
import numpy as np

my_board = Board(9)

my_board.input_position(np.array(solved_puzzle))
assert(my_board.is_solved() == True)

my_board.input_position(np.array(wrong_puzzle))
assert(my_board.is_solved() == False)

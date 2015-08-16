__author__ = 'filipkulig'

import time

from board import Board
from draw import Draw


class Engine():

    draw = None
    board = None

    def __init__(self):
        self.draw = Draw()
        self.board = Board()
        self.draw.set_board(self.board)

    def run(self):

        info = self.draw.get_board_info()

        self.board.set_cols(info['cols'])
        self.board.set_lines(info['lines'])

        self.draw.draw_board()

        while True:
            self.board.update()
            self.draw.draw_board()

            time.sleep(0.1)

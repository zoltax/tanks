__author__ = 'filipkulig'

import curses


class Draw():

    my_screen = None
    board = None

    def __init__(self):
        self.my_screen = curses.initscr()
        self.my_screen.border(0)
        self.my_screen.refresh()


    def set_board(self,kupa):
        self.board = kupa

    def draw_board_info(self):
        self.my_screen.addstr(1,self.board.get_cols()-5,str(self.board.get_lines()))
        self.my_screen.addstr(2,self.board.get_cols()-5,str(self.board.get_cols()))
        pass

    def draw_board(self):
        self.draw_board_info()
        self.my_screen.refresh()

    def get_board_info(self):
        return {
            'lines': curses.LINES,
            'cols': curses.COLS
        }
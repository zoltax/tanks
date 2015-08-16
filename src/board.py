__author__ = 'filipkulig'


class Board():


    # curses.LINES and curses.COLS

    lines = None
    cols = None

    def __init__(self):

        pass

    def get(self):
        return "plansza"

    def update(self):
        pass

    def get_cols(self):
        return self.cols

    def get_lines(self):
        return self.lines

    def set_cols(self,cols):
        self.cols = cols

    def set_lines(self,lines):
        self.lines = lines

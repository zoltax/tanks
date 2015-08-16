__author__ = ['filip kulig', 'radek kulig']

import curses
import time

from src import engine


def curses_init():

    tank = 'x'

    tank_x = 1
    tank_y = 1

    my_screen = curses.initscr()

    while True:
        my_screen.clear()
        my_screen.border(0)
        my_screen.addstr(tank_x, tank_y, tank)
        my_screen.refresh()
        tank_y += 1
        tank_x += 1
        time.sleep(1)

    curses.endwin()

    pass


# curses_init()

e = engine.Engine()

e.run()


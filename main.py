__author__ = 'filipkulig'

import curses

def curses_init():

    my_screen = curses.initscr()

    my_screen.border(0)
    my_screen.addstr(12, 15, "witam")
    my_screen.refresh()
    a = my_screen.getch()


    my_screen.addstr(30, 30, ord(a))


    curses.endwin()


    pass



curses_init()
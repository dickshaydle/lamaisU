#!/usr/bin/python 
import curses
from curses import wrapper

class Character():
    def __init__(self, x0, y0, symbol):
        self.x = x0
        self.y = y0
        self.symbol = symbol

class Player():
    def __init__(self, x0, y0, symbol = '🦍'):
        self.x = x0
        self.y = y0
        self.symbol = symbol


player = Player(4, 11, '🦙')

def update(stdscr):
    stdscr.addch(player.y, player.x, player.symbol)
    stdscr.refresh()

def main_loop(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)

    while True:
        stdscr.clear()
        update(stdscr)
        c = stdscr.getch()
        if c == curses.KEY_RESIZE:
            y, x = stdscr.getmaxyx()
            stdscr.addstr(y-1, 0, 'screen size %dx%d'%(x, y))
            # stdscr.resize()
        if c in (ord('w'), curses.KEY_UP):
            player.y -= 1
        if c in (ord('a'), curses.KEY_LEFT):
            player.x -= 1
        if c in (ord('s'), curses.KEY_DOWN):
            player.y += 1
        if c in (ord('d'), curses.KEY_RIGHT):
            player.x += 1
        elif c == ord('q'):
            break  # Exit the while loop
       
       
if __name__ == '__main__':
    """Entry point."""
    wrapper(main_loop)

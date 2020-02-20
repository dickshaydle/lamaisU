#!/usr/bin/python 
import curses
from curses import wrapper
from time import time

class Character():
    def __init__(self, x0, y0, symbol, style=0):
        self.x = x0
        self.y = y0

        self.symbol = symbol
        self.animation = []
        self.animation_speed = 1
        self.frame = 0
        self.style = style

    def animate(self):
        if len(self.animation) > 0:
            self.frame = int(time()*self.animation_speed % len(self.animation))
            self.symbol = self.animation[self.frame]
            # self.frame += 1
            # if self.frame >= len(self.animation):
            #     self.frame = 0

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, self.symbol, self.style)
        # stdscr.addch(self.y, self.x, self.symbol)
        # stdscr.refresh()

class Player(Character):
    def __init__(self, x0, y0, symbol = '🦍'):
        super().__init__(x0, y0, symbol)



def main_loop(stdscr):
    # init curses
    curses.curs_set(0)  # hide blinking cursor
    curses.halfdelay(1)  # make getch() nonblocking, returns after x*1/10 seconds
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_WHITE)

    # init characters
    player = Player(4, 11, '🦙')

    word_lama = Character(2, 4, '_', curses.color_pair(1))
    word_lama.animation = ('La', 'La', 'La', 'am', 'ma', 'a ', '  ', ' L')
    word_lama.animation_speed = 4
    word_lama.style = curses.color_pair(1)
    word_is = Character(4, 4, 'is')
    word_U = Character(6, 4, 'U', curses.color_pair(2))
    gorilla = Character(2, 10, '🦍', curses.color_pair(4))
    wall = Character(2, 2, '🧱')

    ch_list = [
        word_lama, 
        word_is,
        word_U, 
        player, 
        wall, 
        gorilla]


    while True:
        stdscr.clear()

        y, x = stdscr.getmaxyx()
        stdscr.addstr(y-1, 0, 'screen size %dx%d'%(x, y))
        for ch in ch_list:
            ch.animate()
            ch.draw(stdscr)

        c = stdscr.getch()
        # if c == curses.KEY_RESIZE:
        #     y, x = stdscr.getmaxyx()
        #     stdscr.addstr(y-1, 0, 'screen size %dx%d'%(x, y))
            # stdscr.resize()
        # if c in (ord('1'), ):
            
        if c in (ord('w'), curses.KEY_UP):
            player.y -= 1
        if c in (ord('a'), curses.KEY_LEFT):
            player.x -= 2
        if c in (ord('s'), curses.KEY_DOWN):
            player.y += 1
        if c in (ord('d'), curses.KEY_RIGHT):
            player.x += 2
        elif c == ord('q'):
            break  # Exit the while loop
       
        stdscr.refresh()
       
if __name__ == '__main__':
    """Entry point."""
    wrapper(main_loop)

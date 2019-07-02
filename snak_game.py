import random
import curses

s= curses.initscr()
curses.curs_set(0)
sh,sw=s.getmaxyx()
w=curses.newein(sh,sw,0,0)
w.keypad(1)
w.timeout(100)

snk_x=sw/4
snk_y=sh/2
snak=[
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk-2]
]

food=[sh/2,sw/2]
import random
import curses

# set up game page with curser not there
s = curses.intiscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
# set snake position #
snk_x = sw/4
snk_y = sw/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0,sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head [snake[0][0], snake[0][1]]


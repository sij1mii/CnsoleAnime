import curses
 
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

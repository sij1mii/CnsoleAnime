import time
import curses

stdscr = curses.initscr

for i in range(5):
  for j in range(5 - i):
    stdscr.addstr(j,0,"Hello{}{}".format(i,j))
  stdscr.refresh()
  time.sleep(i)

  for k in range(5):
    stdscr.addstr(k,0,' '*20)
  stdscr.refresh()

curses.reset_shell_mode()

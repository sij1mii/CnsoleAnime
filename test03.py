import curses
 
 
def main(stdscr):
    stdscr.clear()  # 画面のクリア
    stdscr.addstr(0, 0, 'やっほー')  # 0行目, 0番目 に「やっほー」と表示する
    stdscr.refresh()  # 画面の更新
    stdscr.getkey()  # 入力内容の待ち受け。プログラムの終了を防ぐための記述
 
 
if __name__ == '__main__':
    curses.wrapper(main)

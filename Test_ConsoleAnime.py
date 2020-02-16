#2次元リストでコンソールアニメ
import os
import time

while True:
  n = 0
  x = 10
  count = 0

  board = [['□ ' for n in range(10)]for i in range(10)]
#board[n][1] = '@'
#nが7以上になるとエラー
#nが7になったら0を代入
  while count <= 26:
    count += 1
    n += 1
    x -= 1
    if n > 9:
      n = 0
    if x < 1:
      x = 10
    #下から表示
    if 0 < count < 5:
      board[x-1][4+n]='● '#右
      board[x-1][x-4]='● '#左
    elif 4 < count < 7:
      board[x-1][8]='● '
      board[x-1][2]='● '
    elif 6 < count < 9:
      board[2][x+4]='● '
      board[2][n-4]='● '
    elif 8 < count < 10:
      board[3][5]='● '

    #消す
    if 9 < count:
      board[8][5]='□ '
    if 9 < count < 14:
      board[x-2][5+n]='□ '
    elif 13 < count < 16:
      board[x-2][8]='□ '
    elif 15 < count < 18:
      board[2][x+3]='□ '
    elif 17 < count < 20:
      board[x+1][x+3]='□ '
    elif 19 < count < 22:
      board[n+2][x-7]='□ '
    elif 21 < count < 24:
      board[n+2][2]='□ '
    elif 23 < count < 26:
      board[n+2][n-1]='□ '
    
            
    #リストの括弧など非表示 ボード表示
    for board2 in board:
      print(' '.join(board2))

    print(n)
    print(x)
    print(count)
    #print(a)
    time.sleep(0.3)
    os.system('clear')
		

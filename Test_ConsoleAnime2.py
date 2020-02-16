#2次元リストでコンソールアニメ
import os
import time

def Loop1():
  while True:
    n = 0
    x = 10
    count = 0

    board = [['□ ' for n in range(11)]for i in range(11)]
    #nが10以上になるとエラー
    #nが10になったら0を代入
    while count <= 17:
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
        board[8][5]='  ' 
      if 9 < count < 14:
        board[x-2][5+n]='  '
        board[x-2][x-5]='  '
      elif 13 < count < 16:
        board[x-2][8]='  '
        board[x-2][2]='  '
      elif 15 < count < 18:
        board[2][x+3]='  '
        board[2][n-3]='  '
      elif 17 < count < 20:
        board[3][5]='  '
      
      #リストの括弧など非表示 ボード表示
      for board2 in board:
        print(' '.join(board2))

      print('n=',n)
      print('x=',x)
      print(count)
      time.sleep(0.3)
      os.system('clear')
	
Loop1()

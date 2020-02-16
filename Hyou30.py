import time
import sys
import os

nn = 0

def loop():
  while True:

    A = '⬜ '
    B = '⏹ '

    masu1 = A
    masu2 = B

    n = 0
    a = 1
    bb = 10
    b = 0
    nn = 0

    while n <= 25:
      if n % 10:
        a = 1
      print(n)
      bb -= 1

      for x in range(25):
        for y in range(30):
          print(masu1,end='')
          #yが29のa乗
          if y == 29**a:
            print('')

      n += 1
      print('')

      time.sleep(0.5)
      os.system('clear')
      b += 1

  nn += 1
loop()

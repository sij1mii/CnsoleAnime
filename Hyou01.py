import os
import time
import sys

nn = 0

def loop1():
  while True:
  
    A = '⬜ '
    B = '⏹ '

    masu1 = A
    masu2 = B

    n = 0
    a = 1
    aa = {}
    bb = 10
    b = 0
    nn = 0

    while n <= 25:
      if n % 10:
        a = 1
      print(n)
      bb -= 1
      for i in range(20):
        aa[i] = i

      for x in range(10):
        for y in range(10):
          if (x==n)&(y==3):
            print(masu2,end='')
          elif (x==bb)&(y==5):
            print(masu2,end='')
          elif (10<n<20)&((x==3)&(y==(n-11)))|\
            (10<n<21)&((x==6)&(y==(n-12)))|\
            (10<n<22)&((x==6)&(y==(n-13)))|\
            (10<n<23)&(x==6)&(y==(n-14)):
            print(masu2,end='')
          elif (n>10)&((x==8)&(y==9)):
            print(masu2)
          elif (n>11)&((x==8)&(y==8))|\
            (n>12)&((x==8)&(y==7)):
            print(masu2,end='')
          else:
            print(masu1,end='')
            if y == 9**a:
              print('')

      n += 1
      print('')

      time.sleep(0.5)
      os.system('clear')
      b += 1

  nn += 1
loop1()

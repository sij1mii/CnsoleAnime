import os
import random
import time

nn = 0

def loop03():
  A = '□ '
  B = '⏹ '
  a = 1
  b = 10
  r = 0
  n = 0

  masu1 = A
  masu2 = B

  while n < 15:
    if n % 10 == 0:
      a = 1
    print(n)
    b -= 1
    r = random.randint(1,10)

    for x in range(10):
      for y in range(10):
        if (1<n<10)&((x==3)&(y==(n-1)))|\
          (1<n<11)&((x==6)&(y==(n-2)))|\
          (1<n<12)&((x==6)&(y==(n-3)))|\
          (1<n<13)&((x==6)&(y==(n-4))):
          print(masu2,end='')
        else:
          print(masu1,end='')
          if y == 9**a:
            print('')
    n += 1
    print('')

    time.sleep(0.3)
    os.system('clear')
          

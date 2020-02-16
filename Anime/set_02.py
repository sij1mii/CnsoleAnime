import time
import random
import os
import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

def loop02():
  A = '□ '
  B = '● '
  C = '⏹ '
  D = '  '
  n = 0
  a = 1
  b = 10
  r = '\x1b[1;31m'
  g = '\x1b[1;32m'
  z = '\x1b[1;34m'
  c = '\x1b[0m'
  Br = B+r
  Bg = B+g

  while n < 20:
    #if n % 10 == 0:
      #a = 1
    print(n)
    b -= 1

    aaa = '\n'.join([''.join([(C+r)if(x==n)&(y==n)else(B+g)if(n>4)&(x==5)&(y==n-4)else A+c for y in range(20)]) for x in range(10)])
    bbb = '\n'.join([''.join([(C+z)if(x==1)&(y==n)else(D+r)if(n>2)&(x==8)&(y==n-2)else A+c for y in range(20)]) for x in range(10)])
    #print(bbb)
    print(aaa+bbb)
    n += 1
    #print('')

    time.sleep(0.3)
    os.system('clear')


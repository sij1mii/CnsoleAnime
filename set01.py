import colorama
from colorama import Fore,Back,Style
import time
import os

colorama.init(autoreset=True)

def loop01():
  A = '⬜ '
  #A = '  '
  B = '● '

  n = 0
  a = 1
  b = 10
  x = 0
  y = 0
  e[] = 0

  while n < 25:
    if n % 10 == 0:
      a = 1
    print(n)
    b -= 1
    for i in range(50):
      e[i]=i

    for x in range(20):
      if(x<10):
        print('',x,end='')
      else:
        print(x,end='')
      for y in range(30):
        if (x==n)&(y==e[n-2]):
          print(Fore.LIGHTGREEN_EX+B,end='')
        elif (y==10&(x==(n-1))|(x==(n-2))):
          print(Fore.LIGHTBLUE_EX+B,end='')
        else:
          print(A,end='')
      print('')

    n += 1
    print('')

    time.sleep(0.1)
    os.system('clear')

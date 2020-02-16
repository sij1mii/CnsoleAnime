import time
import os
import random
import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

def loop01():
  A = '□ '
  B = '⏹ '
  C = '● '
  D = '  '

  masu1 = A
  
  a = 1
  n = 0
  b = 10

  while n < 35:
    if n % 10 == 0:
      a = 1
    print(n)
    b -= 1

    for x in range(20):
      for y in range(30):
        if (x==n)&(y==0)|(x==b)&(y==n)|\
          (x==b-1)&(y==15):
          print(Fore.LIGHTYELLOW_EX+C,end='')
        elif (x==n*2)&(y==6):
          print(Fore.LIGHTRED_EX+C,end='')
        elif (x==n-1)&(y==5):
          print(Fore.LIGHTGREEN_EX+C,end='')
        elif (x==n-2)&(y==7):
          print(Fore.LIGHTBLUE_EX+C,end='')
        else:
          print(A,end='')
        #if y == 9**a:
          #print('')
      #print('\n')
    n += 1
    #print('')

    time.sleep(0.3)
    os.system('clear')

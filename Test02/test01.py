import time
import os
import random
import colorama
from colorama import Fore,Back,Style

a = '□ '
b = '⏹ '
c = '● '
d = '  '
n = 0
C = '\x1b[0m'
D = '\x1b[39m'
G = '\x1b[1;32m'
R = '\x1b[1;31m'
B = '\x1b[1;34m'
cR = c+R
cG = c+G
cB = c+B
bG = b+G

def mydef():
  rx = [0]*10
  ry = [0]*10

  for i in range(10):
    rx[i] = random.randint(0,10)
    ry[i] = random.randint(0,10)
  n = 0
  nn = 20

  while n < 40:
    print('rx[0]=',rx[0])

    print('\n'.join([''.join([(cR)\
    if((n>0)&(y==4)&(x==(n-rx[0]))|(y==2)&(x==(n-rx[1]))|\
    (y==6)&(x==(n-rx[2]))|(y==8)&(x==(n-rx[3]))|\
    (y==14)&(x==(n-rx[4]))|(y==16)&(x==(n-rx[5]))) else(cB)\
    if(n>1)&(x==(nn-rx[6]))&(y==3)|(n>0)&(x==(nn-rx[7]))&(y==7)|\
    (n>0)&(x==(nn-rx[8]))&(y==13)|(x==(nn-rx[9]))&(y==17)|\
    (n>0)&(x==(nn-rx[0]))&(y==19) else(b)\
    if(n>2)&(y==9)&(x==(n-rx[1]))|(n>0)&(x==11)&(y==(n-ry[0]))|\
    (n>1)&(x==(n-rx[3]))&(y==13) else\
    d for y in range(30)]) for x in range(20)]))

    n += 1
    nn -= 1
    #print(C)
    time.sleep(0.1)
    os.system('clear')
    #:print(C)

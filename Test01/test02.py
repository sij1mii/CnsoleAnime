import time
import os

a = '□ '
b = '⏹ '
c = '  '
n = 0
D = '\x1b[39m'

def mydef():
  n = 0
  C = '\x1b[0m'
  #D = '\x1b[39m'
  R = '\x1b[1;31m'
  G = '\x1b[1;32m'
  while n < 20:

    print('\n'.join([''.join([(b+R) if(n>0)&(y==3)&(x==4+n)|\
    (n>1)&(y==3)&(x==5)|(n>2)&(y==3)&(x==6)else\
    (b+G)if(n>2)&(y==9)&(x==n)|(n>0)&(y==n)&(x==11)|(n>1)&(x==n)&(y==13)\
    else c for y in range(30)])\
    for x in range(20)]))
    n += 1

    time.sleep(0.3)
    os.system('clear')
print(D)

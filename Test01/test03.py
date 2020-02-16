import time
import os

a = '□ '
b = '⏹ '
c = '  '
n = 0
D = '\x1b[39m'

def mydef():
  n = 0
  nn = 20
  C = '\x1b[0m'
  #D = '\x1b[39m'
  R = '\x1b[1;31m'
  G = '\x1b[1;32m'
  B = '\x1b[1;34m'
  while n < 20:

    print('\n'.join([''.join([(b+R) if(n>0)&(y==4)&(x==n)|\
    (n>0)&(y==2)&(x==n)|(n>0)&(y==6)&(x==n)|(n>0)&(y==8)&(x==n)|\
    (n>0)&(y==14)&(x==n)|(n>0)&(y==16)&(x==n)else\
    (b+B) if(n>1)&(x==nn)&(y==3)|(n>0)&(x==nn)&(y==7)|\
    (n>0)&(x==nn)&(y==13)|(n>0)&(x==nn)&(y==17)|(n>0)&(x==nn)&(y==19)\
    else (b+G) if(n>2)&(y==9)&(x==n)|(n>0)&(y==n)&(x==11)|\
    (n>1)&(x==n)&(y==13)\
    else c for y in range(30)])\
    for x in range(20)]))

    n += 1
    nn -= 1

    time.sleep(0.3)
    os.system('clear')
print(D)

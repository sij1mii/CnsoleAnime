import time
import random
import os

def mydef():
  while True:
    b = 32
    for i in range(16):
      print('\r')
      for n in range(b):
        if i < n < (b-(i+1)):
          print(" ",end="")
        else:
          print("@",end="")
      time.sleep(0.3)

    print('\r')
    print('Hello World!')

    a = 32
    for i in range(16):
      print('\r')
      for n in range(a):
        if (a/2)-i < n < (a/2)+i:
          print(" ",end="")
        else:
          print("@",end="")
      time.sleep(0.3)

    os.system('clear')
mydef()    

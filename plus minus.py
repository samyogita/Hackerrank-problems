import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos = 0
    neg = 0
    z =0
    A = list(arr)
    for item in A:
        if item >= 1:
             pos += 1
        elif item < 1 and item!= 0:
            neg += 1
        elif item == 0:
            z += 1
        else:
            pass
    print(pos/n)
    print(neg/n)
    print(z/n)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

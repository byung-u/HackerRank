#!/usr/bin/env python3
from math import ceil, log10
from itertools import count

def fib_number_of_digits(n):
    '''
    http://www.geeksforgeeks.org/finding-number-of-digits-in-nth-fibonacci-number/
    '''
    PHI = 1.6180339887498948
    if n == 1:
        return 1

    d = (n * log10(PHI)) - (log10(5) / 2)
    return ceil(d)

res = [0] * 5001
temp = 0
for i in range(5001):
    for j in count(temp, 1):
        if fib_number_of_digits(j) > i - 1:
            res[i] = j
            temp = j
            break
for _ in range(int(input().strip())):
   N = int(input().strip())
   print(res[N])
#
#
#for _ in range(int(input().strip())):
#    N = int(input().strip())
#    for i in count(1):
#        if fib_number_of_digits(i) > N - 1:
#            break
#    print(i)
#

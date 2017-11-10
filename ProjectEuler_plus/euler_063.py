#!/usr/bin/env python3
import sys


N = int(input().strip())
min_val = 10 ** (N - 1)
max_val = 10 ** (N)
i = 1
while i ** N < min_val:
    i += 1
di = i ** N
while di < max_val:
    print(di)
    i += 1
    di = i ** N

'''
N = int(input().strip())
min_val = int(pow(10 ** (N - 1), (1./N))) + 1
limit = 10 ** (N)
for i in count(min_val, 1):
    n = i ** N
    if n >= limit:
        break
    print(n)

'''

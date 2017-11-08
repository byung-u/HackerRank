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

#!/usr/bin/env python3
import sys
from math import sqrt

def is_palindromic(n):
    return n == n[::-1]

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


ret = []
max_n, base = map(int, input().split())
if base == 2:
    for i in range(max_n, 0, -1):
        if is_palindromic(str(i)) and is_palindromic((str(bin(i)))[2:]):
            ret.append(i)
else:
    for i in range(max_n, 0, -1):
        ci = convert(i, base)
        if is_palindromic(str(i)) and is_palindromic((str(ci))):
            ret.append(i)
print(sum(ret))

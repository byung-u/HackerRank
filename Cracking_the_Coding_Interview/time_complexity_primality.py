#!/usr/bin/env python3
import sys


def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(n - 2, n - 1, n) == 1

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')

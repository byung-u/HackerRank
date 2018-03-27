#!/usr/bin/env python3
from math import factorial

def binomial(x, y):
    try:
        binom = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        binom = 0
    return binom


def p113():
    modulo = 10 ** 9 + 7
    for _ in range(int(input().strip())):
        N = int(input().strip())
        last_dec = 0
        for n in range(1, N + 1):
            inc = 0
            dec = 0
            same = 9 * n
            inc = (binomial(10 + n - 1, n) - 1) % modulo
            dec = inc + last_dec
            last_dec = dec
            print([n]inc + dec - same)



p113()

#!/usr/bin/env python3
from math import sqrt


def is_square(n):
    s = sqrt(n)
    return s.is_integer()


def continued_frac_duration(S):
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    if is_square(S):
        return False
    m, d, a = 0, 1, sqrt(S)
    duration = 0
    while duration == 0 or d != 1:
        m = int(d * a) - m
        d = (S - m * m) // d
        a = (sqrt(S) + m) // d
        duration += 1
    return duration % 2


N = int(input().strip())
print(len([i for i in range(1, N + 1) if continued_frac_duration(i)]))

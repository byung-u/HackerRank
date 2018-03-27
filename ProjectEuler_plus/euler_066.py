#!/usr/bin/env python3
import sys
from math import sqrt

def is_square(n):
    s = sqrt(n)
    return s.is_integer()

def continued_frac_list(S):
    ret = []
    if is_square(S):
        return None
    m, d, a = 0, 1, sqrt(S)
    duration = 0
    ret.append(int(a))
    while duration == 0 or d != 1:
        m = int(d * a) - m
        d = (S - m * m) // d
        a = (sqrt(S) + m) // d
        ret.append(int(a))
        duration += 1
    return ret


def p066_result(A, num, den, i, maximo):
    if (i >= maximo):
        return num * A[i] + 1, A[i]
    else:
        rnum, rden = p066_result(A, den, A[i + 1], i + 1, maximo)
        num = num * rnum + rden
        den = rnum
        return num, den

input_d = int(input()) + 1
max_d, max_q = 0, 0
for D in range(1, input_d):
    A = []
    A = continued_frac_list(D)
    if A is None:
        continue
    # print([D], A, A[1:] + A[1:])
    longCiclo = len(A) - 1
    p, q = 1, 0

    if longCiclo > 0:
        if longCiclo % 2 == 0:
            p, q = p066_result(A, A[0], A[1], 1, longCiclo - 2)
        else:
            A += A[1:] + A[1:]
            p, q = p066_result(A, A[0], A[1], 1, 2 * longCiclo - 1)
    if max_q < q:
        max_q = q
        max_d = D
print(max_d)

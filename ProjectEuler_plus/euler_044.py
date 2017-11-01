#!/usr/bin/env python3
import sys
from math import sqrt

def is_pentagonal(n):
    # https://stackoverflow.com/questions/37390233/python-is-pentagonal-number-check
    # https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
    p = (sqrt((24 * n) + 1) + 1) / 6
    return p.is_integer()

carry = 1
n = 0

result = []
N, K = list(map(int, input().strip().split()))

MAX_N = 10 ** 6 + 1
pentagonal_num = [0]
for i in range(0, MAX_N * 2):
    n += carry
    pentagonal_num.append(n)
    carry += 3

for i in range(N, K, -1):
    k = i - K
    if is_pentagonal(pentagonal_num[i] + pentagonal_num[k]):
        result.append(pentagonal_num[i])
    if is_pentagonal(pentagonal_num[i] - pentagonal_num[k]):
        result.append(pentagonal_num[i])
res = set(result)
for r in sorted(list(res)):
    print(r)

#!/usr/bin/env python3
from math import factorial
from functools import reduce


def combination_calc(n, r):
    nums = [i for i in range(n, n - r, -1)]
    numerator = reduce(lambda x, y: x * y, nums)
    denominator = factorial(r)
    return numerator // denominator


N, K = list(map(int, input().strip().split()))
total = 0
for n in range(N, 1, -1):
    i, j = -1, -1
    for r in range(n, 1, -1):
        cc = combination_calc(n, r)
        if cc > K:
            break
    else:
        continue
    i = r + 1
    for r in range(1, n):
        cc = combination_calc(n, r)
        if cc > K:
            break
    else:
        continue
    j = r
    diff = i - j
    total += diff
print(total)

'''
# wrong
for n in range(N, 1, -1):
    for r in range(n, 1, -1):
        cc = combination_calc(n, r)
        if cc < K:
            if n == N:
                continue
            else:
                break
        result.append([n, r])
print(len(result))
'''

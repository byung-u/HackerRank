#!/usr/bin/env python3
import sys
from functools import reduce


'''
terms

1~9             10~99           100~999         ...
9               180             2700            ...
9 * 1 * 10^0    9 * 2 * 10^1    9 * 3 * 10^2    ...

    ==>  9 * i * (10 ** (i - 1))
'''


for _ in range(int(input().strip())):
    arr = list(map(int, input().strip().split()))
    result = []
    for a in arr:
        num = a
        for i in range(1, 19):  # max 10 ** 18
            term = 9 * i * (10 ** (i - 1))
            if num > term:
                num -= term
                continue
            d, m = divmod(num - 1, i)
            d += 10 ** (i - 1)
            result.append(int(str(d)[m]))
            break
    print(reduce(lambda x, y: x * y, result))


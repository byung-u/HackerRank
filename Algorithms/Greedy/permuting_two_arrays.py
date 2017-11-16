#!/usr/bin/env python3
import sys


for _ in range(int(input().strip())):
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a = sorted(a)
    b = sorted(b, reverse=True)
    ab = [x + y for x, y in zip(a, b)]
    for n in ab:
        if n < k:
            print('NO')
            break
    else:
        print('YES')

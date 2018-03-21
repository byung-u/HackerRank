#!/usr/bin/env python3

for _ in range(int(input())):
    n, p = list(map(int, input().strip().split(' ')))
    if n < 0 or p < 0:
        print('n and p should be non-negative')
    else:
        print(n ** p)

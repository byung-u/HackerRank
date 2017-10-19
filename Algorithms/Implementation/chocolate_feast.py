#!/usr/bin/env python3
for _ in range(int(input().strip())):
    n, c, m = list(map(int, input().strip().split(' ')))
    if m * c == n:
        print(m + 1)
    elif m * c > n:
        print(n // c)
    else:   # m * c < n:
        choco = n // c
        # print(choco)
        free, leftover = divmod(choco, m)
        choco += free
        # print(choco, '\t', free, leftover)
        remain = free + leftover
        while remain >= m:
            free, leftover = divmod(remain, m)
            choco += free
            # print('-->', choco, remain)
            remain = free + leftover
        print(choco)

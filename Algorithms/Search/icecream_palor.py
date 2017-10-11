#!/usr/bin/env python3

import sys
'''
Use Linear Search algorithm.

Performance
- Worst-case	O(n)
- Best-case 	O(1)
- Average 	O(n)

Worst-case space complexity	O(1) iterative
'''

for _ in range(int(input().strip())):
    found = False
    m = int(input().strip())
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    for i in range(0, n - 1):
        if c[i] >= m:
            continue
        for j in range(i + 1, n):
            if c[j] >= m:
                continue
            if c[j] == m - c[i]:
                found = True
                print(i + 1, j + 1)
                break
        if found is True:
            break

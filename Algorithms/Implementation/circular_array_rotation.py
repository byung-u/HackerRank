#!/usr/bin/env python3

import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
max_idx = len(a)

k = k % max_idx
for _ in range(q):
    m = int(input().strip())
    ri = m - k  # rotated index
    if ri < 0:
        ri += max_idx
    print(a[ri])

#!/usr/bin/env python3

import sys
from collections import Counter
from copy import copy

for _ in range(int(input().strip())):
    P = Counter(input())
    Q = copy(P)
    Q.subtract(input())
    cnt = 0
    for k, v in P.items():
        if v - Q[k] >= 1:
            cnt += 1
    if cnt > 1:
        print('YES')
    else:
        print('NO')

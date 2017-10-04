#!/usr/bin/env python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            h += 1
        else:
            h *= 2
    print(h)

#!/usr/bin/env python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    arr = [int(a_temp) for a_temp in input().strip().split(' ')]

    if k > len([a for a in arr if a <= 0]):
        print("YES")
    else:
        print("NO")


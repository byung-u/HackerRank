#!/usr/bin/env python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
if k < max(height):
    print(max(height) - k)
else:
    print(0)


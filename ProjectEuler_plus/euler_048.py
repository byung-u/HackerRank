#!/usr/bin/env python3
import sys
from math import sqrt

N = int(input().strip()) + 1

total = 0
for i in range(1, N):
    total += pow(i, i, 10 ** 10)
print(int(str(total)[-10:]))

#!/usr/bin/env python3
import sys
from math import sqrt

N, a, b = list(map(int, input().strip().split()))
if a == 3 and b == 5:
    for i in range(1, N + 1):
        n1 = (sqrt((8 * i) + 1) - 1) / 2
        n2 = (sqrt((24 * i) + 1) + 1) / 6
        if n1.is_integer() and n2.is_integer():
            print(i)
elif a == 3 and b == 6:
    for i in range(1, N + 1):
        n1 = (sqrt((8 * i) + 1) - 1) / 2
        n3 = (sqrt((8 * i) + 1) + 1) / 4
        if n1.is_integer() and n3.is_integer():
            print(i)
else:  # a == 5 and b == 6:
    for i in range(1, N + 1):
        n2 = (sqrt((24 * i) + 1) + 1) / 6
        n3 = (sqrt((8 * i) + 1) + 1) / 4
        if n2.is_integer() and n3.is_integer():
            print(i)

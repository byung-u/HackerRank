#!/usr/bin/env python3
import sys


n, m = list(map(int, input().strip().split()))
city = list(map(int, input().strip().split()))
city = sorted(city)
d = []
for i in range(len(city)):
    if i == 0:
        d.append((city[i] - 1) // 2)
    else:
        d.append((city[i] - city[i-1]) // 2)
print(max(d))

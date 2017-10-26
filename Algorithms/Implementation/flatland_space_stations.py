#!/usr/bin/env python3
import sys


n, m = list(map(int, input().strip().split()))
city = sorted(list(map(int, input().strip().split())))
if n == m:
    print(0)
    sys.exit(1)
d = []
d.append(city[0] - 0)
for i in range(0, m - 1):
    d.append((city[i + 1] - city[i]) // 2)
d.append(n - city[-1] - 1)
print(max(d))

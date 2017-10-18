#!/usr/bin/env python3


n, k = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
cost = 0
for i in range(0, len(c), k):
    if c[i] == 0:
        cost += 1
    else:  # - 1 - 2
        cost += 3
print(100 - cost)

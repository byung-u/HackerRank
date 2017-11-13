#!/usr/bin/env python3
from collections import Counter


n = int(input().strip())
ar = [int(a_temp) for a_temp in input().strip().split(' ')]
ar = sorted(ar)

mean = sum(ar) / n
median = (ar[n // 2 - 1] + ar[n // 2]) / 2
print(mean)
print(median)

cnt = Counter(ar)
mode_list = []
max_val = max(cnt.values())
for k, v in cnt.items():
    if v == max_val:
        mode_list.append(k)
print(min(mode_list))

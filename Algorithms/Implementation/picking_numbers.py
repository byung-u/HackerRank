#!/usr/bin/env python3

import sys
from collections import Counter, OrderedDict


n = int(input().strip())
ar = [int(a_temp) for a_temp in input().strip().split(' ')]
cnt = Counter()
for a in ar:
    cnt[a] += 1
od = OrderedDict(sorted(cnt.items()))
print(od)
last_k = None
last_v = 0
max_sum = 0
for k, v in od.items():
    if last_k is None:
        last_k = k
        last_v = v
        max_sum = v
        continue
    if last_k + 1 == k:
        if max_sum < last_v + v:
            max_sum = last_v + v
    else:
        if max_sum < v:
            max_sum = v
    last_k = k
    last_v = v
print(max_sum)

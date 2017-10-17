#!/usr/bin/env python3
from collections import Counter


n = int(input())
c = list(map(int, input().strip().split()))

cnt = Counter()
for n in c:
    cnt[n] += 1
for k, v in cnt.items():
    if v == 1:
        print(k)
        continue

#!/usr/bin/env python3
from collections import Counter


n = int(input().strip())
cnt = Counter(list(map(int, input().strip().split(' '))))
for k, v in cnt.items():
    if v == 1:
        print(k)
        break

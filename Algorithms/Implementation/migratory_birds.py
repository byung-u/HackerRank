#!/usr/bin/env python3

import sys
from collections import Counter

def migratoryBirds(n, ar):
    cnt = Counter()
    for a in ar:
        cnt[a] += 1
    return cnt.most_common(1)[0][0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

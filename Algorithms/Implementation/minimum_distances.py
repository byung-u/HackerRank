#!/usr/bin/env python3
import sys
from collections import Counter
from operator import itemgetter
from functools import reduce


n = int(input())
c = list(map(int, input().strip().split()))

# Check pair
cnt = Counter()
for n in c:
    cnt[n] += 1
sorted_cnt = sorted(cnt.items(), key=itemgetter(1))
if sorted_cnt[-1][1] == 1:  # There are no pair
    print(-1)
    sys.exit(1)

diffs = []
for k, v in cnt.items():
    if v == 1:
        continue
    # 1. get pair indexes
    # 2. get diff indexes
    # 3. append result
    diffs.append(reduce(lambda x, y: abs(x - y), [i for i,e in enumerate(c) if e == k]))
print(min(diffs))

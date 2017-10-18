#!/usr/bin/env python3
from collections import Counter
import operator


n = int(input().strip())
arr = input().strip().split()
cnt = Counter()
for a in arr:
    cnt[a] += 1
sorted_cnt = sorted(cnt.items(), key=operator.itemgetter(1))
print(sum([sorted_cnt[i][1] for i in range(len(sorted_cnt) - 1)]))

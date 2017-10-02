#!/usr/bin/env python3
import sys
from collections import Counter

arr1 = list(input().strip())
arr2 = list(input().strip())
c1 = Counter()
c2 = Counter()

for a in arr1:
    c1[a] += 1
for a in arr2:
    c2[a] += 1

diff = 0
dups = c1.keys() & c2.keys()
for k, v in c1.items():
    if k in dups:
        m = min(c1[k], c2[k])
        diff += c1[k] - m
    else:
        diff += c1[k]

for k, v in c2.items():
    if k in dups:
        m = min(c1[k], c2[k])
        diff += c2[k] - m
    else:
        diff += c2[k]
print(diff)

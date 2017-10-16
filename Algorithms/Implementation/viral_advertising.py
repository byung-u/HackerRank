#!/usr/bin/env python3
from math import floor


days = int(input().strip())
n = 5
liked = 0
for _ in range(days):
    like = floor(n/2)
    n = floor(n/2) * 3
    liked += like
print(liked)

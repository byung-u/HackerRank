#!/usr/bin/env python3


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

counter = [0] * 100  # 0 ~ 99
for a in ar:
    counter[a] += 1
print(' '.join(map(str, counter)))

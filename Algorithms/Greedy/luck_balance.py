#!/usr/bin/env python3

import sys


N, K = list(map(int, (input().strip().split())))
temp = [list(map(int, (input().strip().split()))) for i in range(0, N)]
important, unimportant = [], []
for t in temp:
    if t[1] == 1:
        important.append(t[0])
    else:
        unimportant.append(t[0])

important = sorted(important, reverse=True)
print(sum(important[:K]) + sum(unimportant) - sum(important[K:]))

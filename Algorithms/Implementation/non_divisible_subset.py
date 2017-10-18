#!/usr/bin/env python3
import sys
from itertools import permutations, combinations

n, k = list(map(int, input().split())) 
S = set(list(map(int, input().split())))
# print(n, k, S)
arr = None
max_sum = 0
for i in range(2):
    for c1 in combinations(S, len(S) - i):
        # print(c1)
        for c2 in combinations(c1, 2):
            # print('\t', c2, sum(c2))
            if sum(c2) % k == 0:
                break
        else:
            if max_sum < sum(c1):
                max_sum = sum(c1)
                arr = c1
print(len(arr))

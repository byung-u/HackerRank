#!/usr/bin/env python3

import sys

def solve(n, s, d, m):
    return len([i for i in range(0, len(s) - m + 1) if sum(s[i:i+m]) == d])
    # cnt = 0
    # for i in range(0, len(s) - m + 1):
    #     if sum(s[i:i+m]) == d:
    #         cnt += 1
    # return cnt
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

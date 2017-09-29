#!/usr/bin/env python3

import sys

def solve(n, p):
    d = [n // 2 - p // 2, p // 2]
    return min(d)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)


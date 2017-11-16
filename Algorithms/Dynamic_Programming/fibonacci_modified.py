#!/usr/bin/env python3


t1 ,t2, n = list(map(int, input().strip().split()))
n -= 2  # t1, t2 already have
res = 0
for i in range(n):
    t1, t2 = t2, t1 + (t2 ** 2)
print(t2)

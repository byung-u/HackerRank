#!/usr/bin/env python3
import sys


N = int(input().strip())
if N == 1:
    print(2)
    sys.exit(1)
elif N == 2:
    print(3)
    sys.exit(1)

n = [8, 11, 8 + 11]
d = [3, 4, 3 + 4]
i = 5
M = 4
while i < N + 1:
    if i % 3 == 0:
        n[0] = n[2] * M + n[1]
        d[0] = d[2] * M + d[1]
        M += 1
    elif i % 3 == 1:
        n[1] = n[2] * M + n[1]
        d[1] = d[2] * M + d[1]
        M += 1
    elif i % 3 == 2:
        n[2] = n[0] + n[1]
        d[2] = d[0] + d[1]
    i += 1
print(sum(map(int, (str(n[N % 3])))))

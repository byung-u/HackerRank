#!/usr/bin/env python3
import sys


N = int(input().strip())
B = list(map(int, input().strip().split(' ')))
if sum(B) % 2 == 1:
    print('NO')
    sys.exit(1)

cnt = 0
for i in range(N):
    if B[i] % 2 == 1:
        B[i] += 1
        B[i + 1] += 1
        cnt += 2
print(cnt)

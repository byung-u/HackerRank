#!/usr/bin/env python3

max_n = 1000 + 1
ways = [1] + [0] * max_n
for i in range(1, max_n):
    for j in range(i, max_n + 1):
        ways[j] += ways[j - i]

for _ in range(int(input().strip())):
    n = int(input().strip())
    print((ways[n] - 1) % (10 ** 9 + 7))

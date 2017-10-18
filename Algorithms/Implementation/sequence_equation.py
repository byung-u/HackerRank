#!/usr/bin/env python3
n = int(input().strip())
temp = list(map(int, input().split()))
p = [0]
p.extend(temp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if p[p[j]] == i:
            print(j)
            break

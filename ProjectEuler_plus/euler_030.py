#!/usr/bin/env python3

N = int(input().strip())
npower = [i ** N for i in range(0, 10)]


MAX_N = N * npower[9]
result = 0
for i in range(MAX_N, 1, -1):
    digits = list(map(int, str(i)))
    total = 0
    if sum([npower[j] for j in digits]) == i:
        result += i
print(result)

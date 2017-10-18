#!/usr/bin/env python3
from math import sqrt

# I think +100 is too much though..
squares = [i ** 2 for i in range(1, int(sqrt(10 ** 9)) + 100)]
for _ in range(int(input().strip())):
    cnt = 0
    A, B = list(map(int, input().split()))
    for s in squares:
        if s >= A and s <= B:
            cnt += 1
        if s > B:
            break
    print(cnt)

#!/usr/bin/env python3


N, T = list(map(int, input().strip().split(' ')))
width = list(map(int, input().strip().split(' ')))
for _ in range(T):
    i, j = list(map(int, input().strip().split(' ')))
    print(min(width[i:j + 1]))

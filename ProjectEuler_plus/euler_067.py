#!/usr/bin/env python3
import sys


for _ in range(int(input().strip())):
    tri = []
    N = int(input().strip())
    for _ in range(N):
        tri.insert(0, list(map(int, input().strip().split())))  # reversed tri
    for i in range(0, N):
        for j in range(0, N - i - 1):
            tri[i + 1][j] += max(tri[i][j], tri[i][j + 1])
    print(tri[N - 1][0])

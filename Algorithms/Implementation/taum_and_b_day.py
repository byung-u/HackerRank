#!/usr/bin/env python3


T = int(input())
for _ in range(T):
    b, w = list(map(int, input().strip().split()))
    x, y, z = list(map(int, input().strip().split()))
    costs = [b * x + w * y, b * (y + z) + w * y, b * x + w * (x + z)]
    print(min(costs))
'''
    # 1. original
    cost = b * x + w * y
    # 2-1. buy white and chage to black
    cost = b * (y + z) + w * y
    # 2-2. vice versa
    cost = b * x + w * (x + z)
'''

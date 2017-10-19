#!/usr/bin/env python3


L = int(input())
R = int(input())
print(max([i ^ j for i in range(L, R + 1) for j in range(L, R + 1)]))

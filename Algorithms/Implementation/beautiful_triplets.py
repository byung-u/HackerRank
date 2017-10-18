#!/usr/bin/env python3
import sys


n, d = list(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))
arr = sorted(arr)
print(len([i for i in range(0, len(arr) - 2) if arr[i] + d in arr and arr[i] + (2 * d) in arr]))


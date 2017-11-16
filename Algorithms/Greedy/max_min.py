#!/usr/bin/env python3
import sys


n = int(input().strip())
k = int(input().strip())
arr = sorted([int(input().strip()) for _ in range(n)])

result = sys.maxsize
for i in range(0, n - k + 1):
    # result = min((max(arr[i:k]) - min(arr[i:k])), result)  # slow
    result = min((arr[i + k - 1] - arr[i]), result)
print(result)


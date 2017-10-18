#!/usr/bin/env python3
n = int(input())
arr = list(map(int, input().split()))

while len(arr) > 0:
    print(len(arr))
    m = min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - m
    while (1):
        if 0 in arr:
            arr.remove(0)
        else:
            break

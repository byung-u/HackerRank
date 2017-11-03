#!/usr/bin/env python3
import sys


def bin_search(arr, r, n):
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > r:
            hi = mid - 1
        elif arr[mid] < r:
            lo = mid + 1
        else:
            return True
    return False

for i in range(int(input().strip())):
    money = int(input().strip())
    n = int(input().strip())
    flavors = list(map(int, input().strip().split(' ')))
    arr = sorted(flavors)
    for idx, f in enumerate(flavors):
        r = money - f
        if bin_search(arr, r, n):
            if f == r:
                ret = [i + 1 for i in range(n) if flavors[i] == f]
                if len(ret) == 1:
                    continue
                print(min(ret), max(ret))
            else:
                print(min(idx + 1, flavors.index(r) + 1), max(idx + 1, flavors.index(r) + 1))
            break


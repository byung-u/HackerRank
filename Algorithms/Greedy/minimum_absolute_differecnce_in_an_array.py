#!/usr/bin/env python3

import sys


def minimumAbsoluteDifference(n, arr):
    # 1. sort.
    # 2. Compare a[n] and a[n+1] and will get minimum diff values.
    # 3. Return minimum result.

    arr = sorted(arr)  # O(nlog(n))
    return min(abs(x -y) for x, y in zip(arr, arr[1:]))  # O(n^2)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)


#!/usr/bin/env python3
import sys


# There is a pattern.
# A[n] = A[n - 3] + A[n - 2] + A[n - 1]
arr = [0, 1, 2, 4]
for i in range(4, 37):
    arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
for _ in range(int(input().strip())):
    n = int(input().strip())
    print(arr[n])

'''
# Slow
def staircase(n, cnt):
    if n == 0:
        cnt[0] += 1
        return
    elif n < 0:
        return
    staircase(n - 1, cnt)
    staircase(n - 2, cnt)
    staircase(n - 3, cnt)
    return


def staircase(n, cnt):
    if n == 0:
        return cnt + 1
    elif n < 0:
        return cnt
    cnt = staircase(n - 1, cnt)
    cnt = staircase(n - 2, cnt)
    cnt = staircase(n - 3, cnt)
    return cnt

'''

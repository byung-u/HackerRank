#!/usr/bin/env python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap_cnt = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swap_cnt += 1
print('Array is sorted in %d swaps.' % swap_cnt)
print('First Element:', a[0])
print('Last Element:', a[-1])

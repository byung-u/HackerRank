#!/usr/bin/env python3

import sys


for _ in range(int(input().strip())):
    arr = [list(input()) for _ in range(int(input().strip()))]
    new_arr = []
    for ar in arr:
        temp = ([ord(a) for a in ar])
        new_arr.append(sorted(temp))
    for i in range(0, len(new_arr) - 1):
        if new_arr[i + 1][0] < new_arr[i][0] or new_arr[i + 1][-1] < new_arr[i][-1]: 
            print('NO')
            break
    else:
        print('YES')

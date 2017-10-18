#!/usr/bin/env python3

import sys
import copy


def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j > -1 and key < ar[j]:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j+1] = key
    return ar

n = int(input().strip())
ar = list(map(int, input().strip().split()))

key = ar[-1]
new_arr = copy.copy(ar[0:-1])
for i in range(len(new_arr) - 1, -1, -1):
    if new_arr[i] < key:
        new_arr[i + 1] = key
        print(' '.join(list(map(str, new_arr))))
        break
    else:
        if new_arr[i] == max(new_arr):
            new_arr.append(new_arr[i])
        else:
            new_arr[i + 1] = new_arr[i]
        print(' '.join(list(map(str, new_arr))))
else:
    new_arr[0] = key
    print(' '.join(list(map(str, new_arr))))

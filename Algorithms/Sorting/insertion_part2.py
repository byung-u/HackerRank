#!/usr/bin/env python3


n = int(input().strip())
ar = list(map(int, input().strip().split()))

for i in range(1, n):
    key = ar[i]
    j = i - 1
    while j > -1 and key < ar[j]:
        ar[j + 1] = ar[j]
        j = j - 1
    ar[j + 1] = key
    print(' '.join(map(str, ar)))

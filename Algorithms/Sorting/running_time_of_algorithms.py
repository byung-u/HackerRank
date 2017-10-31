#!/usr/bin/env python3

def insertion_sort(l):
    cnt = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > -1) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           cnt += 1
        l[j+1] = key
    return cnt


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
cnt = insertion_sort(ar)
print(cnt)


#!/usr/bin/env python3

def quick_sort(arr):
    pivot = arr[0]
    right = []
    left = []
    for i in range(1, len(arr)):
        if arr[i] >= pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])

    for l in left:
        print(l, end=" ")
    print(pivot, end=" ")
    for r in right:
        print(r, end=" ")
    print()

m = int(input().strip())
arr = [int(i) for i in input().strip().split()]
quick_sort(arr)


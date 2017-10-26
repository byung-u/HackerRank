#!/usr/bin/env python3
'''
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

0. Initial sequence
    [0, 1, 2, 5, 3, 3, 0] len=7

1. Find longest non-increasing suffix
    [0, 1, 2, 5, 3, 3, 0]
     0 < 1
       1 < 2
          2 < 5   --- longest ---
                  i = 7 - 1 - 3 = 3

2. Identify pivot
    [0, 1, 2, 5, 3, 3, 0]
              5
              i = 3, arr[3] = 5

3. Find rightmost sucessor to pivot in the suffix -> 'exceeds the pivot'
    [0, 1, 2, 5, 3, 3, 0]
              5 > 3   --- right most ---
                      j = 7 - 1 - 1 = 5

4. Swap with pivot
    before: [0, 1, 2, 5, 3, 3, 0]

        i - 1 = 2,  arr[2] = 2
        j = 5,      arr[5] = 3

    after : [0, 1, 3, 5, 3, 2, 0]
                  2->3     3->2

5. Reverse the suffix
    [0, 1, 3, 5, 3, 2, 0]
    [0, 1, 3]
              [5, 3, 2, 0]
              -> reverse [0, 2, 3, 5]

6. Done
    [0, 1, 3, 0, 2, 3, 5]

'''


def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        print([i], arr[i])
        i -= 1
    # Now i is the head index of the suffix

    # At the last permutation already
    if i <= 0:
        return False

    # Let array[i - 1] be the pivot
    # Find rightmost element that exceeds the pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    # Now arr[j] willl become the new pivot

    # swap pivot with j
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


for _ in range(int(input().strip())):
    w = list(input().strip())
    print(w)
    if next_permutation(w):
        print(''.join(w))
    else:
        print('no answer')

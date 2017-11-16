#!/usr/bin/env python3

from itertools import permutations


if __name__ == "__main__":
    max_val = 0
    max_res = []
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    for p in permutations(arr, 3):
        # https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
        if p[0] + p[1] > p[2] and p[1] + p[2] > p[0] and p[2] + p[0] > p[1]:
            if max_val < sum(p):
                max_val = sum(p)
                max_res = sorted(p)
    if len(max_res) == 0:
        print(-1)
    else:
        print(' '.join(map(str, max_res)))

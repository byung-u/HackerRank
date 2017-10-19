#!/usr/bin/env python3

import sys
from collections import Counter


def main():
    n = input().strip()
    N_arr = [int(x_temp) for x_temp in input().strip().split(' ')]
    m = input().strip()
    M_arr = [int(x_temp) for x_temp in input().strip().split(' ')]

    Nc = Counter()
    for a in N_arr:
        Nc[a] += 1
    Mc = Counter()
    for a in M_arr:
        Mc[a] += 1

    Dc = (Mc - Nc)
    lc = sorted(list(Dc.keys()))  # Ascending order
    print(' '.join(map(str, lc)))


if __name__ == '__main__':
    main()

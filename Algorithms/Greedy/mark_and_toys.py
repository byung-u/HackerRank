#!/usr/bin/env python3
import sys


def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    cnt, total = 0, 0
    for p in sorted_prices:
        total += p
        if total > k:
            break
        cnt += 1
    return cnt


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)

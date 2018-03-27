#!/usr/bin/env python3
from collections import defaultdict


def is_palindromic(n):
    return n == n[::-1]


def e55():
    d = defaultdict(int)
    n = int(input().strip())
    for i in range(1, n + 1):
        if is_palindromic(str(i)):
            d[i] += 1
            continue

        num = i
        for j in range(500):  # 500 just, guess though..
            num = num + int(str(num)[::-1])
            if is_palindromic(str(num)):
                d[num] += 1
                break
    # print(d)
    max_key = max(d, key=d.get)
    print(max_key, d[max_key])

e55()

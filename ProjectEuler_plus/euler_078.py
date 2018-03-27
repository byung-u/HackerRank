#!/usr/bin/env python3
from itertools import count


def pentagonal_seq(n):  # https://oeis.org/A001318
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * (3 * n - 1) // 2


def partition(n, part, penta):  # https://oeis.org/A000041
    if n == 0:
        return 1
    if n == 1:
        return 1
    ret = 0
    for idx, p in enumerate(penta):
        if n - p < 0:
            break
        if idx % 4 == 0 or idx % 4 == 1:
            ret += part[n - p]
        else:
            ret -= part[n - p]
    return ret


LIMIT = 6 * (10 ** 4)
part = [1, 1]
penta = []
for i in range(1, LIMIT + 1):
    penta.append(pentagonal_seq(i))
    penta.append(pentagonal_seq(i * -1))

for n in range(2, LIMIT + 1):
    ret = partition(n, part, penta)
    part.append(ret)

for _ in range(int(input().strip())):
    n = int(input().strip())
    print(part[n] % (10 ** 9 + 7))

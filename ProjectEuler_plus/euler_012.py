#!/usr/bin/env python3

import sys
from itertools import groupby
from functools import reduce

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def triangle_number(n):
    return int((n * (n + 1)) / 2)


if __name__ == "__main__":
    tn = [triangle_number(i) for i in range(1, 1001)]
    print(tn)
    sys.exit(1)
    for _ in range(int(input())):
        n = int(input())
        i = 2
        while(1):
            print(tn)
            pf = prime_factors(tn)
            pf_dup = [len(list(group)) for key, group in groupby(pf)]
            pf_dup = list(map(lambda x: x + 1, pf_dup))
            divisors = reduce(lambda x, y: x * y, pf_dup)
            if divisors > n:
                print(i, tn)
                break
            i += 1

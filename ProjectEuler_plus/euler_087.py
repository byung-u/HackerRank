#!/usr/bin/env python3
from math import sqrt


def prime_sieve(sieveSize):
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.

    sieve = [True] * sieveSize
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False

    # create the sieve
    for i in range(2, int(sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] is True:
            primes.append(i)

    return primes


def search_idx(arr, lo, hi, key):

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < key:
            lo = mid + 1
        elif arr[mid] > key:
            hi = mid - 1
        else:
            return mid + 1
    return lo


# 3163 ** 2 = 10004569
#  216 ** 3 = 10077696
#   57 ** 4 = 10556001
primes = prime_sieve(3164)
sq = [p for p in primes if p <= 3163]
cb = [p for p in primes if p <= 216]
fp = [p for p in primes if p <= 57]

result = set()
for s in sq:
    for c in cb:
        for f in fp:
            result.add(s ** 2 + c ** 3 + f ** 4)
res = sorted(list(result))
len_res = len(res)
for _ in range(int(input().strip())):
    n = int(input().strip())
    print(search_idx(res, 0, len_res - 1, n))

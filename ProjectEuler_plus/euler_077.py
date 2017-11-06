#!/usr/bin/env python3
import sys
from math import sqrt


def prime_sieve(sieveSize):
    sieveSize += 1
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


for _ in range(int(input().strip())):
    n = int(input().strip())

    primes = prime_sieve(n)
    ways = [1] + [0] * n
    for p in primes:
        for i in range(p, n + 1):
            ways[i] += ways[i - p]
    print(ways[n])

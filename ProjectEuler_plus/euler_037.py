#!/usr/bin/env python3
import sys
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

def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    return pow(n - 2, n - 1, n) == 1


def is_truncable_prime(prime):
    n = 1
    while (1):
        div, mod = divmod(prime, pow(10, n))
        if div == 0:
            return True
        if is_prime(div) is False:
            return False
        if is_prime(mod) is False:
            return False
        n += 1
    return True


ret = []
n = int(input()) + 1
primes = prime_sieve(n)
for prime in primes[4:]:  # 2, 3, 5, 7 not considered
    if (is_truncable_prime(prime)):
        ret.append(prime)
print(sum(ret))

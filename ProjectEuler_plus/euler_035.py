#!/usr/bin/env python3
import sys
from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    return pow(n - 2, n - 1, n) == 1

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

def is_circular_prime(a):
    n = 1
    while(1):
        temp = []
        div, mod = divmod(a, pow(10, n))
        if div == 0:
            return True
        temp.append(str(mod))
        temp.append(str(div))
        c_prime = int(''.join(temp))
        if is_prime(c_prime) is False:
            return False
        n += 1
    return True


ret = []
input_n = int(input())
primes = prime_sieve(input_n)
for prime in primes:
    if is_circular_prime(prime):
        ret.append(prime)
print(sum(ret))

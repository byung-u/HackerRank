#!/usr/bin/env python3
import sys
from itertools import count


def is_prime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


N = int(input().strip())
d = 0
max_a, max_b = 0, 0
for a in range(1, N + 1):
    if a > 90:
        break
    for b in range(1, N + 1):
        if b > 1690:
            break

        for n in count(1):
            num = (n ** 2) + (a * n) + b
            if not is_prime(num):
                break
        if d <= n:
            max_a, max_b = a, b
            # print(max_a, max_b, n)
            d = n

        for n in count(1):
            num = (n ** 2) + (-a * n) + b
            if not is_prime(num):
                break
        if d <= n:
            max_a, max_b = -a, b
            # print(max_a, max_b, n)
            d = n

        for n in count(1):
            num = (n ** 2) + (-a * n) - b
            if not is_prime(num):
                break
        if d <= n:
            max_a, max_b = -a, -b
            # print(max_a, max_b, n)
            d = n

        for n in count(1):
            num = (n ** 2) + (a * n) - b
            if not is_prime(num):
                break
        if d <= n:
            max_a, max_b = a, -b
            # print(max_a, max_b, n)
            d = n

print(max_a, max_b)

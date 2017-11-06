#!/usr/bin/env python3
from decimal import getcontext, Decimal
from math import sqrt


def is_square(n):
    s = sqrt(n)
    return s.is_integer()


N = int(input().strip())
P = int(input().strip())

if N > 1000:
    if P > 1000:
        P = 1000
elif N < 100:
    if P > 10000:
        P = 10000

getcontext().prec = P + 2   # Decimal automatically round last digit
total = 0
for i in range(1, N + 1):
    if is_square(i):
        continue
    decimal_digits = Decimal(i).sqrt()
    result = ''.join(str(decimal_digits).split('.'))
    total += sum(map(int, result[0:P]))
print(total)

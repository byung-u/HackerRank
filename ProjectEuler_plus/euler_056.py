#!/usr/bin/env python3
import sys
from functools import reduce

N = int(input().strip())

max_digit_sum = [0] * N
max_digit = 0
for i in range(N):
    for j in range(N):
        digit_sum = 0
        d = i ** j
        while d != 0:
            d, m = divmod(d, 10)
            digit_sum += m
        if max_digit < digit_sum:
            max_digit_sum[i] = digit_sum
            max_digit = digit_sum
        else:
            max_digit_sum[i] = max_digit

print(max_digit_sum[-1])

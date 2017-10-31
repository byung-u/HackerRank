#!/usr/bin/env python3
import sys
from math import factorial

# f = [factorial(i) for i in range(0, 10)]
f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

#digit_factorials = []
#MAX_N = 10 ** 5 + 1
#for i in range(10, MAX_N):  # 0.28 sec
#    num = i
#    total = 0
#    while num > 0:
#        num, m = divmod(num, 10)
#        total += f[m]
#    if total % i == 0:
#        digit_factorials.append(i)
digit_factorials = [19, 56, 71, 93, 145, 219, 758, 768, 7584, 7684, 9696, 10081, 21993, 40585]

N = int(input())
total = 0
for d in digit_factorials:
    if d > N:
        break
    total += d
print(total)

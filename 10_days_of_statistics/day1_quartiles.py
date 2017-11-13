#!/usr/bin/env python3


n = int(input().strip())
ar = sorted([int(a_temp) for a_temp in input().strip().split(' ')])

L = ar[:n // 2]
U = ar[n // 2 + 1:]
len_half = len(L)

if n % 2 == 0:
    median = (ar[n // 2 - 1] + ar[n // 2]) // 2
    U = ar[n // 2:]
else:
    median = ar[n // 2]
    U = ar[n // 2 + 1:]

Q2 = median
if len_half % 2 == 0:
    Q1 = (L[len_half // 2 - 1] + L[len_half // 2]) // 2
    Q3 = (U[len_half // 2 - 1] + U[len_half // 2]) // 2
else:
    Q1 = L[len_half // 2]
    Q3 = U[len_half // 2]

print(Q1)
print(Q2)
print(Q3)

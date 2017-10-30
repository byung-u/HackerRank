#!/usr/bin/env python3
from copy import copy


def possible_swap(dn, i, j, sorted_dn):
    temp_dn = copy(dn)
    temp_dn[i], temp_dn[j] = temp_dn[j], temp_dn[i]
    if temp_dn == sorted_dn:
        return True
    else:
        return False


def possible_reverse(dn, i, j, sorted_dn):
    temp = dn[i: j + 1]
    temp_dn = []

    temp_dn.extend(dn[0:i])
    temp_dn.extend(temp[::-1])
    temp_dn.extend(dn[j + 1:])
    if temp_dn == sorted_dn:
        return True
    else:
        return False


n = int(input().strip())
dn = list(map(int, input().strip().split(' ')))
sorted_dn = sorted(dn)
for i in range(0, n - 1):
    if dn[i] > dn[i + 1]:
        break

for j in range(n - 1, 0, -1):
    if dn[j - 1] > dn[j]:
        break

if possible_swap(dn, i, j, sorted_dn):
    print('yes')
    print('swap', i + 1, j + 1)
elif possible_reverse(dn, i, j, sorted_dn):
    print('yes')
    print('reverse', i + 1, j + 1)
else:
    print('no')

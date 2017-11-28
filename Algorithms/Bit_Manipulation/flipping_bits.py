#!/usr/bin/env python3


INT_POWER = 32
for _ in range(int(input())):
    arr = [1] * INT_POWER
    b = bin(int(input()))[2:]

    len_b = len(b)
    for i in range(len_b):
        if b[i] == '1':
            arr[len_b - i - 1] = 0

    print(sum([2 ** i for i in range(INT_POWER) if arr[i] == 1]))

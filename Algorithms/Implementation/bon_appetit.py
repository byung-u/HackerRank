#!/usr/bin/env python3

import sys

def bonAppetit(n, k, b, ar):
    del ar[k]
    res = b - (sum(ar)//2)
    if res == 0:
        return 'Bon Appetit'
    else:
        return res

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)

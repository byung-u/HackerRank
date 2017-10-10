#!/usr/bin/env python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = list(map(int, input()))
    num = int(''.join(map(str, n)))
    print(len([i for i in n if i != 0 and num % i == 0]))

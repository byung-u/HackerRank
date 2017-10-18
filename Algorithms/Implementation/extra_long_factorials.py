#!/usr/bin/env python3

import sys


n = int(input().strip())
ret = 1
for i in range(n, 1, -1):
    ret *= i
print(ret) 

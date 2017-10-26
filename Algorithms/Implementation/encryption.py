#!/usr/bin/env python3
import sys
from math import ceil, sqrt


s = input().strip()
c = ceil(sqrt(len(s)))
print(' '.join([s[i::c] for i in range(c)]))

# awesome solution
# https://www.hackerrank.com/challenges/encryption/forum/comments/130572
# print(' '.join(map(lambda x: s[x::c], range(c))))

#!/usr/bin/env python3
from collections import Counter
import sys

S = Counter(input().strip())
possible_odd = 1
for k, v in S.items():
    if v % 2 == 1:
        possible_odd -= 1
        if possible_odd < 0:
            print('NO')
            sys.exit(1)
print('YES')

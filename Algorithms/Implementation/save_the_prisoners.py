#!/usr/bin/env python3
import sys
from collections import Counter
from operator import itemgetter
from functools import reduce

import sys

def saveThePrisoner(n, m, s):
    warn = m - 1 + s
    if warn > n:
        warn %= n
        if warn == 0:
            # all prisoner has it, so last person index
            warn = n
    return warn

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

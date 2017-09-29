#!/usr/bin/env python3

import sys
from collections import Counter

def sockMerchant(n, ar):
    sock = Counter()
    for a in ar:
        sock[a] += 1
    return sum([v // 2 for k, v in sock.items()])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)


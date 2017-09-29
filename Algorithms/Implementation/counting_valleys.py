#!/usr/bin/env python3

import sys

N = int(input().strip())
G = input().strip()
l = 0  
s = None
cnt = 0
for g in G:
    if g == 'U':
        l += 1
    else:
        l -= 1

    if l > 0 and s != 'M':
        s = 'M'
    elif l < 0 and s != 'V':
        s = 'V'
        cnt += 1
    elif l == 0:
        s = None
print(cnt)

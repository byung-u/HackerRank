#!/usr/bin/env python3

import sys


s = input().strip()
n = int(input())
if set(s) == {'a'}:
    print(n)
    sys.exit(1)
cnt_a = s.count('a')
len_s = len(s)
d, m = divmod(n, len_s)
cnt_a *= d
cnt_a += s[0:m].count('a')
print(cnt_a)

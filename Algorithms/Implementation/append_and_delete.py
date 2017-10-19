#!/usr/bin/env python3
import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

len_s = len(s)
len_t = len(t)
if s == t:
    print('Yes')
    sys.exit(1)

for i in range(len_t - 1, 0, -1):
    if s[0:i] == t[0:i]:
        if k >= (len_s - i) + (len_t - i):
            print('Yes')
        else:
            print('No')
        break
else:
    if len_s + 1 + len_t + 1 + 1 >= k:
        print('Yes')
    else:
        print('No')

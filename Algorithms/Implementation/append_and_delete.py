#!/usr/bin/env python3
import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

len_s = len(s)
len_t = len(t)
common_len = 0
for i in range(min(len_s, len_t)):
    if s[i] == t[i]:
        common_len += 1
print(common_len)
if len_s + len_t - 2 * common_len > k:  # case 1
    print('No')

'''
hackerhappy
      happy (delete)
hackerrank
      rank  (append)
5 + 4 = 9

aaa
aaa\0 (delete)
a
a     (append)
4 + 1 = 5

abcdef

fedcba
15

'''

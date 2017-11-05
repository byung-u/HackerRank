#!/usr/bin/env python3


a = list(input().strip())
b = list(input().strip())

alpha = [0] * 26
ord_a = ord('a')

for c in a:
    alpha[ord(c) - ord_a] += 1
for c in b:
    alpha[ord(c) - ord_a] -= 1
print(sum(map(abs, alpha)))


'''
# Great answer
from collections import Counter


counts = Counter(input())
counts.subtract(input())
print(sum([abs(v) for k, v in counts.items()]))
'''

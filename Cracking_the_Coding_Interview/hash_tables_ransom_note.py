#!/usr/bin/env python3
import sys
from collections import Counter


def ransom_note(magazine, ransom):
    m = Counter()
    for mag in magazine:
        m[mag] += 1
    r = Counter()
    for ran in ransom:
        r[ran] += 1
    for k, v in r.items():
        if r[k] - m[k] > 0:
            return False
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")


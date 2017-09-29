#!/usr/bin/env python3

import sys
from itertools import product

def getMoneySpent(keyboards, drives, s):
    res = -1
    for p in product(keyboards, drives):
        sp = sum(p)
        if sp == s:
            return s
        if sp < s:
            if res < sp:
                res = sp
    return res

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

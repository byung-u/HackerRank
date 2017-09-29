#!/usr/bin/env python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(z - y) == abs(z - x):
        print('Mouse C')
    elif abs(z - y) < abs(z - x):
        print('Cat B')
    else:
        print('Cat A')

#!/usr/bin/env python3
import sys

n = int(input())
path = [input() for _ in range(n)]
m, p  = None, None
for i in range(n):
    for j in range(n):
        if path[i][j] == 'm':
            m = (i, j)
        elif path[i][j] == 'p':
            p = (i, j)
        if m is not None and p is not None:
            break

x = m[0] - p[0]
y = m[1] - p[1]
if x < 0:
    while x != 0:
        print('DOWN')
        x += 1
elif x > 0:
    while x != 0:
        print('UP')
        x -= 1
if y < 0:
    while y != 0:
        print('RIGHT')
        y += 1
elif y > 0:
    while y != 0:
        print('LEFT')
        y -= 1

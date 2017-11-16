#!/usr/bin/env python3
import sys


for _ in range(int(input().strip())):
    N = int(input().strip())
    f = 0
    while N > 4:
        if N % 3 == 0:
            break
        f += 1
        N -= 5
    t = N // 3
    if t == 0 and f == 0:
        print(-1)
        continue
    if N % 3 != 0:
        print(-1)
        continue
    three = []
    five = []
    for _ in range(t):
        three.extend(['5' for i in range(3)])
    for _ in range(f):
        five.extend(['3' for i in range(5)])
    if len(three) == 0:
        print(''.join(five))
    elif len(five) == 0:
        print(''.join(three))
    else:
        a = ''.join(three)
        b = ''.join(five)
        print(a + b)

'''
# wrong
    # print(d, m)
    three = []
    five = []
    if m == 0 or m == 3 or m == 5:
        for i in range(d):
            three = ['5' for i in range(3)]
            five = ['3' for i in range(5)]
    
        if m == 3:
            three.extend(['5' for i in range(3)])
        elif m == 5:
            five.extend(['3' for i in range(5)])
    else:
        print(-1)
        continue
    # print(five, three)
    if len(three) == 0: 
        print(''.join(five))
    elif len(five) == 0: 
        print(''.join(three))
    else:
        a = ''.join(five)
        b = ''.join(three)
        c = b + a
        print(c)

'''

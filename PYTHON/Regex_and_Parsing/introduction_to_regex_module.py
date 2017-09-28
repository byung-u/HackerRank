#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    # ?      -> 0 or 1
    # *      -> 0 or more
    # [0-9]+ -> digits
    for _ in range(int(input())):
        print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
'''
    # This was awful
    t = int(input())
    for _ in range(t):
        s = input()
        if s.count('.') > 1:
            print('False')
        else:
            print(bool(re.match(r'^(\+\d+\.|\-\d+\.|\d+\.|\.|\+\.)+(\d+)$', s)))

'''

#!/usr/bin/env python3
import sys
import re

for _ in range(int(input())):
    m = re.search('^[7-9]\d{9}$', input())
    if m is None:
        print('NO')
    else:
        print('YES')

#!/usr/bin/env python3

import sys
from math import floor


n = int(input().strip())

m = 5
m = floor(m/2)
for i in range(0, n + 1):
    m = n * floor(m / 2)
    print(i, m)




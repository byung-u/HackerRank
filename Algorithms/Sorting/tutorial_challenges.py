#!/usr/bin/env python3

import sys

n = int(input().strip())
V = int(input().strip())
ar = list(map(int, input().strip().split()))

print(ar.index(n))

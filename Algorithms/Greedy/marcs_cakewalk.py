#!/usr/bin/env python3

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories = sorted(calories, reverse=True)
print(sum([(2 ** i) *c for i, c in enumerate(calories)]))

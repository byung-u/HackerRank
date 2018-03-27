#!/usr/bin/env python3
import sys
from math import sqrt


# (n * (n + 1)) / 2 -> n ** 2 + n - (2 * x)
#   Solved with quadratic equation
#   https://en.wikipedia.org/wiki/Quadratic_equation

for _ in range(int(input().strip())):
    t = int(input().strip())
    d = (sqrt(4 * 2 * t + 1) - 1)
    if d.is_integer():
        print(int(d) // 2)
    else:
        print(-1)


def e42():
    for _ in range(int(input().strip())):
        n = int(input().strip())
        root = int(sqrt(2 * n))
        if (root * (root + 1)) // 2 == n:
            print(root)
        else:
            print(-1)

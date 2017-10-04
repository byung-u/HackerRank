#!/usr/bin/env python3

import sys


arr = input().strip().split()
i, j, k = arr[0], arr[1], int(arr[2])
print(len([n for n in range(int(i), int(j) + 1) if (n - int(''.join(list(reversed(str(n)))))) % k == 0]))

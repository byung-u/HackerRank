#!/usr/bin/env python3
import sys

D1, M1, Y1 = list(map(int, input().split()))  # actual
D2, M2, Y2 = list(map(int, input().split()))  # expected

# delay year, month, day
dy = Y1 - Y2
dm = M1 - M2
dd = D1 - D2
if dy < 0:
    print(0)
elif dy <= 0 and dm < 0:
    print(0)
elif dy <= 0 and dm <= 0 and dd <= 0:
    print(0)
elif dm == 0 and dd > 0:
    print(15 * dd)
elif dy == 0 and dm > 0:
    print(500 * dm)
elif dy > 0:
    print(10000 * dy)

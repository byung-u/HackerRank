#!/usr/bin/env python3
import sys


MAX_VAL = 10 ** 12 + 1 # 1 ~ 10 **12
top_num = [3]
i = 3
while True:
    if i > MAX_VAL:
        break
    i *= 2
    top_num.append(i)

n = int(input().strip())
if top_num[0] >= n:
    print(top_num[0] - n + 1)
    sys.exit(1)

for i in range(1, len(top_num)):
    st = sum(top_num[0:i])
    if st >= n:
        print(st - n + 1)
        break

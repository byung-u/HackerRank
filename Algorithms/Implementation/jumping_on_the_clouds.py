#!/usr/bin/env python3


n = int(input())
c = list(map(int, input().strip().split()))
jump = 0
i = 0
len_c = len(c)
while i < len_c:
    if i == len_c - 3:
        jump += c[i + 2] + 1
        break
    elif i == len_c - 2:
        jump += c[i + 1] + 1
        break
    elif c[i + 2] == 0:
        jump += 1
        i += 2
    elif c[i + 1] == 0:
        jump += 1
        i += 1
    elif c[i + 2] == 1:
        jump += 2
        i += 2
print(jump)

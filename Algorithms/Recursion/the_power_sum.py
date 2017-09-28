#!/usr/bin/env python3

import sys

cnt = 0
def the_power_sum(num, n, e):
    global cnt

    num = num - (n ** e)
    if num == 0:
        # print('\t', num, n)
        cnt += 1
        return
    elif num < 0:
        return
    elif n == 1 and num != 1:
        return 
    n -= 1
    for i in range(n, 0, -1):
        if i == 1 and num != i:
            continue
        the_power_sum(num, i, e)


num = int(input())
e = int(input())
n = int(pow(num, 1/e))
for i in range(n, 0, -1):
    the_power_sum(num, i, e)
print(cnt)

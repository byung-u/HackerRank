#!/usr/bin/env python3

import sys

# 256th day
def solve_err(year):
    if year == 1918:
        return '26.09.%s' % year
    elif (year <= 1917 and year % 4) or (year > 1918 and (year % 4 == 0 and year % 100 != 0)):
        return '12.09.%s' % year
    else:
        return '13.09.%s' % year

def solve(year):
    D = 256
    d = (31 * 5) + (30 * 2)
    if year % 400 == 0:
        feb = 29
    elif year % 4 == 0:
        if year < 1918:
            if year % 4 == 0:
                feb = 29
            else:
                feb = 28
        else:
            if year % 100 != 0:
                feb = 29
            else:
                feb = 28
    else:
        feb = 28
    d += feb
    if year == 1918:
        d -= 13
    result = D - d
    return '%d.09.%d' % (result, year)

year = int(input().strip())
result = solve(year)
print(result)


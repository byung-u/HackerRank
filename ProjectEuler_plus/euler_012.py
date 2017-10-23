#!/usr/bin/env python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler012
import sys
from collections import OrderedDict
from math import sqrt

def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n / i))
    return results


# https://oeis.org/A076711/b076711.txt
highly_tn = [1, 3, 6, 28, 36, 120, 300, 528, 630, 2016, 3240, 5460, 25200, 73920, 157080, 437580, 749700, 1385280, 1493856, 2031120, 2162160, 17907120, 76576500, 103672800, 236215980, 842161320, ]

d = {}
for h in highly_tn:
    d[h] = len(factors(h))

oc = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
for _ in range(int(input())):
    n = int(input())
    for k, v in oc.items():
        if v > n:
            print(k)
            break


'''
# highly_tn = [1, 3, 6, 28, 36, 120, 300, 528, 630, 2016, 3240, 5460, 25200, 73920, 157080, 437580, 749700, 1385280, 1493856, 2031120, 2162160, 17907120, 76576500, 103672800, 236215980, 842161320, 3090906000, 4819214400, 7589181600, 7966312200, 13674528000, 20366564400, 49172323200, 78091322400, 102774672000, 557736444720, 666365279580, 876785263200, 1787835551040, 2427046221600, 3798207594720, 24287658595200, 26571463158240, 55093761676800, 70233049766880, 108825865948800, 700316229412800, 1751240328757920, 9730325811286080, 21108266891712000, 26416963807043040, 45742477468287600, 173735224344601920, 386503015576597920, 1185170185920520800, 7257013715087136000, 23680108643128938000, 47037157144547169600, 58649388578552772000, 78431386999734568800, 215379824102948625120, 335323643308670016000, 350272008384804586080, 1874830276609768558080, 2092324407584321710800, 5466414640512276360000, 5928498533477533693680, 7741959553552142318400, 28926759578859038332800, 39674777683728241454400,]

##########
## slow ##
##########


def triangle_number(n):
    return (n * (n + 1)) // 2


d = OrderedDict()
for i in range(1, 1001):
    tn = triangle_number(i)
    d[tn] = len(user_factors(tn))

compare = {}
max_val = 0
for k, v in d.items():
    if max_val < v:
        max_val = v
        compare[k] = v
    # print(k,v)
oc = OrderedDict(sorted(compare.items(), key=lambda t: t[0]))
# print(compare)
# print(oc)
for _ in range(int(input())):
    n = int(input())
    for k, v in oc.items():
        if n > k:
            print(v)
            break
'''

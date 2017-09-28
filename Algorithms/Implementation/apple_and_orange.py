#!/usr/bin/env python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

# print('st', s, t)
# print('ab', a, b)
# print('apple', apple)
# print('orange', orange)

A = [(a + ap) for ap in apple]
O = [(b + o) for o in orange]
# print(A, O)
cnt = 0
for n in A:
    if s <= n <= t:
        cnt += 1
print(cnt)
cnt = 0
for n in O:
    if s <= n <= t:
        cnt += 1
print(cnt)

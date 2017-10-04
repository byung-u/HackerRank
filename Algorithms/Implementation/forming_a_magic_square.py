#!/usr/bin/env python3

import sys

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)

res = 0
l = [num for n in s for num in n]
l1, l2 = [], []
for i in range(0, len(l), len(s)):
    l1.append(l[i: i + len(s)])

for i in range(0, len(s)):
    temp = []
    for j in range(0, len(s)):
        temp.append(l[i + (j * len(s))])
    l2.append(temp)

print(l1)
print(l2)




# res = 0
# l1 = []
# l2 = sorted([num for n in s for num in n])
# for i in range(1, 10):
#     if i in l2:
#         l2.remove(i)
#     else:
#         l1.append(i)
# len_l = len(l1)
# for i in range(len_l):
#     res += abs(l1[i] - l2[i])
# print(res)

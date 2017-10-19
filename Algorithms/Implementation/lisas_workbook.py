#!/usr/bin/env python3
n, k = list(map(int, input().strip().split(' ')))
t = list(map(int, input().strip().split(' ')))
res = []
for num in t:
    for i in range(1, num + 1):
        res.append(i)
    div, mod = divmod(num, k)
    if mod == 0:
        r = 0
    else:
        r = k - mod
    for i in range(r):
        res.append(0)

print(len([i for i in range(0, len(res), k) if (i // k) + 1 in res[i:i+k]]))
#for i in range(0, len(res), k):
#    if (i // k) + 1 in res[i:i+k]:
#        print([i], res[i:i+k])

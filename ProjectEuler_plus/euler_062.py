#!/usr/bin/env python3
from collections import defaultdict


N, K = list(map(int, input().strip().split()))
d = {}
d_num = defaultdict(int)
cubes = []

for i in range(1, N + 1):
    cube = i ** 3
    cubes.append(cube)
    check_num = ''.join(sorted(list(str(cube))))
    d[check_num] = d.get(check_num, 0) + 1

    if d_num[check_num] == 0:
        d_num[check_num] = cube
    else:
        d_num[check_num] = min(d_num[check_num], cube)

result = []
for k, v in d.items():
    if v == K:
        result.append(d_num[k])
result = sorted(result)
print('\n'.join(map(str, result)))

'''
# slow
for i in range(1, N + 1):
    cube = i ** 3
    cubes.append(cube)
    check_num = ''.join(sorted(list(str(cube))))
    d[check_num] = d.get(check_num, 0) + 1
len_cubes = len(cubes)

result = []
for k, v in d.items():
    if v == K:
        for i in range(0, len_cubes):
            if ''.join(sorted(list(str(cubes[i])))) == k:
                result.append(cubes[i])
                break
result = sorted(result)
print('\n'.join(map(str, result)))
'''

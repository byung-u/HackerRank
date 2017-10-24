#!/usr/bin/env python3
from collections import Counter


for _ in range(int(input())):
    n = int(input())
    arr = list(input())
    cnt = Counter()
    for a in arr:
        cnt[a] += 1

    if len(cnt) == 1 and list(cnt.keys())[0] == '_':
        print('YES')
        continue

    if '_' not in arr:
        if n < 3:
            print('NO')
        elif arr[0] == arr[1] and arr[-1] == arr[-2]:
            print('YES')
        else:
            print('NO')
        continue

    for k, v in cnt.items():
        if k != '_' and v == 1:
            print('NO')
            break
    else:
        print('YES')

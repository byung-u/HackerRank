#!/usr/bin/env python3


for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    if a > b:
        a, b = b, a
    result = set([a * (n - i - 1) + b * i for i in range(n)])
    res = sorted(list(result))
    print(' '.join(map(str, res)))

''' 
# slow

for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    temp = set()
    for p in product([a, b], repeat=n - 1):
        temp.add(sum(p))
        if len(temp) == n:
            break
    result = sorted(list(temp))
    print(' '.join(map(str, (result[0:n]))))
''' 

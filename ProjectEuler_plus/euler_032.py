#!/usr/bin/env python3


def is_pandigital(n, s=9):
    return len(n) == s and not '1234567890'[:s].strip(n)

N = int(input().strip())
result = set()
for i in range(1, 10000):
    for j in range(1, 10000):
        check_str = str(i) + str(j) + str(i * j)
        len_cs = len(check_str)
        if len_cs > N:
            break
        elif len_cs < N:
            continue
        if is_pandigital(str(i) + str(j) + str(i * j), len_cs):
            result.add(i * j)
                
print(sum(list(result)))

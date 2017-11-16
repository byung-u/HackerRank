#!/usr/bin/env python3
from math import sqrt

'''
# Sample test case for insight

## INPUT
1
100 2

## OUTPUT

3 4 1 2 7 8 5 6 11 12 9 10 15 16 13 14 19 20 17 18 23 24 21 22 27 28 25 26 31 32 29 30 35 36 33 34 39 40 37 38 43 44 41 42 47 48 45 46 51 52 49 50 55 56 53 54 59 60 57 58 63 64 61 62 67 68 65 66 71 72 69 70 75 76 73 74 79 80 77 78 83 84 81 82 87 88 85 86 91 92 89 90 95 96 93 94 99 100 97 98
'''


def factors_for_abperm(n):
    results = set()
    results.add(0)

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 1:
                results.add(i)
            elif (n // i) % 2 == 1:
                results.add(int(n / i))
            else:
                results.add(i)
                results.add(int(n / i))
    return results


for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    if N % 2 == 1:
        if K == 0:
            arr = [i + 1 for i in range(N)]
            print(' '.join(map(str, arr)))
        else:
            print(-1)
    elif K == 0:
        arr = [i + 1 for i in range(N)]
        print(' '.join(map(str, arr)))
    else:
        possible = factors_for_abperm(N)
        if K not in possible:
            print(-1)
            continue
        DK = K * 2
        for i in range(1, N + 1, DK):
            arr = [i + j for j in range(DK)]
            print(' '.join(map(str, arr[K:DK])), end=' ')
            print(' '.join(map(str, arr[0:K])), end=' ')
        print()


'''
# Error
def factors_for_abperm(n):
    results = set()
    results.add(0)

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 1:
                results.add(i)
            elif (n // i) % 2 == 1:
                results.add(int(n / i))
            else:
                results.add(i)
                results.add(int(n / i))
    return results


for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    arr = [i + 1 for i in range(N)]
    if N % 2 == 1:
        if K == 0:
            print(' '.join(map(str, arr)))
        else:
            print(-1)
        continue
    possible = factors_for_abperm(N)
    if K in possible:
        for a in arr:
            res = a + K
            if res > N:
                print(a - K, end=' ')
            else:
                print(res, end=' ')
        print()
    else:
        print(-1)

# Too slow
    for p in permutations(arr):
        pz = list(zip(p, arr))
        pset = set([reduce(lambda x, y: abs(x - y), temp) for temp in pz])
        print(pset)
        if len(pset) == 1 and list(pset)[0] == K:
            print(' '.join(list(map(str, p))))
            break
    else:
        print(-1)

# TEST
for N in range(2, 20, 2):
    print(N)
    arr = [i + 1 for i in range(N)]
    if N % 2 == 1:
        if K == 0:
            print(' '.join(map(str, arr)))
        else:
            print(-1)
        continue
    for p in permutations(arr):
        diff = [abs(arr[i] - p[i]) for i in range(N)]
        sd = set(diff)
        if len(sd) == 1:
            print('\t', sd, arr, p)
'''

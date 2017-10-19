#!/usr/bin/env python3


n, m = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
ways = [1] + [0] * n
for coin in c:
    for i in range(coin, n+1):
        ways[i] += ways[i-coin]
        # print(ways)
        # print('\t', i, i - coin)
print(ways[n])

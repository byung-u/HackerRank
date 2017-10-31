#!/usr/bin/env python3


target = 10 ** 5
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target
for coin in coins:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]

for _ in range(int(input().strip())):
    print((ways[int(input().strip())]) % (10 ** 9 + 7))

#!/usr/bin/env python3


n = int(input().strip())
ar = [int(a_temp) for a_temp in input().strip().split(' ')]
w = [int(a_temp) for a_temp in input().strip().split(' ')]

print(round(sum([ar[i] * w[i] for i in range(n)]) / sum(w), 1))

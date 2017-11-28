#!/usr/bin/env python3


for _ in range(int(input())):
    b = bin(int(input()))[2:]
    len_b = len(b)
    print(sum([2 ** (len_b - i - 1) for i in range(len_b) if b[i] == '0']))
    # for i in range(len_b):
    #     if b[i] == '0':
    # print(b[i], len_b - i, 2 ** (len_b - i - 1))

'''
# Wrong
MAX_E = 10 + 1
e_2 = [2 ** i for i in range(0, MAX_E + 1)]

for _ in range(int(input())):
    num = int(input())
    N = num
    res_idx = []
    while N > 1:
        for i in range(len(e_2)):
            if e_2[i] > N:
                N = N - e_2[i - 1]
                res_idx.append(i - 1)
                break
    great = 0
    for r in res_idx:
        if e_2[r + 1] > num:
            great += num - e_2[r] + 1
        else:
            great += e_2[r + 1] - e_2[r]
    print(great)
'''

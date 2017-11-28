#!/usr/bin/env python3
import sys

def xor_seq(num, div):
    if num == 0:
        n = 4 * div 
    elif num == 1:
        n = 1
    elif num == 2:
        n = 4 * div + 3
    else:
        n = 0
    return n

for _ in range(int(input())):
    result = 0
    L, R = map(int, input().strip().split())
    ld, lm = divmod(L, 4)
    rd, rm = divmod(R, 4)
    if L == R:
        print(xor_seq(lm, ld))
        continue
    # print([L, R])
    # print('\t', ld, lm)
    for i in range(lm, 4):
        n = xor_seq(i, ld)
        result = result ^ n
        # print('\t\t', [ld], i, '->', n)

    diff = rd - ld
    if diff > 1 and diff % 2 == 0:
        result = result ^ 2

    if diff != 0:
        for i in range(rm, -1, -1):
            n = xor_seq(i, rd)
            result = result ^ n
            # print('\t\t', [rd], i, '->', n)
    print(result)


'''
arr = [12, 1, 15]
arr = [4, 1, 7]
arr = [0, 1, 3]
x = 0
for i in arr:
    x = x ^ i
    print(x, end=', ')


sys.exit(1)

x = 0
print(x, end=', ')
for i in range(1, 30):
    x = x ^ i
    print(x, end=', ')
print()



#arr = [1, 7, 0, 8, 1, 11, 0, 12, 1, 15, 0, 16, 1, 19, 0]
#x = 4
#for i in arr:
#    x = x ^ i
#    print(x, end=', ')
#sys.exit(1)
# n = 0
# for i in range(1, 30):
#     n ^= i * 4
#     print([4 * i], n)
# #print([4], 0 ^ 4)
# #print([8], 4 ^ 8)
# #print([12], 12 ^ 12)
# #print([16], 0 ^ 16)
# #print([20], 16 ^ 20)
# #print([24], 4 ^ 24)
# sys.exit(1)

'''

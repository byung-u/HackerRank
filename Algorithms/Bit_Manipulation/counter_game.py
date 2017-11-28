#!/usr/bin/env python3
import sys

for _ in range(int(input())):
    N = int(input().strip())

    # If they set counter to 1, Richard wins,
    # because its Louise' turn and she cannot make a move.
    N -= 1
    
    b = bin(N)[2:]
    b_sum = sum([bn == '1' for bn in b])
    if b_sum & 1:
        print('Louise')
    else:
        print('Richard')
# Awesome
# for _ in range(int(input())):
#     on = sum([b == '1' for b in bin(int(input().strip()) - 1)[2:]])
#     if on & 1:
#         print('Louise')
#     else:
#         print('Richard')

# Use bit operation

'''
def closest_search(power_of_2, lo, hi, N):

    while lo < hi:
        mid = (lo + hi) // 2
        if N < power_of_2[mid]:
            hi = mid - 1
        elif power_of_2[mid] < N:
            lo = mid + 1
        else:
            return mid
    return lo - 1


power_of_2 = [2 ** i for i in range(1, 64)]
for _ in range(int(input())):
    N = int(input())
    cnt = 0
    if N in power_of_2:
        while N != 1:
            N /= 2
            cnt += 1
            # print('\t', N, cnt)
    else:
        while N > 3:
            closest_val = closest_search(power_of_2, 0, len(power_of_2) - 1, N)
            print(N, power_of_2[closest_val])
            N -= power_of_2[closest_val]
            cnt += 1
            print('\t', N, cnt)
            if N in power_of_2:
                while N != 1:
                    N /= 2
                    cnt += 1
                    print('\t\t', N, cnt)

        while N > 1:
            N -= 2
            cnt += 1
            print('-->> \t\t', N, cnt)

    if cnt % 2 == 1:
        print('Louise')
    else:
        print('Richard')
'''

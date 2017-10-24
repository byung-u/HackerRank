#!/usr/bin/env python3
MAX_E = 32


def next_power_of_2(n):
    for i in range(MAX_E):
        if e_2[i] > n:
            return e_2[i]


e_2 = [2 ** i for i in range(1, MAX_E + 1)]
for _ in range(int(input())):
    a, b = list(map(int, input().strip().split()))
    np = next_power_of_2(a ^ b)
    np = np - 1
    print(a & (~(np)))


"""
Simple O(1) solution:
XOR a and b. Find its next power of 2. Subtract 1. Flip its bits and AND with either a or b.
a & ~(nextpowerof2(a^b)-1)


ukale about a year ago
Let's say a and b are:

a = 26 = 011010
b = 40 = 101000

The leftmost 1 bit of b is to the left of the leftmost 1 bit of a.
So, there is a power of 2 that lies between a and b - namely,
32 (100000) which when ANDed with anything before it will result in 0. This will make the final result 0.


However, if a and b were
a = 42 = 101010
b = 57 = 111001
their leftmost 1 bits are aligned (are in the same bit position).
If we temporarily ignore this 1 bit in both, we have:

a = 01010
b = 11001

Again there exists a power of 2,
namely 16 (10000) that lies between these two sub-values that will eventually zero out the AND product in these bits.

The ANDproduct of the range [101010, 111001] is 100000. In other words, ANDing the range [101010, 111001] is equivalent to preserving the ALL leftmost ALIGNED bits (both 1s and 0s) and zeroing out all bits starting with the first non-aligned bit.

To zero-out all bits starting with the first non-aligned bit, we need to AND these bits with 0s.

To do so, we first a XOR b to get 10011. These bits will have to be zeroed-out. Next, we get the smallest power of 2 larger than this XOR value which happens to be 100000. Subtracting 1, we get 11111, and then finally inverting the bits, we get 11111111111111111111111111100000 (32-bit).

Now, this value ANDed with either A or B will produce the final AND product.

"""


# wrong answer
'''
    res = []
    while a > 1:
        for i in range(len(e_2)):
            if e_2[i] > a:
                a = a - e_2[i - 1]
                res.append(e_2[i-1])
                print(res)
                break
    print(reduce(lambda x, y: x + y, res))
'''

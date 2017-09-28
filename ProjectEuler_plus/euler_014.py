#!/usr/bin/env python3

def collatz_sequence(x):
    seq = [x]
    if x < 1:
        return []
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        seq.append(x)    # Added line
    return seq

t = int(input())
for a0 in range(t):
    n = int(input())
    print(len(collatz_sequence(n)))

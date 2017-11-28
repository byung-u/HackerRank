#!/usr/bin/env python3

input_b = bin(int(input()))[2:]
if input_b == '0':
    print(1)
else:
    print(2 ** sum([b == '0' for b in input_b]))

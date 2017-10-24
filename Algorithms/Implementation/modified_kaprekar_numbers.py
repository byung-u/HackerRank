#!/usr/bin/env python3

#unit = 1
#Kaprekar = []
#for i in range(1, 100000):
#    if i == unit:
#        unit *= 10
#    if i == (i ** 2 // unit) + (i ** 2 % unit):
#        Kaprekar.append(i)
p = int(input())
q = int(input())

unit = 10 ** (len(str(p)))
Kaprekar = []
for i in range(p, q + 1):
    if i == unit:
        unit *= 10
    if i == (i ** 2 // unit) + (i ** 2 % unit):
        Kaprekar.append(i)
if len(Kaprekar) == 0:
    print('INVALID RANGE')
else:
    print(' '.join(list(map(str, Kaprekar))))

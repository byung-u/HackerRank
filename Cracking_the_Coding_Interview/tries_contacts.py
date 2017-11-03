#!/usr/bin/env python3
from bisect import insort_left, bisect_left, bisect_right


names = []
for _ in range(int(input().strip())):
    op, contact = input().strip().split(' ')
    cnt = 0
    if op == 'add':
        insort_left(names, contact)
    else:
        next_contact = contact[0:-1] + chr(ord(contact[-1]) + 1)
        start = bisect_left(names, contact)
        end = bisect_right(names, next_contact)
        print(end - start)


'''
# Slow
names = []
for _ in range(int(input().strip())):
    op, contact = input().strip().split(' ')
    cnt = 0
    if op == 'add':
        names.append(contact)
    elif op == 'find':
        for n in names:
            if n.startswith(contact):
                cnt += 1
        print(cnt)
'''

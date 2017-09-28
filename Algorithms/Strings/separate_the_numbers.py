#!/usr/bin/env python3
import sys


# Success
for _ in range(int(input())):
    n = input()
    len_n = len(n)
    for i in range(0, len_n // 2):
        num = int(n[0:i+1])
        temp = str(num)
        while len(temp) < len_n:
            num += 1
            temp = '%s%d' % (temp, num)
        if temp == n:
            print('YES', n[0:i+1])
            break
    else:
        print('NO')



def failed1():
    for _ in range(int(input())):
        N = input()
        if N[0:2] == '01':
            if N[2] != '2':
                print('NO')
                continue
        found = False
        for i in range(0, len(N) // 2):
            temp = []
            start = 0
            n = int(N[0:i+1])
            temp.append(n)
            n_next = n + 1
            temp.append(n_next)
            while start >= 0:
                str_n_next = str(n_next)
                start = N.find(str_n_next, start)
                print(start)
                if start != -1 and str_n_next == N[-(len(str_n_next)):]:
                    print('YES %s' % (min(temp)))
                    found = True
                    break
                n_next += 1
                temp.append(n_next)
            if found == True:
                break
        else:
            print('NO')

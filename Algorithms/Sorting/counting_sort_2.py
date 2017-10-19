#!/usr/bin/env python3

def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
        counter[i] += 1
    print(counter)
    print(len(counter))

    ndx = 0;
    for i in range(len(counter)):
        while 0 < counter[i]:
            aList[ndx] = i
            ndx += 1
            counter[i] -= 1

n = int(input().strip())
ar = list(map(int, input().strip().split()))

# solution 1
# print(' '.join(list(map(str, sorted(ar)))))

countingsort(ar, n)
print(' '.join(list(map(str, sorted(ar)))))


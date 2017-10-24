#!/usr/bin/env python3
from functools import reduce

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    if N % 2 == 0:
        print(0)
        continue

    res = [arr[i] for i in range(0, N, 2)]
    print(reduce(lambda x, y: x ^ y, res))

"""
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    if N % 2 == 0:
        print(0)
        continue

    cnt = Counter()
    for i in range(1, N + 1):
        for j in range(0, N):
            if len(arr[j:i+j]) != i:
                continue
            for c in arr[j:i+j]:
                cnt[c] += 1
    print(arr)
    print(cnt)
    res = [k for k, v in cnt.items() if v % 2 == 1]
    if len(res) == 0:
        print(0)
    else:
        print(reduce(lambda x, y: x ^ y, res))
"""


'''
# XOR
#   X ^ X = 0
#   X ^ 0 = X
#   0 ^ 0 = 0

    # Too slow (naive way)
    # tc = [reduce(lambda x, y: x ^ y, arr[j:i+j]) for i in range(1, N + 1) for j in range(0, N) if len(arr[j:i+j]) == i]
    # print(reduce(lambda x, y: x ^ y, tc))


# Explanation


david_david188 about a year ago
Explanation: Basic Rules 1. A^0=A -> Rule 1 2. A^A=0 -> Rule 2 3. A^(B^C)=(A^B)^C -> Rule 3
Considering the above rules

Now

Case 1 : Array length 3 (odd)

input is
1 2 3

1^2^3^(1^2)^(2^3)^(1^2^3)

now count each digit
1 - 3 counts (zeroth position)
2 - 4 counts (first position)
3 - 3 counts    (second position)

so we can rewrite the above as

(1^1)^1^(2^2)^(2^2)^(3^3)^3  -> applying Rule 3
0^1^0^0^3 -> applying Rule 1
1^3 -> applying Rule 2
=> Result = 2

So if the array length is odd then it is enough to XOR the 0,2,.... positions

Case 2 : Array length 4 (even)

input is
4 5 7 3 (for easy understanding I am changing last 5 to 3)

4^5^7^3^(4^5)^(5^7)^(7^3)^(4^5^7)^(5^7^3)^(4^5^7^3)

4 - 4 counts
5 - 6 counts
7 - 6 counts
3 - 4 counts

since all the counts are even the result is 0.
'''

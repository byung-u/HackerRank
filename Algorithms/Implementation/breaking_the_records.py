#!/usr/bin/env python3

def getRecord(S):
    h, l = S[0], S[0]
    h_cnt, l_cnt = 0, 0
    for s in S:
        if s > h:
            h_cnt += 1
            h = s
        elif s < l:
            l_cnt += 1
            l = s
    return [h_cnt, l_cnt]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

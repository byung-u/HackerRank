#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    S = input()
    k = input()
    len_k = len(k)
    ret = [i for i in range(len(S) - len_k + 1) if S[i:i+len_k] == k]
    if len(ret) == 0:
        print((-1, -1))
    else:
        for r in ret:
            print((r, r+len_k - 1))

    # for r in re.finditer(k, S):
    #     print(r.start(), r.end())
    # print(m.start())
    # print(m.end())


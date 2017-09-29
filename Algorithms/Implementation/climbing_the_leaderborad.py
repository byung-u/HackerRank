#!/usr/bin/env python3

import sys
from collections import Counter, OrderedDict

def bin_search(num, s_key, lo, hi):
    if hi < lo:
        return lo
    mid = (lo + hi) // 2
    if num > s_key[mid]:
        return bin_search(num, s_key, lo, mid - 1)
    else:
        return bin_search(num, s_key, mid + 1, hi)

def get_closest_key_idx(a, s_key):
    return bin_search(a, s_key, 0, len(s_key) - 1)

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

score_cnt = Counter()
for s in scores:
    score_cnt[s] += 1
sc_dict = OrderedDict(sorted(score_cnt.items(), reverse=True))
sc = list(sc_dict.items())
s_key = list(sc_dict.keys())
len_sc = len(sc)
max_s = max(scores)
min_s = min(scores)
for a in alice:
    if a < min_s:
        print(len_sc + 1)
    elif a == min_s:
        print(len_sc)
    elif a >= max_s:
        print(1)
    else:
        if score_cnt[a] > 0:
            print(list(sc_dict.keys()).index(a) + 1)
        else:
            idx = get_closest_key_idx(a, s_key)
            print(idx + 1)

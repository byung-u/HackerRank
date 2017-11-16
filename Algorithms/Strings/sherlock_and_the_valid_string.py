#!/usr/bin/env python3
from collections import Counter, OrderedDict, defaultdict
from operator import itemgetter


S = Counter(input().strip())
cnt = defaultdict(int)
for k, v in S.items():
    cnt[v] += 1
common_val = max(cnt.items(), key=itemgetter(1))[0]  # cnt -> key means S -> values
words = OrderedDict(S)
possible_del = 1
for k, v in words.items():
    if v == common_val:
        continue
    elif v == 1:
        possible_del -= 1
    elif v - 1 == common_val:
        possible_del -= 1
    else:
        print('NO')
        break

    if possible_del < 0:
        print('NO')
        break
else:
    print('YES')

#!/usr/bin/env python3


all_cases = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
             [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
             [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
             [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
             [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
             [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
             [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
             [[2, 7, 6], [9, 5, 1], [4, 3, 8]], ]

s = []
for s_i in range(3):
    s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
    s.append(s_t)

diffs = [sum([abs(cases[i][j] - s[i][j]) for i in range(0, 3) for j in range(0, 3)]) for cases in all_cases]
print(min(diffs))

# Origin code
# for cases in all_cases:
#     diff = 0
#     for i in range(0, 3):
#         for j in range(0, 3):
#             diff += abs(cases[i][j] - s[i][j])
#     diffs.append(diff)
#
# tranpose sample
# seeds.append([list(t) for t in list(zip(*seed))])

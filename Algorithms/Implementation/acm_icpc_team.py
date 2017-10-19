#!/usr/bin/env python3
from collections import defaultdict


N, M = list(map(int, input().strip().split()))
topics = [int(input().strip(), 2) for _ in range(N)]
d = defaultdict(int)
for i in range(0, N - 1):
    for j in range(i + 1, N):
        d[bin(topics[i] | topics[j]).count("1")] += 1
print(max(d, key=int))
print(d[max(d, key=int)])


'''
# Wrong Solutions.


N, M = list(map(int, input().strip().split()))
topics = [int(input().strip(), 2) for _ in range(N)]
res = [topics[i] | topics[j] for i in range(0, N - 1) for j in range(i + 1, N)]
res = sorted(res)
print(res[0:10])
mr = floor(log(max(res) + 1, 2))
mr_list = [r for r in res if floor(log(r + 1, 2)) == mr]
print(mr)
print(len(mr_list))

# res = [(i, j) for i in range(0, N - 1) for j in range(i + 1, N)]
# print(res)
# print(M)
# print(len(res))
sys.exit(1)
#for i in range(0, N - 1):
#    for j in range(i + 1, N):
#        if topics[i] | topics[j] == e
#            print(i, j, topics[i] + topics[j])
#res = [(topics[i] + topics[j]) for i in range(0, N - 1) for j in range(i + 1, N) if topics[i] + topics[j] < e]
#print(res)
#
sys.exit(1)
#for i in range(0, N - 1)
#    for j in range(i + 1, N):
#        if topics[i] + topics[j] < e
#    # print(int(t, 2))


sys.exit(1)
# print(topics)

solve = []
for i in range(N - 1):
    for j in range(i + 1, N):
        solve.append([(int(topics[i][k]) | int(topics[j][k])) for k in range(M)])

cnt = Counter()
for s in solve:
    cnt[s.count(1)] += 1

print(max(cnt, key=int))
print(cnt[max(cnt, key=int)])
'''

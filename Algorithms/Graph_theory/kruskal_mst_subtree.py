#!/usr/bin/env python3
from operator import itemgetter
# reference
# https://github.com/ynyeh0221/HackerRank/blob/master/Kruskal%20(MST):%20Really%20Special%20Subtree.py


def Kruskal(node, edge):
    cost = 0
    while edge:
        if ( (edge[0][0] not in node[edge[0][1] - 1]) or
             (edge[0][1] not in node[edge[0][0] - 1])):

            node[edge[0][0] - 1] = node[edge[0][0] - 1] | node[edge[0][1] - 1]
            node[edge[0][1] - 1] = node[edge[0][0] - 1] | node[edge[0][1] - 1]

            for i in node[edge[0][0] - 1]:
                node[i - 1] = node[edge[0][0] - 1]
            cost += edge[0][2]

        edge.pop(0)
    print(cost)


t = input().split()
N, M = int(t[0]), int(t[1])
edge = [list(map(int, input().split())) for _ in range(M)]
edge = sorted(edge, key=itemgetter(2))
node = [set([i]) for i in range(1, N + 1)]

Kruskal(node, edge)

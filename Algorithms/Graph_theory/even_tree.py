#!/usr/bin/env python3
# Understanding problem with this comment
# https://www.hackerrank.com/challenges/even-tree/forum/comments/185759
from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges[to_node].append(from_node)

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.edges[node]:
                self.dfs(n, visited)
        return visited


N, M = list(map(int, input().split()))
node = [list(map(int, input().split())) for _ in range(M)]

g = Graph()
for n in node:
    g.add_node(n[0])
    g.add_edge(n[0], n[1])

cnt = 0
visited = []
for n in g.nodes:
    v = g.dfs(n, [])
    # print(v)
    if len(v) % 2 == 0:
        cnt += 1
print(cnt)

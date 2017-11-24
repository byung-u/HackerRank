#!/usr/bin/env python3
import sys
from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list) 
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.edges[node]:
                self.dfs(n, visited)
        return visited


sys.setrecursionlimit(10000)

n, p = (map(int, input().split()))
astronauts = [list(map(int, input().split())) for _ in range(p)]

g = Graph()
for astronaut in astronauts:
    g.add_node(astronaut[0])
    g.add_edge(astronaut[0], astronaut[1])

country = set()
visited_node = []
for node in g.nodes:
    if node in visited_node:
        continue
    v = g.dfs(node, [])
    visited_node.extend(v)
    country.add(tuple(sorted(v)))

l = [len(c) for c in country]
alone = n - sum(l)
for i in range(alone):
    country.add(tuple([i]))
l = [len(c) for c in country]

total = 0
for i in range(1, len(country)):
    total += l[i - 1] * l[i]
    l[i] += l[i - 1]
print(total)

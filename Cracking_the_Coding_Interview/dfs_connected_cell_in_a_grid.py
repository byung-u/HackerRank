#!/usr/bin/env python3
from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        # self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph.edges[node]:
            dfs(graph, n, visited)
    return visited


# Main
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

g = Graph()
for i in range(n):
    for j in range(m):
        node = str(i) + str(j)
        g.add_node(node)
        if grid[i][j] == 0:
            continue
        for x, y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,   1):
            if 0 <= i + x < n and 0 <= j + y < m:
                if grid[i + x][j + y] == 1:
                    neighbor = str(i + x) + str(j + y)
                    g.add_edge(node, neighbor, grid[i + x][j + y])

largest = 0
for n in g.nodes:
    visited = dfs(g, n, [])
    if largest < len(visited):
        largest = len(visited)
print(largest)

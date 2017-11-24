#!/usr/bin/env python3
from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges[to_node].append(from_node)
        self.edges[from_node].append(to_node)

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.edges[node]:
                self.dfs(n, visited)
        return visited


for _ in range(int(input().strip())):
    n, m, c_lib, c_load = (map(int, input().split()))
    libs = c_lib * n
    nodes = [list(map(int, input().split())) for _ in range(m)]
    lib_and_repair = [0] + [c_lib] * n  # 0, 1, 2, 3 ... n
    if m == 0 or c_lib < c_load:
        print(libs)
        continue

    g = Graph()
    for node in nodes:
        g.add_node(node[0])
        g.add_edge(node[0], node[1])

    len_nodes = len(g.nodes)
    for node in g.nodes:
        v = g.dfs(node, [])
        len_v = len(v)
        if lib_and_repair[v[0]] == c_lib:
            for i in range(1, len_v):
                temp = lib_and_repair[v[i]]
                lib_and_repair[v[i]] = c_load
                # print(v, temp, '->', lib_and_repair[v[i]], v[i])
        if len_v == len_nodes:
            break
    print(min(libs, sum(lib_and_repair)))
    # print((libs, sum(lib_and_repair)))

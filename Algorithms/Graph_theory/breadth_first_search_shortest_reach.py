#!/usr/bin/env python3
from queue import Queue
from collections import defaultdict


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.nodes)]
        unvisited = set([i for i in range(self.nodes)])
        q = Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(root)
        print(" ".join(map(str, distances)))


for i in range(int(input())):
    n, m = list(map(int, input().split()))
    graph = Graph(n)
    for i in range(m):
        x, y = list(map(int, input().split()))
        graph.connect(x - 1, y - 1)  # Different start idx node and array
    s = int(input())
    graph.find_all_distances(s - 1)

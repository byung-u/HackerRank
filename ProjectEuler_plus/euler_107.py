#!/usr/bin/env python3
from operator import itemgetter
# reference
# https://inanemathgeek.wordpress.com/2012/10/15/euler-107-back-to-python/

class DisjointSet (dict):
    def add(self, item):
        self[item] = item

    def find(self, item):
        parent = self[item]
        while self[parent] != parent:
            parent = self[parent]
        self[item] = parent
        return parent

    def union(self, item1, item2):
        self[item2] = self[item1]

def kruskal(nodes, edges):
    forest = DisjointSet()
    mst = []
    for n in nodes:
        forest.add(n)

    sz = len(nodes) - 1

    for e in sorted(edges, key=itemgetter(2)):
        n1, n2, _ = e
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            if sz == 0:
                return mst
            forest.union (t1, t2)

def convert2Edges (m):
    e = []
    for i in range (1, len(m)):
        for j in range (0, i):  # check half of 2d array
            if m[i][j] != 0:
                e.append([str(i), str(j), m[i][j]])
    return e

def generateNodes (m):
    return [str(i) for i in range(0, len(m))]

def calcWeight(e):
    w = 0
    for i in e:
        w += i[2]
    return w


t = input().split()
N, M = int(t[0]), int(t[1])
edge = [list(map(int, input().split())) for _ in range(M)]
edge = sorted(edge, key=itemgetter(2))
node = [i for i in range(1, N + 1)]

e1 = kruskal(node, edge)
print(calcWeight(e1))

#!/usr/bin/env python3
import sys

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    if head:
        N = Node(data=data)
        N.next = head
        return N
    else:
        head = Node(data=data)
        return head


def test():
    ll = Node
    m = ll(data=1, next_node=ll(data=2, next_node=ll(data=3)))
    Insert(m, 9)

    sys.exit(1)
    print(m.data)
    print(m.next.data)
    print(m.next.next.data)

    print(m)
    print(m.next)
    print(m.next.next)





if __name__ == '__main__':
    test()

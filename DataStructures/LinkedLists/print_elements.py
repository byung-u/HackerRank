#!/usr/bin/env python3
import sys

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)


def test():
    ll = Node
    m = ll(data=1, next_node=ll(data=2, next_node=ll(data=3)))
    print(m.data)
    print(m.next.data)
    print(m.next.next.data)

    print(m)
    print(m.next)
    print(m.next.next)


if __name__ == '__main__':
    test()

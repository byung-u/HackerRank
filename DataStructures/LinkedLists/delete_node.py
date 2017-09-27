#!/usr/bin/env python3
import sys

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    if head is None:
        head = Node(data=data)
    elif position == 0:
        tmp = head
        head = Node(data=data)
        head.next = tmp
    else:
        cur = head
        for _ in range(0, position - 1):
            cur = cur.next
            if cur is None:
                break
        if cur is None:
            head.next = Node(data=data)
        else:
            tmp = cur.next
            cur.next = Node(data=data)
            cur.next.next = tmp
    return head


def Delete(head, position):
    if position == 0:
        head = head.next
    elif head:
        cur = head
        for _ in range(0, position - 1):
            cur = cur.next
            if cur is None:
                break
        if cur:
            cur.next = cur.next.next
    return head


def test():
    head = None
    for i in range(int(input())):
    for i in range(int(input())):
        length = input()
        S = list(map(int, input().split()))
        pos = int(input())
        print(S, pos)


'''
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
'''

if __name__ == '__main__':
    test()

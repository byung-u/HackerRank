#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head:
            cur = head
            while cur.next:
                cur = cur.next
            N = Node(data=data)
            cur.next = N
            return head
        else:
            head = Node(data=data)
            return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head, data)
mylist.display(head);

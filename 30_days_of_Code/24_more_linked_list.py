#!/usr/bin/env python3
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 

    def insert(self, head, data):
        p = Node(data)           
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head  

    def display(self, head):
        current = head
        while current:
            print(current.data, end = ' ')
            current = current.next

    def removeDuplicates(self, head):
        temp = set()
        current = head
        new_head = None
        while current:
            temp.add(current.data)
            current = current.next
        current = head
        while current:
            if current.data in temp:
                new_head = self.insert(new_head, current.data)
                temp.remove(current.data)
            current = current.next
        return new_head

    def removeDuplicates2(self, head):
        current = head
        li = [head.data]

        while current.next: # exists
            if current.next.data in li:
                # delete it and reset pointer
                pointer = current.next.next
                del current.next
                current.next = pointer
            else:
                li.append(current.next.data)
                current = current.next
        return head


mylist =  Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)    
mylist.display(head); 
print()
head = mylist.removeDuplicates(head)
mylist.display(head); 
print()

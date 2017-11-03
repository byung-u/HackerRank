#!/usr/bin/env python3

def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False

# Much better to understand
def has_cycle(head):
    fast = head;
    while (fast != None and fast.next != None):
        fast = fast.next.next;
        head = head.next;

        if(head == fast):
            return True;

    return False;

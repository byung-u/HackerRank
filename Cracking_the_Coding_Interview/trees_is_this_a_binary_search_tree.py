#!/usr/bin/env python3

def check_in_BST(root, min_val, max_val):
    if root is None:
        return True

    if root.data < min_val or root.data > max_val:
        return False

    return (check_in_BST(root.left, min_val, root.data -1) and
            check_in_BST(root.right, root.data + 1, max_val))

def checkBST(root):
    return check_in_BST(root, 0, 10000)  # max value: 10 ** 4

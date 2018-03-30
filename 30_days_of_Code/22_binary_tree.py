#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        height_left = 0
        height_right = 0
        if root.left is not None:
            height_left = self.getHeight(root.left) + 1
        if root.right is not None:
            height_right = self.getHeight(root.right) + 1
        return max(height_right, height_left)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)

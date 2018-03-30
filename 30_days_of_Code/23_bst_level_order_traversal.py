#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, data):
        self.right = self.left=None
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
                cur=self.insert(root.right, data)
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

    def levelOrder(self, root):
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)

#!/usr/bin/env python2
import sys
def preOrder(root):
    if root is None:
        return
    sys.stdout.write(str(root.data) + ' ')
    preOrder(root.left)
    preOrder(root.right)


#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    # \1  <- found 1st
    m = re.search(r'([^\W_])\1+', input())
    print(m[1] if m else -1)

#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    print('\n'.join(filter(None, re.split('[,.]', input()))))

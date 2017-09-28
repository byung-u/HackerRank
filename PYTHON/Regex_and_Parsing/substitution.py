#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        s = re.sub('\s&&\s', ' and ', re.sub('\s\|\|\s', ' or ', s))
        print(re.sub('\s&&\s', ' and ', re.sub('\s\|\|\s', ' or ', s)))

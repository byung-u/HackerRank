#!/usr/bin/env python3
import sys
import re

for _ in range(int(input().strip())):
    s = input().strip()
    print(len(set(list(s))))

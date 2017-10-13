#!/usr/bin/env python3

import re

n = input()
print(bool(re.search(r'^[1-9][0-9]{5}$', n)) and bool(len(re.findall(r'(?=(\d)\d\1)', n)) < 2))

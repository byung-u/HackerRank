#!/usr/bin/env python3

import re
import email.utils

for _ in range(int(input())):
    n = input()
    e = email.utils.parseaddr(n)
    if re.match('^[a-zA-Z][a-zA-Z0-9-_\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', e[1]) is None:
        continue
    print(n)

#!/usr/bin/env python3

import re

arr = [ 'lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.comzxc','jak?989@hackerrank.com',]
for a in arr:
    print(a, re.match('[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$', a))
    # print(a, re.match('(^[a-zA-Z-_])@(\w{3})\.(\w{3})', a))

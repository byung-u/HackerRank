#!/usr/bin/env python3
import sys
import re

S = list(map(str, input().strip()))
SS = sorted(set([s.lower() for s in S if re.match('[a-zA-Z]', s)]))
if len(SS) == 26:
    print('pangram')
else:
    print('not pangram')

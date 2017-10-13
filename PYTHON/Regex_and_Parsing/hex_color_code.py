#!/usr/bin/env python3

import re


for _ in range(int(input())):
    for m in re.finditer(r'(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[,;)])', input()):
        print(m.group())

    # It was solve the problem, but length check logic is not a good idea.
    '''
    if re.search('^[^#](\w+|\s+)', n) is None:
        continue
    m = re.findall('[\#][0-9a-fA-F]{3,6}', n)
    for hc in m:
        len_hc = len(hc)
        if len_hc == 5 or len_hc == 6:
            continue
        print(hc)
    '''

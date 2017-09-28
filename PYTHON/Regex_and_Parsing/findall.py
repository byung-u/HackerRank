#!/usr/bin/env python3
import sys
import re

if __name__ == '__main__':
    input_str = input()
    ret = ([r.group(0) for r in re.finditer(r'([aeiou])+', input_str, re.I) if len(r.group(0)) > 1])
    if len(ret) == 0:
        print(-1)
    else:
        if ret[-1] == input_str[(-1 * len(ret[-1])):]:
            ret.pop()
        print('\n'.join(ret))

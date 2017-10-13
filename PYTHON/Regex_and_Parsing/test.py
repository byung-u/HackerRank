#!/usr/bin/env python3

import re

m = re.findall('(?<=abc)def', 'abcdef')
print(m)
m = re.findall('(?<=abc)def', 'zjwdef')
print(m)

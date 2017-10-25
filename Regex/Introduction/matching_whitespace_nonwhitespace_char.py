#!/usr/bin/env python3

import sys
import re

#12 10 11
#2312 10 11sdf
Regex_Pattern = r'^\S{2,}\s{1}\S{2}\s{1}\S{2,}$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())

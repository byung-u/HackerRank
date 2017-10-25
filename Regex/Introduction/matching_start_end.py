#!/usr/bin/env python3

import sys
import re

# www.hackerrank.com
# http://www.hackerrank.com
# Regex_Pattern = r'^\w{3}\W{1}\w+\W{1}\w{3}$'
Regex_Pattern = r'^\d{1}\w{4}\.$'


print(str(bool(re.search(Regex_Pattern, input()))).lower())

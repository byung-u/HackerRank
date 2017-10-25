#!/usr/bin/env python3

import sys
import re

regex_pattern = r'^.{3}\..{3}\..{3}\..{3}$'

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

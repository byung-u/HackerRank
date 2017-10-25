#!/usr/bin/env python3

import sys
import re

# Regex_Pattern = r'\d+\D+\d+\D+\d+'
Regex_Pattern = r'^\d{2}\D{1}\d{2}\D{1}\d{4,}$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())

#!/usr/bin/env python3

import sys
import string

h = list(map(int, input().strip().split(' ')))
word = input().strip()
L = list(string.ascii_lowercase)

wi = [h[L.index(w)] for w in word]
print(len(word) * max(wi))



#!/usr/bin/env python3

S = input().strip()

try:
    print (int(S))
except ValueError:
    print ("Bad String")

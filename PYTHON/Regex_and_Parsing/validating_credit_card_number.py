#!/usr/bin/env python3

import re

# It is amazing
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")

def normal_answer():
    for _ in range(int(input())):
        n = input()
        m = re.match(r'([\d]{16}|^[0-9]{4}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}$)', n)
        if m is None:
            print('Invalid')
            continue
        n = n.replace('-', '')
        m = re.match(r'(?!.*?([0-9])\1{3,})(?=(^[4-6]){1})(?=[\d]{16})', n)
        if m is None:
            print('Invalid')
        else:
            print('Valid')

    # m = re.match(r'(?=(^[4-6]){1})', input())
    # m = re.match(r'(?=[\d]{16})', n)
    # m = re.match(r'(?=.*?([0-9])\1{3,})', n)
    # m = re.match(r'(?!([0-9]).*?\1{3,})', n)

    '''
    (?!([a-zA-Z0-9]){1,}.*?\1)
    (?=(.*\d+){3,})
    (?=(.*[A-Z]+){2,})
    (?=^[\d\w]{10}$)', input())
    '''


'''
    # It must start with a 4, 5, 6
    # -->  m = re.match(r'(?=(^[4-6]){1})', input())
    # It must contain exactly 16 digits.
    # It must only consist of digits (0-9).
    # It may have digits in groups of 4, separated by one hyphen "-".
    # [1]
    # --> m = re.match(r'([\d]{16}|[0-9]{4}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4})', n)
    # [2]
    # -->  n = n.replace('-', '')
    # --> m = re.match(r'([\d]{16})', n)
    # It must NOT use any other separator like ' ' , '_', etc.
    # It must NOT have 4 or more consecutive repeated digits.
    # --> m = re.match(r'([0-9]).*?\1{3,}', n)

'''

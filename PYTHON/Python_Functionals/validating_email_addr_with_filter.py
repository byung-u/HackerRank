#!/usr/bin/env python3

import re

def fun(s):
    if re.match('[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$', s) is None:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#!/usr/bin/env python3
import sys

# ['{', '[', '(', ')', ']', '}']
# [123,  91,  40,  41, 93,  125]
def is_matched(expression):
    arr = list(expression)
    if arr[0] == '}' or arr[0] == ']' or arr[0] == ')':  # It was a key.
        return False
    found = True
    while found == False:
        diff = abs(ord(arr[0]) - ord(arr[-1]))
        if diff < 3 and diff != 0:
            arr.pop(0)  # 0
            arr.pop()   # last
        else:
            found = False

    while len(arr) != 0:
        for i in range(0, len(arr) - 1):
            diff = abs(ord(arr[i + 1]) - ord(arr[i]))
            if diff < 3 and diff != 0:
                arr.pop(i)  # i
                arr.pop(i)  # i + 1
                break
        else:
            return False
    return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
'''
# Wrong answer
for _ in range(int(input().strip())):
    s = list(input().strip())
    half_len_s = len(s) // 2
    ord_s = list(map(ord, s))
    left = ord_s[0:half_len_s]
    right = list(reversed(ord_s[half_len_s:]))
    for i in range(half_len_s):
        if right[i] - left[i] > 3:
            print('NO')
            break
    else:
        print('YES')

'''

#!/usr/bin/env python3
#  : 32  -> space
# !: 33
# ': 39
# (: 40, ): 41
# ,: 44
# -: 45
# .: 46
# 0: 48, 9: 57
# :: 58
# ;: 59
# ?: 63
# A: 65, Z: 90
# a: 97, z: 122
n = int(input().strip())
cipher = list(map(int, input().strip().split()))

plain_text = [32, 33] + list(range(39, 41 + 1)) + list(range(44, 46 + 1)) + list(range(48, 59 + 1)) + [63] + list(range(65, 90 + 1)) + list(range(97, 122 + 1))
all_key = list(range(97, 122 + 1))
password = []
for a in all_key:
    for c in cipher[0::3]:
        if a ^ c not in plain_text:
            break
    else:
        password.append(chr(a))
        break

for a in all_key:
    for c in cipher[1::3]:
        if a ^ c not in plain_text:
            break
    else:
        password.append(chr(a))
        break

for a in all_key:
    for c in cipher[2::3]:
        if a ^ c not in plain_text:
            break
    else:
        password.append(chr(a))
        break
print(''.join(password))

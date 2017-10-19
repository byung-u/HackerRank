#!/usr/bin/env python3
# NUMBERS
unit = ['', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ten = ['', '', 'twenty', 'thirty', 'forty',
       'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


H = int(input().strip())
M = int(input().strip())
if M == 0:
    print(unit[H], "o' clock")
elif M == 1:
    print('one minute past', unit[H])
elif M == 15:
    print('quarter past', unit[H])
elif M == 30:
    print('half past', unit[H])
elif M == 45:
    print('quarter to', unit[H + 1])
elif M < 30:
    if M < 10:
        print(unit[M], 'minutes past', unit[H])
    elif 10 <= M < 20:
        print(teen[M-10], 'minutes past', unit[H])
    else:
        print(ten[int(str(M)[0])], unit[int(str(M)[1])], 'minutes past', unit[H])
else:  # M > 30
    M = 60 - M
    if M == 1:
        print('one minute to', unit[H + 1])
    elif M < 10:
        print(unit[M], 'minutes to', unit[H + 1])
    elif 10 <= M < 20:
        print(teen[M-10], 'minutes to', unit[H + 1])
    else:
        print(ten[int(str(M)[0])], unit[int(str(M)[1])], 'minutes to', unit[H + 1])

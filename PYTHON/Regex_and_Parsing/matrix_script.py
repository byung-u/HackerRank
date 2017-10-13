#!/usr/bin/env python3

import re

T = list(map(int, input().split()))
N, M = T[0], T[1]
arr = [input() for _ in range(N)]
res = ''.join([a[m] for m in range(0, M) for a in arr])
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", res))



'''
(?<=...)
    Matches if the current position in the string is preceded by a match for ... that ends at the current position.
    This is called a positive lookbehind assertion.
    (?<=abc)def will find a match in abcdef,
    since the lookbehind will back up 3 characters and check if the contained pattern matches.
    The contained pattern must only match strings of some fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} are not.
    Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the search() function rather than the match() function:

'+'
    Causes the resulting RE to match 1 or more repetitions of the preceding RE.
    ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.



(?=...)
    Matches if ... matches next, but doesn’t consume any of the string.
    This is called a lookahead assertion.
    For example, Isaac (?=Asimov) will match
    'Isaac ' only if it’s followed by 'Asimov'.
'''

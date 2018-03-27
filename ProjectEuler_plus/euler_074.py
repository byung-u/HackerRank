#!/usr/bin/env python3
from math import factorial

def e74():
    fs = [factorial(i) for i in range(0, 10)]
    # print(fs)
    limit = 1000000
    chain = [0] * (limit + 1)
    for i in range(limit + 1):
        if chain[i] != 0:
            continue
        num = i
        temp = [num]
        while True:
            fsum = sum(list(map(lambda x: fs[int(x)], str(num))))
            if fsum in temp:
                chain[i] = len(temp)
                if chain[fsum] == 0:
                    loop_idx = temp.index(fsum)
                    loop_val = len(temp) - loop_idx
                    # print([i], '->', fsum, loop_idx, len(temp))
                    for j in range(loop_idx, len(temp)):
                        if chain[temp[j]] == 0:
                            chain[temp[j]] = loop_val
                        # print(temp[j], chain[temp[j]],  loop_val)
                # print([i], chain[i], temp, '->', fsum)
                break

            if fsum <= limit and chain[fsum] != 0:
                chain[i] = len(temp) + chain[fsum]
                # print([i], '--->', chain[i], temp, chain[fsum], fsum)
                break
            temp.append(fsum)
            num, fsum = fsum, 0

    for _ in range(int(input().strip())):
        n, l = list(map(int, input().strip().split()))
        result = [i for i in range(n + 1) if chain[i] == l]
        if len(result) == 0:
            print(-1)
        else:
            print(' '.join(map(str, result)))
    return


e74()

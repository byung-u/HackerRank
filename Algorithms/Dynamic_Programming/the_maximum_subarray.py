#!/usr/bin/env python3
# Maximum subarray


for _ in range(int(input().strip())):
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))

    is_minus = True
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        if x < 0:
            is_minus = False
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    if is_minus:
        print(max_so_far, max_ending_here)
    else:
        if max_so_far == max_ending_here:
            if sum([x for x in A if x > 0]) == 0:
                seq_sum = max(max_ending_here, max(A))
            else:
                seq_sum = max(max_ending_here, sum([x for x in A if x > 0]))
            print(max_so_far, seq_sum)
        else:
            seq_sum = sum([x for x in A if x > 0])
            if seq_sum > 0:
                print(max_so_far, seq_sum)
            else:
                print(max_so_far, max(A))

'''
# wrong
    if max_so_far == max_ending_here:
        print(max_so_far, max_ending_here)
    else:
        total = 0
        if max_so_far < 0:
            flag = False
            for x in A:
                if flag == False:
                    if x == max_so_far:
                        flag = True
                        total += x
                else:
                    if x < max_so_far:
                        continue
                    total += x
            print(max_so_far, total)
        else:
            for x in A:
                if x < 0:
                    continue
                total += x
            print(max_so_far, total)
#        if len(A[0:max_ending_here]) == 1:
#            seq_sum = sum([x for x in A[0:max_ending_here]])
#        else:
#            seq_sum = max(sum([x for x in A[0:max_ending_here] if x > 0]),
#                    sum([x for x in A[0:max_ending_here]]) - min(A[0:max_ending_here]))
#
#        print(max_so_far, seq_sum)

    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far, sum([x for x in A[0:max_ending_here] if x > 0]))
'''

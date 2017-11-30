#!/usr/bin/env python3

def simple_solution(s, len_s, t, len_t, k):
    common_len = 0
    for i in range(min(len_s, len_t)):
        if s[i] == t[i]:
            common_len += 1
        else:
            break

    if (len_s + len_t - 2 * common_len) > k:  # case 1
        print('No')
    elif (len_s + len_t - 2 * common_len) % 2 == k % 2:  # case 2
        print('Yes')
    elif (len_s + len_t - k) < 0:  # case 3
        print('Yes')
    else:  # case 4
        print('No')


def check_append_delete_possible(s, len_s, t, len_t, k):
    if s == t:
        if k % 2 == 0:
            print('Yes')
            return 

    common_len = 0
    for i in range(min(len_s, len_t)):
        if s[i] == t[i]:
            common_len += 1
        else:
            break
    # print('[common]:', common_len)

    ls = len_s - common_len
    lt = len_t - common_len
    diff_len = abs(ls - lt)

    if lt == 0:
        total_len = len_s + 1 + common_len + (len_t - common_len)
        # print('[total]', total_len)
        if total_len == k:
            print('Yes')
        elif total_len > k:
            if diff_len > k - diff_len: 
                if (k - diff_len) % 2 == 0:
                    print('Yes')
                    return
            print('No')
        elif (k - total_len) % 2 == 0:
            print('Yes')
        else:
            print('No')
        return
    elif ls == 0:
        if diff_len == k:
            print('Yes')
        elif (k - diff_len) % 2 == 0:
            print('Yes')
        else:
            print('No')
    elif ls + lt <= k:
        if ls + lt == k:
            print('Yes')
        elif (k - (ls + lt)) % 2 == 0:
            print('Yes')
        else:
            total_len = len_s + 1 + common_len + (len_t - common_len)
            if total_len == k:
                print('Yes')
            elif total_len > k:
                print('No')
            elif (k - total_len) % 2 == 0:
                print('Yes')
            else:
                print('No')
        return
    else:
        print('No')


s = input().strip()
t = input().strip()
k = int(input().strip())

check_append_delete_possible(s, len(s), t, len(t), k)
# simple_solution(s, len(s), t, len(t), k)




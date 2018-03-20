#!/usr/bin/env python3
from collections import defaultdict
from operator import itemgetter

d = defaultdict(list)
for n in range(int(input().strip())):
    str_num = input()
    d[len(str_num)].append(str_num)
sorted_d = sorted(d.items(), key=itemgetter(0))
for nums in sorted_d:
    print('\n'.join(sorted(nums[1])))


'''
# slow 4
def insertion_sort(ar):
    for i in range(1, len(ar)):
        # key, key_len = ar[i], len(ar[i])
        key = ar[i]
        j = i - 1
        while j > -1 and key < ar[j]:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j+1] = key
    return ar

# slow 3
def insertion_sort(ar):
    for i in range(1, len(ar)):
        key, key_len = ar[i], len(ar[i])
        j = i - 1
        while j > -1 and ((key_len < len(ar[j])) or (key_len == len(ar[j]) and key < ar[j])):
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j+1] = key
    return ar


n = int(input().strip())
arr = [input() for _ in range(n)]
print('\n'.join(map(str, insertion_sort(arr))))

# slow 2
def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j > -1 and key < ar[j]:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j+1] = key
    return ar


nums = defaultdict(list)
n = int(input().strip())
max_num_len = 0
for _ in range(n):
    num = input().strip()
    len_num = len(num)
    if max_num_len < len_num:
        max_num_len = len_num
    nums[len_num].append(num)


for i in range(max_num_len + 1):
   if len(nums[i]) == 0:
       continue
   print('\n'.join(map(str, insertion_sort(nums[i]))))

# Slow 1
def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j > -1 and int(key) < int(ar[j]):
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j+1] = key
    return ar


# Slow 2
nums = defaultdict(list)
n = int(input().strip())
for _ in range(n):
    num = input().strip()
    nums[len(num)].append(int(num))

mk = max(nums, key=nums.get)
for i in range(mk + 1):
    if len(nums[i]) == 0:
        continue
    print('\n'.join(map(str, sorted(nums[i]))))

# Slow 3
# print('\n'.join(map(str, insertion_sort(ar))))
# print(insertion_sort(ar))
# print('\n'.join(map(str, sorted(arr))))
'''

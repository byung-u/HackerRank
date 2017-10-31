#!/usr/bin/env python3

N = int(input().strip())
arr = [int(i) for i in input().strip().split()]
sorted_arr = sorted(arr)
diff_arr = [sorted_arr[i + 1] - sorted_arr[i] for i in range(0, N - 1)]
min_diff = min(diff_arr)
idx = [i for i in range(len(diff_arr)) if diff_arr[i] == min_diff]
for i in idx:
    print(sorted_arr[i], sorted_arr[i + 1], end=' ')
print()



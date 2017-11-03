#!/usr/bin/env python3

from bisect import insort_left


arr = []
for _ in range(int(input().strip())):
   insort_left(arr, int(input().strip()))
   len_arr = len(arr)
   mid = len_arr // 2
   if len_arr % 2 == 1:
       print(arr[mid] / 1)
   else:
       print((arr[mid] + arr[mid - 1]) / 2)

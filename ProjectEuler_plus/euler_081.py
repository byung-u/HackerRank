#!/usr/bin/env python3
import sys


n = int(input().strip())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

sum_list = [[0 for x in range(n)] for x in range(n)]
sum_list[0][0] = matrix[0][0]
for i in range(1, n):  # set 1st sum of row
    sum_list[0][i] = sum_list[0][i - 1] + matrix[0][i]  
for i in range(1, n):  # set 1st sum of column
    sum_list[i][0] = sum_list[i - 1][0] + matrix[i][0]

for i in range(1, n):
    for j in range(1, n):
        sum_list[i][j] = min(sum_list[i - 1][j], sum_list[i][j -1]) + matrix[i][j]

print(sum_list[n - 1][n - 1])

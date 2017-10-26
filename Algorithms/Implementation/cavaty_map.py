#!/usr/bin/env python3

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = list(input().strip())
    # grid_t = str(input().strip())
    grid.append(grid_t)

hole = []
for y in range(1, n - 1):
    for x in range(1, n - 1):
        center = grid[y][x]
        right = grid[y][x + 1]
        left = grid[y][x - 1]
        up = grid[y + 1][x]
        down = grid[y - 1][x]
        if center > max(right, left, up, down):
            hole.append((y, x))
  
for h in hole:
    grid[h[0]][h[1]] = 'X'
for g in grid:
    print(''.join(g))

#!/usr/bin/env python3


g, erg = [], []
for _ in range(20):
    g.append([int(grid_t) for grid_t in input().strip().split(' ')])

for y in range(20):
    for x in range(20):
        if x < 17:
            erg.append(g[y][x] * g[y][x+1] * g[y][x+2] * g[y][x+3])
        if y < 17:
            erg.append(g[y][x] * g[y+1][x] * g[y+2][x] * g[y+3][x])
        if x >= 3 and y < 17:
            erg.append(g[y][x] * g[y+1][x-1] * g[y+2][x-2] * g[y+3][x-3])
        if x < 17 and y < 17:
            erg.append(g[y][x] * g[y+1][x+1] * g[y+2][x+2] * g[y+3][x+3])

print(max(erg))


'''
c = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    c.append(grid_t)

mtx = copy.copy(c)
m = 0
product = lambda s: reduce(lambda a,b:a * b, s)
for i in range(16):
    for j in range(16):
        m = max(m,product(c[i][j:j+4]))
        m = max(m,product([d[j] for d in mtx[i:i+4]]))
        m = max(m, c[i][j]  *  c[i+1][j+1]  *  c[i+2][j+2]  *  c[i+3][j+3])
        if j >= 3 and i <= 17:
            m = max(m, c[i][j]  *  c[i+1][j-1]  *  c[i+2][j-2]  *  c[i+3][j-3])

m = max(m, c[0][1]  *  c[1][0])
m = max(m, c[0][2]  *  c[1][1]  *  c[2][0])

m = max(m, c[0][18]  *  c[1][19])
m = max(m, c[0][17]  *  c[1][18]  *  c[2][19])

m = max(m, c[18][0]  *  c[19][1])
m = max(m, c[17][0]  *  c[18][1]  *  c[19][2])

m = max(m, c[19][18]  *  c[18][19])
m = max(m, c[17][19]  *  c[18][18]  *  c[19][17])

print(m)
def search_max(x, y, max_val, memo):
    if memo[x][y] is True:
        return max_val

    right, down, r_diag, l_diag = (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)
    ret_right, ret_down, ret_rdiag, ret_ldiag = 0, 0, 0, 0

    if x < 16 and y < 16:

        right = grid[x][y], grid[x][y + 1], grid[x][y + 2], grid[x][y + 3]
        ret_right = search_max(x + 1, y, max_val, memo)
        memo[x + 1][y] = True

        down = grid[x][y], grid[x + 1][y], grid[x + 2][y], grid[x + 3][y]
        ret_down = search_max(x, y + 1, max_val, memo)
        memo[x][y + 1] = True

        # right down diagonal
        r_diag = grid[x][y], grid[x + 1][y + 1], grid[x + 2][y + 2], grid[x + 3][y + 3]
        ret_rdiag = search_max(x + 1, y + 1, max_val, memo)
        memo[x + 1][y + 1] = True
    if x > 16:
        right = grid[x][y], grid[x][y + 1], grid[x][y + 2], grid[x][y + 3]
        ret_right = search_max(x + 1, y, max_val, memo)
        memo[x + 1][y] = True

    if y > 16:
        down = grid[x][y], grid[x + 1][y], grid[x + 2][y], grid[x + 3][y]
        ret_down = search_max(x, y + 1, max_val, memo)
        memo[x][y + 1] = True

    if (x > 2 and y > -1) and (x < 20 and y < 16):  # left down diagonal
        l_diag = grid[x][y], grid[x - 1][y + 1], grid[x - 2][y + 2], grid[x - 3][y + 3]
        ret_ldiag = search_max(x - 1, y + 1, max_val, memo)
        memo[x - 1][y + 1] = True

    chk_val = reduce(lambda x, y: x  *  y, (max(right, down, r_diag, l_diag)))
    if max_val < chk_val:
        max_val = chk_val
        # print(max_val, max(right, down, r_diag))

    chk_val_nested = max(ret_right, ret_down, ret_rdiag, ret_ldiag)
    if max_val < chk_val_nested:
        max_val = chk_val_nested
    return max_val



c = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    c.append(grid_t)

memo = [[False]  *  20]  *  20
result = search_max(0, 0, 0, memo)
print(result)
'''

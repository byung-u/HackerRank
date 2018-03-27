#!/usr/bin/env python3

n = int(input().strip())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

cost = [grid[r][-1] for r in range(n)]

for c in range(n - 2, -1, -1): 
    cost[0] += grid[0][c]
    for r in range(1, n): 
        cost[r] = min(cost[r], cost[r - 1]) + grid[r][c]

    for r in range(n - 2, -1, -1): 
        cost[r] = min(cost[r], cost[r + 1] + grid[r][c])
print(min(cost))
'''
131 673 234 103 | 18
201  96 342 965 |150
630 803 746 422 |111
537 699 497 121 |956
805 732 524  37 |331


# loop 1
131 673 234 121   18
201  96 342 1115 150  [ 965 + 103 < 965 + 150 ] ... start
630 803 746 533  111          
537 699 497 654  956
805 732 524 368  331   ... end

# loop 2
131 673 234 121   18   ... end
201  96 342 1115 150  
630 803 746 533  111           
537 699 497 654  956  [ 654 > 331 + 37 + 121 ]  ... start
805 732 524 368  331
'''

#!/usr/bin/env python3


def check_inner_arr(G, P, C, c, r):

    for line, g in enumerate(G):
        for pos in range(C):
            if g[pos] != P[0][0]:
                continue

            if g[pos: pos + c] == P[0]:
                for i in range(r):
                    if P[i] != G[line + i][pos: pos + c]:
                        break
                else:
                    return True
    return False


t = int(input().strip())
for a0 in range(t):
    R, C = input().strip().split(' ')
    R, C = [int(R), int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r, c = input().strip().split(' ')
    r, c = [int(r), int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)

    if check_inner_arr(G, P, C, c, r) is True:
        print('YES')
    else:
        print('NO')


'''
# Need to check multiple lines and strings
# Can't check this case
                        1
                        7 15
                        111111111111111
                        111111111111111
                        111111111111111
                        111111011111111
                        111111111111111
                        111111111111111
                        101010101010101
                        4 5
                        11111
                        11111
                        11111
                        11110

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    for line, g in enumerate(G):
        pos = g.find(P[0])
        if pos != -1:
            break
    else:
        print('NO')
        continue

    for i in range(r):
        if P[i] != G[line + i][pos: pos + c]:
            print('NO')
            break
    else:
        print('YES')
'''

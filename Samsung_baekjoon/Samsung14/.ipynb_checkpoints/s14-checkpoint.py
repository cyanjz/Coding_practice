from itertools import product
from copy import deepcopy

s = {1 : ([1, 0], [-1, 0], [0, 1], [0, -1]),
     2 : ([1, 0, -1, 0], [0, 1, 0, -1]),
     3 : tuple([([i, 0, 0, j]) for i in [-1, 1] for j in [-1, 1]]),
     4 : ([1, 0, -1, 0, 0, 1], [1, 0, -1, 0, 0, -1], [-1, 0, 0, -1, 0, 1], [1, 0, 0, 1, 0, -1]),
     5 : [1, 0, -1, 0, 0, 1, 0, -1]}

def update_room(room, cord, ds, N, M):
    length = len(ds) // 2
    for i in range(length):
        cr, cc = cord
        while True:
            nr, nc = cr + ds[2 * i], cc + ds[2 * i + 1]
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] != 6:
                    cr, cc = nr, nc
                    if room[nr][nc] == 0:
                        room[nr][nc] = '#'
                else:
                    break
            else:
                break
    return room

# def pr(room, M):
#     print('_' * M * 2)
#     for row in room:
#         print(' '.join([f'{x}' for x in row]))

def solve():
    N, M = map(int, input().split())
    room = []
    cctvs = []
    cctvs_5 = []
    for i in range(N):
        row = []
        for j, x in enumerate(map(int, input().split())):
            if x != 0 and x != 6:
                if x != 5:
                    cctvs.append(([i, j], x))
                else:
                    cctvs_5.append([i, j])
            row.append(x)
        room.append(row)
    min_black = N * M
    for cctv in cctvs_5:
        room = update_room(room, cctv, s[5], N, M)
    if cctvs:
        for case in product(*[s[cctv[1]] for cctv in cctvs]):
            rc = deepcopy(room)
            for i in range(len(cctvs)):
                rc = update_room(rc, cctvs[i][0], case[i], N, M)
            black = len([_ for row in rc for _ in row if _ == 0])
            if min_black > black:
                min_black = black
    else:
        min_black = len([_ for row in room for _ in row if _ == 0])
    print(min_black)
    return 0

solve()
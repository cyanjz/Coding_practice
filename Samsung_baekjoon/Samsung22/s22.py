def pr(room):
    for row in room:
        print(' '.join([f'{x}' if len(f'{x}') >= 2 else f'0{x}' for x in row]))
    print('#' * C)

def air_cleaner(room):
    global cleaner, total_dust
    r1, r2 = cleaner
    total_dust -= (room[r1-1][0] + room[r2+1][0])
    # upper part
    # shift to rightside
    tmp1 = [-1, 0] + room[r1][1:-1]
    # shift to upper side
    tmp2 = [room[i][-1] for i in range(2, r1+1)]
    # shift to leftside
    tmp3 = room[0][1:] + [room[1][-1]]
    # shift to lower side
    tmp4 = [room[i][0] for i in range(r1-1)]
    room[r1] = tmp1
    room[0] = tmp3
    p = 0
    for i in range(1, r1):
        room[i][0] = tmp4[p]
        room[i][-1] = tmp2[p]
        p += 1

    # lower part
    tmp1 = [-1, 0] + room[r2][1 : -1]
    tmp2 = [room[i][-1] for i in range(r2, R-2)]
    tmp3 = room[R-1][1:] + [room[R-2][-1]]
    tmp4 = [room[i][0] for i in range(r2+2, R)]
    room[r2] = tmp1
    room[R-1] = tmp3
    p = 0
    for i in range(r2+1, R-1):
        room[i][0] = tmp4[p]
        room[i][-1] = tmp2[p]
        p += 1
    # pr(room)
    return 1

def dust_spread(room):
    resulted_room = [[0 for _ in range(C)] for __ in range(R)]
    for r in range(R):
        for c in range(C):
            dust = room[r][c]
            if 0 < dust:
                quin = dust // 5
                for ne in neigh[r][c]:
                    resulted_room[ne[0]][ne[1]] += quin
                    dust -= quin
                resulted_room[r][c] += dust
    r1, r2 = cleaner
    resulted_room[r1][0] = -1
    resulted_room[r2][0] = -1
    del room
    return resulted_room

def solve(room):
    global total_dust
    for _ in range(T):
        # print(_)
        room = dust_spread(room)
        # pr(room)
        air_cleaner(room)
    # pr(room)
    # dump = 0
    # for row in room:
    #     for dust in row:
    #         dump += max(dust, 0)
    # print(dump)
    return total_dust

if __name__ == '__main__':
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    total_dust = 0
    R, C, T = map(int, input().split())
    cleaner = []
    room = []
    for r in range(R):
        row = [int(x) for x in input().split()]
        for c, num in enumerate(row):
            if num == -1:
                cleaner.append(r)
            if num > 0:
                total_dust += num
        room.append(row)
    neigh = [[0 for _ in range(C)] for __ in range(R)]
    for r in range(R):
        for c in range(C):
            tmp = []
            for k in range(4):
                nr, nc = r + dy[k], c + dx[k]
                if 0 <= nr <= R-1 and 0 <= nc <= C-1:
                    if room[nr][nc] != -1:
                        tmp.append((nr, nc))
            neigh[r][c] = tmp
    print(solve(room))
from collections import deque

dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def read_terminal():
    C, R = map(int, input().split())
    points = []
    room = []
    for r in range(R):
        row = input()
        for c, e in enumerate(row):
            if e == 'C':
                points.append((r, c))
        room.append([x for x in row])
    return R, C, room, points

def read_file():
    fp = open('input.txt')
    while True:
        first_line = fp.readline().rstrip('\n')
        if not first_line:
            fp.close()
            return
        C, R = map(int, first_line.split())
        points = []
        room = []
        for r in range(R):
            row = fp.readline().rstrip('\n')
            for c, e in enumerate(row):
                if e == 'C':
                    points.append((r, c))
            room.append([x for x in row])
        print(solve(R, C, room, points))
    fp.close()
    return


def pr(room):
    for row in room:
        print(''.join([f'{x}' for x in row]))

def solve(R, C, room, points):
    dir_map = [[[] for __ in range(C)] for _ in range(R)]
    sr, sc = points.pop()
    er, ec = points.pop()
    room[sr][sc] = 'S'
    room[er][ec] = '.'
    q = deque()
    for k in range(4):
        nr, nc = sr+dr[k], sc+dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if room[nr][nc] == '.':
                q.append((nr, nc, k, 0))
                room[nr][nc] = 0
                dir_map[nr][nc].append(k)
            if room[nr][nc] == 'E':
                return 0
    q = deque(q)
    # iter_times = 0
    while q:
        cr, cc, ck, cost = q.popleft()
        if room[cr][cc] != cost:
            continue
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                loc_type = room[nr][nc]
                n_cost = cost if k == ck else cost + 1
                if loc_type == '.':
                    room[nr][nc] = n_cost
                    dir_map[nr][nc].append(k)
                    q.append((nr, nc, k, n_cost))
                elif type(loc_type) == int:
                    if loc_type > n_cost:
                        q.appendleft((nr, nc, k, n_cost))
                        room[nr][nc] = n_cost
                        dir_map[nr][nc] = [k]
                    elif loc_type == n_cost:
                        if k not in dir_map[nr][nc] and (k+2)%4 not in dir_map[nr][nc]:
                            q.appendleft((nr, nc, k, n_cost))
                            dir_map[nr][nc].append(k)
        # print('#' * C)
        # print(iter_times)
        # pr(room)
        # print(q)
        # iter_times += 1
    return room[er][ec]

if __name__ == '__main__':
    R, C, room, points = read_terminal()
    print(solve(R, C, room, points))
    
    # read_file()
    
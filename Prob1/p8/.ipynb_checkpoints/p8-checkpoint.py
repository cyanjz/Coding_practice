from collections import deque

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def map_prison(prison):
    for row in prison:
        print(''.join(row))
    return

def map_dist(dist):
    for row in dist:
        print(' '.join([f'{x}' for x in row]))
    return

def bfs(cr, cc, R, C, prison):
    dist = [[-1] * (C+2) for _ in range(R+2)]
    q = deque([(cr, cc)])
    dist[cr][cc] = 0
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr, nc = cr+dr[k], cc+dc[k]
            if 0 <= nr < R+2 and 0 <= nc < C+2:
                loc_type = prison[nr][nc]
                d_type = dist[nr][nc]
                if d_type == -1:
                    if loc_type == '.' or loc_type == '$':
                        dist[nr][nc] = dist[cr][cc]
                        q.appendleft((nr, nc))
                    elif loc_type == '#':
                        dist[nr][nc] = dist[cr][cc] + 1
                        q.append((nr, nc))
                    else:
                        dist[nr][nc] = '*'
    return dist

def solve():
    R, C = map(int, input().split())
    people = []
    prison = []
    for r in range(R):
        row = [x for x in input()]
        for c, e in enumerate(row):
            if e == '$':
                people.append((r+1, c+1))
        prison.append(['.'] + row + ['.'])
    prison = [['.'] * (C+2)] + prison + [['.'] * (C+2)]
    # print(prison)
    # prison = [['.'] * (C+2)] + [['.'] + [x for x in input()] + ['.'] for _ in range(R)] + [['.'] * (C+2)]
    d1 = bfs(0, 0, R, C, prison)
    d2 = bfs(*people[0], R, C, prison)
    d3 = bfs(*people[1], R, C, prison)
    # map_dist(d1)
    # map_dist(d2)
    # map_dist(d3)
    ans = 50000
    for r in range(R+2):
        for c in range(C+2):
            if prison[r][c] == '*':
                continue
            temp = d1[r][c] + d2[r][c] + d3[r][c]
            if prison[r][c] == '#':
                temp -= 2
            if temp >= 0:
                ans = min(temp, ans)
    print(ans)
    return

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solve()
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

def unfreeze(lake):
    new_lake = [row[:] for row in lake]
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 'X':
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C:
                        if lake[nr][nc] == '.':
                            new_lake[r][c] = '.'
                            break
    return new_lake

def check(lake, swan):
    visited = [[0] * C for _ in range(R)]
    sr, sc = swan[0]
    er, ec = swan[1]
    q = [(sr, sc)]
    pivot = 0
    qlen = 1
    visited[sr][sc] = 1
    while pivot < qlen:
        cr, cc = q[pivot]
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if nr == er and nc == ec:
                    return True
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if lake[nr][nc] == '.':
                        q.append((nr, nc))
                        qlen += 1
        pivot += 1
    return False

def solve(lake, swan):
    day = 0
    while True:
        if check(lake, swan):
            print(day)
            return 1
        else:
            lake = unfreeze(lake)
        day += 1
    return -1

if __name__ == '__main__':
    R, C = map(int, input().split())
    lake = []
    swan = []
    for r in range(R):
        row = [x for x in input()]
        for c, cha in enumerate(row):
            if cha == 'L':
                swan.append([r, c])
        lake.append(row)

    solve(lake, swan)
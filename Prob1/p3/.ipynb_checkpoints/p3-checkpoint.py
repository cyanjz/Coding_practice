dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

def unfreeze(lake):
    new_lake = [row[:] for row in lake]
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 1:
                for nr, nc in neigh[r][c]:
                    if lake[nr][nc] == 0:
                        new_lake[r][c] = 0
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
    while q:
        cr, cc = q.pop(0)
        for nr, nc in neigh[cr][cc]:
            if nr == er and nc == ec:
                return True
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                if lake[nr][nc] == 0:
                    q.append((nr, nc))
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
    char2int = {'.' : 0, 'X' : 1, 'L' : 2}
    for r in range(R):
        row = [char2int[x] for x in input()]
        for c, e in enumerate(row):
            if e == 2:
                swan.append([r, c])
        lake.append(row)
        
    neigh = [[None] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            tmp = []
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < R and 0 <= nc < C:
                    tmp.append((nr, nc))
            neigh[r][c] = tmp

    solve(lake, swan)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def shark_move():
    global sharks, sea
    next_sea = [row[:] for row in sea]
    next_sharks = {k : v for k, v in sharks.items()}
    for k, v in sharks.items():
        d, r, c = v
        order = orders[k-1][d]
        empty = None
        visited = None
        for i in range(4):
            nd = order[i]
            nr, nc = r + dr[nd], c + dc[nd]
            if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                if not sea[nr][nc]:
                    empty = (nd, nr, nc)
                    break
                if not visited:
                    if sea[nr][nc][1] == k:
                        visited = (nd, nr, nc)
        nd, nr, nc = empty if empty else visited
        next_sea_shark = next_sea[nr][nc]
        if empty:
            if next_sea_shark:
                if k < next_sea_shark[1]:
                    del next_sharks[next_sea_shark[1]]
                    next_sea[nr][nc] = (K+1, k)
                    next_sharks[k] = (nd, nr, nc)
                else:
                    del next_sharks[k]
            else:
                next_sea[nr][nc] = (K+1, k)
                next_sharks[k] = (nd, nr, nc)
        else:
            next_sea[nr][nc] = (K+1, k)
            next_sharks[k] = (nd, nr, nc)
    sea = [row[:] for row in next_sea]
    sharks = {k : v for k, v in next_sharks.items()}
    return 1

def remove_marks():
    global sea
    for r, row in enumerate(sea):
        for c, v in enumerate(row):
            if v:
                v = (v[0] - 1, v[1])
                if not v[0]:
                    sea[r][c] = 0
                else:
                    sea[r][c] = v
    return 1

def solve():
    for turn in range(1000):
        shark_move()
        if len(sharks) == 1:
            print(turn + 1)
            return 1
        remove_marks()
    print(-1)
    return -1

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    sharks = {k : None for k in range(1, M+1)}
    sea = []
    for r in range(N):
        row = [int(x) for x in input().split()]
        for c, num in enumerate(row):
            if num:
                sharks[num] = [r, c]
                row[c] = (K, num)
        sea.append(row)

    directions = [int(x)-1 for x in input().split()]
    for k in range(1, M+1):
        sharks[k] = [directions[k-1]] + sharks[k]
    
    orders = [[[int(x)-1 for x in input().split()] for _ in range(4)] for __ in range(M)]
    solve()

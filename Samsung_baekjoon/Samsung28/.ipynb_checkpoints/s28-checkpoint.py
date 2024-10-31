dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

def pb():
    print('#' * (2*M + 1))
    for row in b:
        print(' '.join([f'{x}' for x in row]))
    return 1

def update_board():
    global total_sum
    board_average = total_sum/total_count
    for r, row in enumerate(b):
        for c, num in enumerate(row):
            if num != 'x':
                if board_average > num:
                    b[r][c] += 1
                    total_sum += 1
                elif board_average < num:
                    b[r][c] -= 1
                    total_sum -= 1
    return 1

def bfs():
    global b, total_count, total_sum
    is_removed = 0
    for r in range(N):
        for c in range(M):
            if b[r][c] != 'x':
                target = b[r][c]
                q = []
                for nr, nc in neigh[r][c]:
                    if b[nr][nc] == target:
                        is_removed = 1
                        b[nr][nc] = 'x'
                        total_sum -= target
                        total_count -= 1
                        q.append((nr, nc))
                if q:
                    b[r][c] = 'x'
                    total_sum -= target
                    total_count -= 1
                while q:
                    cr, cc = q.pop(0)
                    for nr, nc in neigh[cr][cc]:
                        if b[nr][nc] == target:
                            b[nr][nc] = 'x'
                            total_sum -= target
                            total_count -= 1
                            q.append((nr, nc))
    return is_removed
                

def solve():
    global b
    for _ in range(T):
        x, d, k = map(int, input().split())
        # rotate phase
        k %= M
        d = int(2 * (d - 0.5))
        r = x
        while r <= N:
            b[r-1] = b[r-1][d*k:] + b[r-1][:d*k]
            r += x
        flag = bfs()
        if not total_count:
            print(0)
            return 1
        if not flag:
            update_board()
    print(total_sum)
    return 1

if __name__ == '__main__':
    N, M, T = map(int, input().split())
    # N * M matrix
    b = [[int(x) for x in input().split()] for _ in range(N)]
    total_count = N * M
    total_sum = sum([sum(row) for row in b])
    neigh = [[[] for __ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N:
                    if -1 <= nc < M:
                        neigh[r][c].append((nr, nc))
                    elif nc == M:
                        neigh[r][c].append((nr, 0))
    solve()
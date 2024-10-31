#N W E S
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

# def pb(board):
#     print('#' * N)
#     for row in board:
#         print(' '.join([f'{x}' for x in row]))
#     print('#' * N)

# edilbe fish found -> must check whether it is visited or not because shark size may larger than 9
# if visited is not checked, bfs may returns 2 infinitely when size > 9
def bfs():
    global shark_size, shark_hunger, shark_loc, board
    sr, sc = shark_loc
    q = [(sr, sc, 0)]
    visited = [(sr, sc)]
    min_time = 400
    cand = []
    while q:
        cr, cc, t = q.pop(0)
        for nr, nc in neigh[cr][cc]:
            if (nr, nc) not in visited:
                if 0 < board[nr][nc] < shark_size and t + 1 <= min_time:
                    min_time = t+1
                    cand.append((nr, nc))
                    visited.append((nr, nc))
                elif (board[nr][nc] == shark_size or board[nr][nc] == 0) and t + 1 < min_time:
                    q.append((nr, nc, t+1))
                    visited.append((nr, nc))
    if min_time == 400:
        return 0
    else:
        cand.sort(key = lambda x : (x[0], x[1]))
        nr, nc = cand[0]
        board[sr][sc] = 0
        board[nr][nc] = 9
        shark_loc = (nr, nc)
        shark_hunger += 1
        if shark_hunger == shark_size:
            shark_hunger = 0
            shark_size += 1
        return min_time

def solve():
    meal_time = 0
    for _ in range(N*N):
        tte = bfs()
        if not tte:
            return meal_time
        meal_time += tte
    return 'fatal error'

if __name__ == '__main__':
    N = int(input())
    board = []
    for r in range(N):
        row = [int(x) for x in input().split()]
        for c, num in enumerate(row):
            if num == 9:
                shark_loc = (r, c)
        board.append(row)
    
    neigh = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = []
            for k in range(4):
                nr, nc = i+dy[k], j+dx[k]
                if (0<=nr<=N-1) and (0<=nc<=N-1):
                    tmp.append((nr, nc))
            neigh[i][j] = tmp
    
    shark_size = 2
    shark_hunger = 0
    print(solve())
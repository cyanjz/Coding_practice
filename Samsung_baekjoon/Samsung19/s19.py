def dfs(i, j, visited, turn):
    global L, R, board, neigh
    chunk_sum = board[i][j]
    chunk = [(i, j)]
    chunk_size = 1
    visited[i][j] = turn
    pivot = 0
    while pivot < chunk_size:
        cr, cc = chunk[pivot]
        for nr, nc in neigh[(cr, cc)]:
            if visited[nr][nc] < turn and (L<= abs(board[nr][nc] - board[cr][cc]) <= R):
                visited[nr][nc] = turn
                chunk.append((nr, nc))
                chunk_size += 1
                chunk_sum += board[nr][nc]
        pivot += 1
    return chunk, chunk_size, chunk_sum

def solve():
    global board
    num_chunks = 0
    turn = 0
    visited = [[0 for _ in range(N)] for __ in range(N)]
    queue = [(r, c) for r in range(N) for c in range(r%2, N, 2)]
    while num_chunks != end_state:
        num_chunks = end_state
        turn += 1
        next_q = []
        for cr, cc in queue:
            if visited[cr][cc] < turn:
                chunk, chunk_size, chunk_sum = dfs(cr, cc, visited, turn)
                num_chunks -= chunk_size - 1
                if chunk_size != 1:
                    chunk_avg = chunk_sum // chunk_size
                    for r, c in chunk:
                        board[r][c] = chunk_avg
                    next_q += chunk
        queue = next_q
    return turn - 1

if __name__ == '__main__':
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    N, L, R = map(int, input().split())
    neigh = {}
    end_state = N * N
    for i in range(N):
        for j in range(N):
            tmp = []
            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                    tmp.append((nr, nc))
            neigh[(i, j)] = tmp
    board = [[int(x) for x in input().split()] for _ in range(N)]
    print(solve())
# ewsn
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
#opposite
opposite = [1, 0, 3, 2]
#roll, ewsn
# 첫번째에 cur를, cur에 두번째를, 두번째에 7-cur을.
roll = [(1, 0), (0, 1), (3, 2), (2, 3)]
#c-rotate
c_rotate = [2, 3, 1, 0]
#cc-rotate
cc_rotate = [3, 2, 0, 1]

class dice:
    def __init__(self):
        #ewsn, cur
        self.numbers = [3, 4, 5, 2, 6]
        # self.n = 2
        # self.e = 3
        # self.w = 4
        # self.s = 5
        # self.cur = 6
        self.direction = 0
        self.r = 0
        self.c = 0

def bfs(mat_chunk_size, neigh, number, r, c):
    if mat_chunk_size[r][c]:
        return mat_chunk_size[r][c], mat_chunk_size
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    q = [(r, c)]
    len_q = 1
    pivot = 0
    while pivot < len_q:
        cr, cc = q[pivot]
        for nr, nc in neigh[cr][cc]:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                if B[nr][nc] == number:
                    q.append((nr, nc))
                    len_q += 1
        pivot += 1
    for r, c in q:
        mat_chunk_size[r][c] = len_q
    return len_q, mat_chunk_size
            

def solve():
    # build neighborhood matrix for bfs
    neigh = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            temp = []
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    temp.append((nr, nc))
            neigh[r][c] = temp
    # store chunk_size for future
    mat_chunk_size = [[0] * M for _ in range(N)]
    # main part
    score = 0
    di = dice()
    for _ in range(K):
        #1
        nr, nc = di.r + dr[di.direction], di.c + dc[di.direction]
        if 0 <= nr < N and 0 <= nc < M:
            di.r, di.c = nr, nc
        else:
            di.direction = opposite[di.direction]
            di.r += dr[di.direction]
            di.c += dc[di.direction]
        first, second = roll[di.direction]
        di.numbers[first] = di.numbers[4]
        di.numbers[4] = di.numbers[second]
        di.numbers[second] = 7 - di.numbers[first]
        #2
        board_number = B[di.r][di.c]
        chunk_size, mat_chunk_size = bfs(mat_chunk_size, neigh, board_number, di.r, di.c)
        score += chunk_size * board_number
        #3
        A = di.numbers[4]
        if A > board_number:
            di.direction = c_rotate[di.direction]
        elif A < board_number:
            di.direction = cc_rotate[di.direction]
    print(score)
    return

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    B = [[int(x) for x in input().split()] for _ in range(N)]
    solve()
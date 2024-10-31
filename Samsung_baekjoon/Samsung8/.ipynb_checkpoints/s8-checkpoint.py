from copy import deepcopy
import time
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 
def estimate_safe_area(ws, b, v, N, M, Z, V):
    bc = deepcopy(b)
    for wr, wc in ws:
        bc[wr][wc] = 1
    q = v.copy()
    infection = 0
    # cr과 cc가 이미 2가 되었는데 stack에 남아 있는 경우가 발생.
    # nr, nc를 기준으로 업데이트하면 문제 해결됨!
    while q:
        cr, cc = q.pop()
        infection += 1
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if bc[nr][nc] == 0:
                    bc[nr][nc] = 2
                    q.append((nr, nc))
    return Z-3-infection+V

def solve():
    N, M = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    zeros, virus = [], []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                zeros.append([i, j])
            elif board[i][j] == 2:
                virus.append([i, j])
    Z = len(zeros)
    V = len(virus)
    max_area = 0
    es = Z-3
    ws = [(zeros[i], zeros[j], zeros[k]) for i in range(Z-2) for j in range(i+1, Z-1) for k in range(j+1, Z)]
    for w in ws:
        sa = estimate_safe_area(w, board, virus, N, M, Z, V)
        if sa <0:
            print(sa, Z, V)
        if sa > max_area:
            max_area = sa
            if max_area == es:
                print(es)
                return
    print(max_area)

solve()    
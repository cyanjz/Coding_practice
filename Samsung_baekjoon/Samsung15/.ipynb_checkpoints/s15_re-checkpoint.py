dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def is_correct(ladders, i, H, N):
    r, c = 0, i
    while r != H:
        if ladders[r][c]:
            c += 1
        else:
            if c != 0 and ladders[r][c-1]:
                c -= 1
        r += 1
    return c == i
    
def backtracking(depth, ladders, neigh, N, H, r):
    # Stop when there are too many values to swap. -> 1 horizontal line can change 2 values.
    wrong = 0
    for i in range(N):
        if not is_correct(ladders, i, H, N, i):
            wrong += 1
    if wrong == 0:
        return depth
    elif wrong > (3 - depth) * 2:
        return
    
        
        
    for c in range(N):
        if not any([ladder[nr][nc] for nr, nc in neigh[r][c]]):
            ladders[r][c] = 1
            backtracking(depth + 1, ladders, neigh, N, H, r)
    return

def solve(ladders, neigh, N, H):
    answer = backtracking(0, ladders, neigh, N, H, N-1)
    return

if __name__ == '__main__':
    ans = 0
    N, M, H = map(int, input().split())
    temp = [[int(x) for x in input().split()] for _ in range(M)]
    ladders = [[0] * N for _ in range(H)]
    for a, b in ladders:
        ladders[a-1][b-1] = 1
        
    neigh = [[None] * N for _ in range(H)]
    for r in range(H):
        for c in range(N):
            temp = []
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < H and 0 <= nc < N:
                    temp.append(nr, nc)
            neigh[r][c] = temp
    
    solve(ladders, neigh, N, H)
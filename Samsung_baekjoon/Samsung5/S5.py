from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def sol():
    M, N, x, y, K = map(int, input().split())
    b = []
    for i in range(M):
        b.append([int(_) for _ in input().split()])
    moves = [int(_) - 1 for _ in input().split()]
    col = deque([0, 0, 0, 0])
    R, L = 0, 0
    while moves:
        move = moves.pop(0)
        nx, ny = x + dx[move], y + dy[move]
        # dice in the board
        if 0<=nx<=N-1 and 0<=ny<=M-1:
            # E
            if move == 0:
                temp = col[1]
                col[1] = L
                L = col[3]
                col[3] = R
                R = temp
            # W
            if move == 1:
                temp = col[1]
                col[1] = R
                R = col[3]
                col[3] = L
                L = temp
            # N
            if move == 2:
                col.append(col.popleft())
            # S
            if move == 3:
                col.appendleft(col.pop())
            print(col[1])
            if b[ny][nx] == 0:
                b[ny][nx] = col[-1]
            else:
                col[-1] = b[ny][nx]
                b[ny][nx] = 0
            x, y = nx, ny
                
sol()
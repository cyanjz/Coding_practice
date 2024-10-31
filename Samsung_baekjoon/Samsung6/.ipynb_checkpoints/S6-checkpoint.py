def pt(t):
    board = [['O'] * 8 for _ in range(8)]
    for cord in t:
        try:
            board[cord[0]+4][cord[1]+4] = '#'
        except:
            breakpoint()
    for row in board:
        print(''.join(row))
    print('________')
    return
ts = [[(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)], 
        [(0, 0), (1, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1)], 
        [(0, 0), (1, 0), (1, 1), (2, 0)]]
sym = [(1, -1), (-1, 1), (-1, -1)]
# ts[5]
ts.append([(x[1], x[0]) for x in ts[0]])

# ts[6]
ts.append([(x[1], x[0]) for x in ts[4]])
# ts[7]
ts.append([(x[0], -x[1]) for x in ts[4]])
# ts[8]
ts.append([(-x[0], x[1]) for x in ts[6]])

# ts[9]
ts.append([(x[1], x[0]) for x in ts[3]])
# 10
ts.append([(-x[0], x[1]) for x in ts[3]])
#11
ts.append([(x[0], -x[1]) for x in ts[9]])

# 12
ts.append([(x[1], x[0]) for x in ts[2]])
for s in sym:
    ts.append([(s[0]*x[0], s[1]*x[1]) for x in ts[2]])
for s in sym:
    ts.append([(s[0]*x[1], s[1]*x[0]) for x in ts[2]])

def solve():
    board = []
    N, M = map(int, input().split())
    for _ in range(N):
        row = [int(_) for _ in input().split()]
        board.append(row)
    max_sum = 0
    for r in range(N):
        for c in range(M):
            for t in ts:
                tet_sum = 0
                for cord in t:
                    nr, nc = r+cord[0], c+cord[1]
                    if 0 <= nr < N and 0 <= nc < M:
                        tet_sum += board[nr][nc]
                    else:
                        tet_sum = 0
                        break
                if tet_sum > max_sum:
                    max_sum = tet_sum
    print(max_sum)

solve()
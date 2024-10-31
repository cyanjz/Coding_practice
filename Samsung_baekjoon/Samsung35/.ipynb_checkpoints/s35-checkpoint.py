def solve():
    global board, ball_loc, total_mass
    for _ in range(K):
        next_ball_loc = []
        next_board = [[None] * N for __ in range(N)]
        #1 fire ball moves
        for r, c in ball_loc:
            if board[r][c]:
                for m, s, d in board[r][c]:
                    nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
                    if next_board[nr][nc]:
                        next_board[nr][nc].append((m, s, d))
                    else:
                        next_board[nr][nc] = [(m, s, d)]
                        next_ball_loc.append((nr, nc))
        #2 ball fusion
        for r, c in next_ball_loc:
            if len(next_board[r][c]) -1 :
                fire_ball_count = len(next_board[r][c])
                mlist, slist, dlist = zip(*next_board[r][c])
                sum_m = sum(mlist)
                m = sum_m//5
                total_mass -= (sum_m - m * 4)
                if m:
                    s = sum(slist)//fire_ball_count
                    direction_flag = sum([x%2 for x in dlist])
                    if direction_flag == fire_ball_count or direction_flag == 0:
                        next_dlist = [0, 2, 4, 6]
                    else:
                        next_dlist = [1, 3, 5, 7]
                    next_board[r][c] = [(m, s, next_dlist[i]) for i in range(4)]
                else:
                    next_board[r][c] = None
        board = next_board
        ball_loc = next_ball_loc
        #es
        if total_mass == 0:
            break
    print(total_mass)
    return

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    total_mass = 0
    board = [[None for _ in range(N)] for __ in range(N)]
    ball_loc = []
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        total_mass += m
        board[r-1][c-1] = [(m, s, d)]
        ball_loc.append((r-1, c-1))
    solve()
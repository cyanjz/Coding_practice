# E W N S
dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

# d % 2 -> 0 : d + 1
# d % 2 -> 1 : d - 1

def play_turn():
    global pieces, pieces_board
    flag = 0
    for p_num, p in enumerate(pieces):
        cr, cc, d, i = p
        nr, nc = cr + dr[d], cc + dc[d]
        if board[nr][nc] == 2:
            d -= int(2 * (d%2-0.5))
            nr, nc = cr + dr[d], cc + dc[d]
            pieces[p_num][2] = d
        if board[nr][nc] == 2:
            continue
        else:
            temp = pieces_board[cr][cc][i:]
            if len(temp) + len(pieces_board[nr][nc]) >= 4:
                return 1
                
            pieces_board[cr][cc] = pieces_board[cr][cc][:i]
            if board[nr][nc] == 1:
                temp.reverse()
                
            i = len(pieces_board[nr][nc])
            for j, moving_p in enumerate(temp):
                pieces[moving_p][:2] = [nr, nc]
                pieces[moving_p][3] = i + j
            
            pieces_board[nr][nc].extend(temp)
    return 0
    
    
def solve():
    for turn in range(1000):
        flag = play_turn()
        if flag:
            return turn + 1
    return -1

if __name__ == '__main__':
    N, K = map(int, input().split())
    board = [[2] + [int(x) for x in input().split()] + [2] for _ in range(N)]
    board = [[2] * (N + 2)] + board + [[2] * (N + 2)]
    pieces_board = [[[] for _ in range(N+2)] for __ in range(N+2)]
    pieces = []
    for k in range(K):
        r, c, d = map(int, input().split())
        pieces_board[r][c].append(k)
        pieces.append([r, c, d-1, 0])
    print(solve())
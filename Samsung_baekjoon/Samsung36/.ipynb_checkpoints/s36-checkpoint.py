def ds_alpha_test(ds, alpha, percentage):
    dump = [[0] * 5 for _ in range(N)]
    for i in range(9):
        dr, dc = ds[i]
        dump[2+dr][2+dc] = percentage[i]
    dump[2+alpha[0]][2+alpha[1]] = 'a'
    for row in dump:
        print(' '.join([f'{x}' for x in row]))
    return

def print_board(board, cr, cc):
    board_copy = [row[:] for row in board]
    board_copy[cr][cc] = 'xx'
    for row in board_copy:
        print(' '.join([f'{x}' if len(f'{x}') == 2 else f'0{x}' for x in row]))
    return

def solve():
    global board, dr, dc
    div2 = N//2
    cr, cc = div2 + 2, div2 + 2
    length = 1
    for _ in range(div2):
        for i in range(2):
            for j in range(2):
                for __ in range(length):
                    # print('#' * (N + 2))
                    # print(i+j)
                    cr += dr[2*i+j]
                    cc += dc[2*i+j]
                    cds, ca = ds_list[2*i+j], alpha_list[2*i+j]
                    alpha = board[cr][cc]
                    target_sand = alpha
                    for k, (cdr, cdc) in enumerate(cds):
                        spread = int(percentages[k] * target_sand)
                        board[cr + cdr][cc + cdc] += spread
                        alpha -= spread
                    board[cr + ca[0]][cc + ca[1]] += alpha
                    board[cr][cc] = 0
                    # print_board(board, cr, cc)
            length += 1
    # 시작은 [2, N-1]
    ds_left = ds_list[0]
    alpha_left = alpha_list[0]
    cr, cc = 2, N+1
    for i in range(N-1):
        cc -= 1
        alpha = board[cr][cc]
        target_sand = alpha
        for i, (dr, dc) in enumerate(ds_left):
            spread = int(percentages[i] * target_sand)
            board[cr + dr][cc + dc] += spread
            alpha -= spread
        board[cr][cc-1] += alpha
    # print_board(board, cr, cc)

    #calculation
    out_of_board = 0
    for i in range(2):
        out_of_board += sum(board[i])
        out_of_board += sum(board[N+3-i])
    for j in range(N):
        out_of_board += board[2+j][0]
        out_of_board += board[2+j][1]
        out_of_board += board[2+j][N+3]
        out_of_board += board[2+j][N+2]
    print(out_of_board)
    return

if __name__ == '__main__':
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    board = [[0] * N] + [[0] * N] + board + [[0] * N] + [[0] * N]
    board = [[0] * 2 + row + [0] * 2 for row in board]
    ds = [[-2, 0], [-1, -1], [-1, 0], [-1, 1], [0, -2], [1, -1], [1, 0], [1, 1], [2, 0]]
    alpha = [0, -1]
    percentages = (0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02)
    
    # left, down, right, up
    ds_up = [[c, r] for r, c in ds]
    alpha_up = [-1, 0]
    ds_down = [[-r, c] for r, c in ds_up]
    alpha_down = [1, 0]
    ds_right = [[r, -c] for r, c in ds]
    alpha_right = [0, 1]
    ds_list = [ds, ds_down, ds_right, ds_up]
    alpha_list = [alpha, alpha_down, alpha_right, alpha_up]

    dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
    # for ds, alpha in zip(ds_list, alpha_list):
    #     ds_alpha_test(ds, alpha, percentages)
    solve()
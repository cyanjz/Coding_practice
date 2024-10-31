from sys import stdin

def move_block(board, t, x, y):
    i = 2
    while not board[i][y]:
        i += 1
        if i == 6:
            break
    if t == 1:
        board[i-1][y] = 1
        return [i-1]
    elif t == 2:
        j = 2
        while not board[j][y+1]:
            j += 1
            if j == 6:
                break
        min_index = min(i, j)
        board[min_index-1][y] = 1
        board[min_index-1][y+1] = 1
        return [min_index-1]
    elif t == 3:
        board[i-1][y] = 1
        board[i-2][y] = 1
        return [i-2, i-1]

def blocks_shift(board):
    number_of_clear = sum([any(board[r]) for r in range(2)])
    if number_of_clear:
        board[:] = [[0] * 4 for _ in range(number_of_clear)] + board[:-number_of_clear]
        return 1
    return 1

def earn_score(board, scope):
    score = 0
    for pivot in scope:
        if all(board[pivot]):
            board[:] = [[0] * 4] +  board[:pivot] + board[pivot + 1:]
            score += 1
    return score

def solve():
    global blue_board, green_board
    score = 0
    T = int(input())
    for _ in range(T):
        t, x, y = map(int, stdin.readline().rstrip('\n').split())
        
        g_scope = move_block(green_board, t, x, y)
        if t == 2 or t == 3:
            b_scope = move_block(blue_board, 5-t, y, x)
        else:
            b_scope = move_block(blue_board, t, y, x)
        score += earn_score(green_board, g_scope)
        score += earn_score(blue_board, b_scope)
        blocks_shift(green_board)
        blocks_shift(blue_board)
    print(score)
    print(sum([sum(row) for row in green_board]) + sum([sum(row) for row in blue_board]))
    return 1

if __name__ == '__main__':
    blue_board = [[0] * 4 for _ in range(6)]
    green_board = [[0]  * 4 for _ in range(6)]
    solve()
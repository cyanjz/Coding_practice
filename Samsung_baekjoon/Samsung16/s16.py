# R U L D = 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def is_square(x, y, board):
    if board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1:
        return 1
    return 0

def solve():
    board = [[0 for _ in range(101)] for __ in range(101)]
    N = int(input())
    dragons = []
    max_gen = 0
    for i in range(N):
        dragon = [int(_) for _ in input().split()]
        if max_gen < dragon[3]:
            max_gen = dragon[3]
        dragons.append(dragon)

    max_dragon = [0]
    for gen in range(max_gen):
        length = len(max_dragon)
        for i in range(length):
            max_dragon.append((max_dragon[length-i-1] + 1)%4)

    for dragon in dragons:
        x, y, d, g = dragon
        board[y][x] = 1
        for i in range(2 ** g):
            di = (max_dragon[i] + d) % 4
            x, y = x + dx[di], y + dy[di]
            board[y][x] = 1

    cnt = 0
    for y in range(100):
        for x in range(100):
            if is_square(x, y, board):
                cnt += 1
    # for row in board:
    #     print(''.join(map(str, row)))
    return cnt

print(solve())
            
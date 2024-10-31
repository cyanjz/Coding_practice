from itertools import accumulate

# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 0 ≤ r < x + d1, 0 ≤ c ≤ y
# 2번 선거구: 0 ≤ r ≤ x+d2, y < c ≤ N - 1
# 3번 선거구: x+d1 ≤ r ≤ N - 1, 0 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N - 1, y-d1+d2 ≤ c ≤ N - 1

# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# col le : 1 <= d1 <= y re : 1 <= d2 <= N - 1 - y
# row top : 0 <= r bot : x + d1 + d2 <= N - 1, d2 <= N -1 - x - d1
def test_print(x, y, d1, d2):
    board = [['_' for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = sector(x, y, d1, d2, i, j)
    for row in board:
        print(' '.join([f'{x}' for x in row]))
    return 1

def is_vaild(x, y, d1, d2):
    if d1 >= 1 and d2 >= 1 and 1 <= x and x + d1 + d2 <= N and 0 <= y - d1 and y + d2 <= N-1:
        return 1
    return 0

def bf(min_diff):
    tot_pop = min_diff
    for x in range(N):
        for y in range(N):
            for d1 in range(1, y + 1):
                for d2 in range(1, min(N-1-y, N-1-x-d1) + 1):
                    le, re = boundary(x, y, d1, d2)
                    pop_dict = [0, 0, 0, 0, 0]
                    #1 sector board method
                    # sector_board = [[0 for _ in range(N)] for __ in range(N)]
                    # for r in range(x + d1):
                    #     sector_board[r][:y+1] = [1] * (y+1)
                    # for r in range(x + d2 + 1):
                    #     sector_board[r][y+1:N] = [2] * (N-1-y)
                    # for r in range(x + d1, N):
                    #     sector_board[r][:y-d1+d2] = [3] * (y-d1+d2)
                    # for r in range(x + d2 + 1, N):
                    #     sector_board[r][y-d1+d2:N] = [4] * (N-y+d1-d2)
                    # for r in range(x, x + d1 + d2 + 1):
                    #     left, right = le[r-x][1], re[r-x][1]+1
                    #     sector_board[r][left:right] = [5] * (right-left)
                    # for r in range(N):
                    #     for c in range(N):
                    #         pop_dict[sector_board[r][c]] += A[r][c]

                    #2 sector funcion method
                    # for r in range(N):
                    #     for c in range(N):
                    #         pop_dict[sector(x, y, d1, d2, r, c, le, re)] += A[r][c]

                    # #3 summation method
                    # # 1 & 2
                    # for r in range(x):
                    #     pop_dict[0] += acc_A[r][y]
                    #     pop_dict[1] += acc_A[r][N-1] - acc_A[r][y]
                    # for r in range(x, x + d1):
                    #     pop_dict[0] += acc_A[r][le[r-x][1]-1]
                    # for r in range(x, x + d2 + 1):
                    #     pop_dict[1] += acc_A[r][N-1] - acc_A[r][re[r-x][1]]

                    # # 3 & 4
                    # for r in range(x+d1+d2+1, N):
                    #     pop_dict[2] += acc_A[r][y-d1+d2-1]
                    #     pop_dict[3] += acc_A[r][N-1] - acc_A[r][y-d1+d2-1]
                    # if le[d1][1] > 0:
                    #     pop_dict[2] += acc_A[x+d1][le[d1][1]-1]
                    # for r in range(x+d1+1, x+d1+d2+1):
                    #     pop_dict[2] += acc_A[r][le[r-x][1]-1]
                    # for r in range(x+d2+1, x+d1+d2+1):
                    #     pop_dict[3] += acc_A[r][N-1] - acc_A[r][re[r-x][1]]

                    for i in range(x):
                        pop_dict[0] += acc_A[i][y]
                        pop_dict[1] += acc_A[i][N-1] - acc_A[i][y]
                    for i in range(d1):
                        pop_dict[0] += acc_A[x+i][le[i][1]-1]
                        pop_dict[3] += acc_A[x+d2+1+i][N-1] - acc_A[x+d2+1+i][re[d2+1+i][1]]
                    for i in range(d2):
                        pop_dict[1] += acc_A[x+i][N-1] - acc_A[x+i][re[i][1]]
                        pop_dict[2] += acc_A[x+d1+1+i][le[d1+1+i][1]-1]
                    for r in range(x+d1+d2+1, N):
                        pop_dict[2] += acc_A[r][y-d1+d2-1]
                        pop_dict[3] += acc_A[r][N-1] - acc_A[r][y-d1+d2-1]
                    pop_dict[1] += acc_A[x+d2][N-1] - acc_A[x+d2][re[d2][1]]
                    if le[d1][1] > 0:
                        pop_dict[2] += acc_A[x+d1][le[d1][1]-1]
                    
                    
                    pop_dict[4] = tot_pop - sum(pop_dict)
                    # pop_list = [v for v in pop_dict.values()]
                    pop_diff = max(pop_dict) - min(pop_dict)
                    if min_diff >= pop_diff:
                        min_diff = pop_diff
    return min_diff

def boundary(x, y, d1, d2):
    left_end = [(x + i, y - i) for i in range(d1)] + [(x + d1 + i, y - d1 + i) for i in range(d2+1)]
    right_end = [(x + i, y + i) for i in range(d2)] + [(x + d2 + i, y + d2 - i) for i in range(d1+1)]
    return left_end, right_end

def sector(x, y, d1, d2, r, c, le, re):
    if x <= r <= x + d1 + d2 and le[r-x][1] <= c <= re[r-x][1]:
        return 5
    # x - 1까지는 다 더하고 x 부터는 le
    if 0 <= r < x + d1 and 0 <= c <= y:
        return 1
    # x - 1까지는 다 더하고 x 부터는 re
    if 0 <= r <= x + d2 and y < c <= N - 1:
        return 2
    # x + d1 + d2 까지는 le, 이후는 y - d1 + d2
    if x + d1 <= r <= N - 1 and 0 <= c < y - d1 + d2:
        return 3
    # x + d1 + d2 까지는 re, 이후는 y - d1 + d2
    if x + d2 < r <= N - 1 and y - d1 + d2 <= c <= N - 1:
        return 4
    else:
        return 0

def solve():
    min_diff = sum([sum(row) for row in A])
    min_diff = bf(min_diff)
    print(min_diff)
    return 1

if __name__ == '__main__':
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    # accumulate pop board
    acc_A = [[x for x in accumulate(row)] for row in A]
    # test_print(1, 3, 2, 2)
    solve()
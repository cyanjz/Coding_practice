# 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# 다음 칸은 경계선이다.
# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
# 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

# d1, d2 >= 1
# 0 <= r < r + d1 + d2 <= N-1
# 0 <= c - d1 < c < c + d2 <= N-1

# r : 0 ~ N-3
# c : 1 ~ N-2
# ends
#right :  c + d2 <= N-1, d2 <= N-1 - c
#down: r + d1 + d2 <= N-1, d1 + d2 <= N-1 - r
#up : r
#left : 0 <= c - d1, d1 <= c

def pb(le, re):
    pop_map = [[0 for _ in range(N)] for __ in range(N)]
    for r, c in le:
        pop_map[r][c] = 5
    for r, c in re:
        pop_map[r][c] = 5
    for row in pop_map:
        print(' '.join([f'{x}' for x in row]))
    print('#' * N)
    return 1

def bf():
    global min_diff
    for r in range(N-2):
        for c in range(1, N-1):
            for d1 in range(1, c+1):
                for d2 in range(1, N-c):
                    if d1+d2 > N-1-r:
                        continue
                    population = calculate_pop(r, c, d1, d2)
                    left_end, right_end = boundary(r, c, d1, d2)
                    for le, re in zip(left_end, right_end):
                        i = le[0]
                        for j in range(le[1], re[1] + 1):
                            li = loc_index(r, c, d1, d2, i, j)
                            if li != 5:
                                population[li] -= A[i][j]
                            population[5] += A[i][j]
                    pop_list = [p for p in population.values()]
                    pop_diff = max(population.values()) - min(population.values())
                    min_diff = min(pop_diff, min_diff)
    return 1


def loc_index(r, c, d1, d2, x, y):
    if 0 <= x < r+d1 and 0 <= y < c+1:
        return 1
    if 0 <= x < r+d2+1 and c+1 <= y < N:
        return 2
    if r+d1 <= x < N and 0 <= y < c - d1 + d2:
        return 3
    if r+d2+1 <= x < N and c-d1+d2 <= y < N:
        return 4
    return 5


def boundary(r, c, d1, d2):
    left_end = [(r + i, c - i) for i in range(d1)] + [(r + d1 + i, c - d1 + i) for i in range(d2+1)]
    right_end = [(r + i, c + i) for i in range(d2)] + [(r + d2 + i, c + d2 - i) for i in range(d1+1)]
    return left_end, right_end


def calculate_pop(r, c, d1, d2):
    population = {i : 0 for i in range(1, 6)}
    for i in range(r+d1):
        population[1] += sum(A[i][:c+1])
        
    for i in range(r+d2+1):
        population[2] += sum(A[i][c+1:])
        
    for i in range(r+d1, N):
        population[3] += sum(A[i][:c-d1+d2])
        
    for i in range(r+d2+1, N):
        population[4] += sum(A[i][c-d1+d2:])
    return population


def print_boundary(x, y, d1, d2):
    board = [[0 for _ in range(N)] for __ in range(N)]
    le, re = boundary(x, y, d1, d2)
    for i in range(N):
        for j in range(N):
            board[i][j] = loc_index(x, y, d1, d2, i, j)
    for i in range(N):
        for j in range(N):
            if (i, j) in le or (i, j) in re:
                board[i][j] = 5
    for row in board:
        print(' '.join([f'{x}' for x in row]))
    return 1

def solve():
    bf()
    return 1


if __name__ == '__main__':
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    min_diff = sum([sum(row) for row in A])
    solve()
    print(min_diff)
    # print(print_boundary(1, 3, 2, 2))
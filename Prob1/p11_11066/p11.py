import time

def pm(matrix):
    for row in matrix:
        print(row)
    return

def solve(N, pages):
    time_line = []
    time_line.append(time.time())
    cost_mat = [[0] * N for _ in range(N)]
    time_line.append(time.time())
    block_mat = [[sum(pages[r:c+1]) if c >= r else 0 for c in range(N)] for r in range(N)]
    time_line.append(time.time())
    for k in range(1, N):
        for r in range(N-k):
            cost_mat[r][r+k] = min([cost_mat[r][j] + cost_mat[j+1][r+k] for j in range(r, r+k)]) + block_mat[r][r+k]
    time_line.append(time.time())
    print(cost_mat[0][-1])
    time_line.append(time.time())
    # pm(cost_mat)
    # pm(block_mat)
    print(time_line)
    return

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        pages = [int(x) for x in input().split()]
        solve(N, pages)
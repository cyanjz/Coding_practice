from itertools import accumulate

def bf(min_diff):
    tot_pop = min_diff
    for x in range(N):
        for y in range(N):
            for d1 in range(1, min(N-x-1, y+1)):
                for d2 in range(1, min(N-1-y, N-1-x-d1) + 1):
                    le, re = boundary(x, y, d1, d2)
                    pop_list = [0, 0, 0, 0, 0]
                    for i in range(x):
                        pop_list[0] += acc_A[i][y]
                        pop_list[1] += acc_A[i][N-1] - acc_A[i][y]
                    for i in range(d1):
                        pop_list[0] += acc_A[x+i][le[i][1]-1]
                        pop_list[3] += acc_A[x+d2+1+i][N-1] - acc_A[x+d2+1+i][re[d2+1+i][1]]
                    for i in range(d2):
                        pop_list[1] += acc_A[x+i][N-1] - acc_A[x+i][re[i][1]]
                        pop_list[2] += acc_A[x+d1+1+i][le[d1+1+i][1]-1]
                    for r in range(x+d1+d2+1, N):
                        pop_list[2] += acc_A[r][y-d1+d2-1]
                        pop_list[3] += acc_A[r][N-1] - acc_A[r][y-d1+d2-1]
                    pop_list[1] += acc_A[x+d2][N-1] - acc_A[x+d2][re[d2][1]]
                    if le[d1][1] > 0:
                        pop_list[2] += acc_A[x+d1][le[d1][1]-1]
                    
                    
                    pop_list[4] = tot_pop - sum(pop_list)
                    pop_diff = max(pop_list) - min(pop_list)
                    if min_diff >= pop_diff:
                        min_diff = pop_diff
    return min_diff

def boundary(x, y, d1, d2):
    left_end = [(x + i, y - i) for i in range(d1)] + [(x + d1 + i, y - d1 + i) for i in range(d2+1)]
    right_end = [(x + i, y + i) for i in range(d2)] + [(x + d2 + i, y + d2 - i) for i in range(d1+1)]
    return left_end, right_end

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
    solve()
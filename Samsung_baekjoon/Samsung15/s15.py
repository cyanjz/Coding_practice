from copy import deepcopy
from itertools import combinations
from collections import defaultdict

def ladder(h, N, H):
    start = [i for i in range(N)]
    for k in range(H):
        for b in h[k]:
            # swaps
            temp = start[b]
            start[b] = start[b + 1]
            start[b + 1] = temp
    return start

def solve():
    N, M, H = map(int, input().split())
    c = [[0 for _ in range(N-1)] for __ in range(H)]
    horizon = []
    for _ in range(M):
        # update candidates
        a, b = map(int, input().split())
        c[a-1][b-1] = 1
        if b < N-1:
            c[a-1][b] = 1
        if 0 <= b-2:
            c[a-1][b-2] = 1
        horizon.append((a-1, b-1))
    hd = defaultdict(list)
    for a, b in horizon:
        hd[a].append(b)
    candidates = [(i, j) for i in range(H) for j in range(N-1) if not c[i][j]]
    for i in range(0, 4):
        combs = combinations(candidates, i)
        for comb in combs:
            hc = deepcopy(hd)
            for a, b in comb:
                hc[a].append(b)
            end = ladder(hc, N, H)
            if end == [_ for _ in range(N)]:
                return i
    return -1

if __name__ == '__main__':
    print(solve())
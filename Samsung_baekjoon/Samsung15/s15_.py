def es_diff(end, start):
    d = 0
    for i in range(len(end)):
        if end[i] != start[i]:
            d += 1
    return d

def ladder_down(N, ladder):
    start = [_ for _ in range(N)]
    for row in ladder:
        for b, r in enumerate(row[1 : -1]):
            if r == 1:
                temp = start[b]
                start[b] = start[b+1]
                start[b+1] = temp
    return start

# ladder -> ladder가 존재하는 곳만.
def solve():
    N, M, H = map(int, input().split())
    ladder = [[0 for _ in range(N-1)] for __ in range(H)]
    ladder = [[-1] + row + [-1] for row in ladder]
    for _ in range(M):
        # a -> 0 ~ H-1, b -> 0 ~ N-2
        # 4가 있으면 3, 5는 불가능.
        a, b = map(lambda x : int(x), input().split())
        ladder[a-1][b] = 1
        ladder[a-1][b-1] = -1
        ladder[a-1][b+1] = -1
    start = [_ for _ in range(N)]
    end = ladder_down(N, ladder)
    d = es_diff(end, start)
    # add 0
    if d == 0:
        return 0
    cands = [(i, j) for i in range(H) for j in range(N) if ladder[i][j] == 0]
    C = len(cands)
    # add 1
    if d <= 2:
        for cand in cands:
            ladder[cand[0]][cand[1]] = 1
            if ladder_down(N, ladder) == start:
                return 1
            ladder[cand[0]][cand[1]] = 0
    # add 2
    if d <= 4:
        for i in range(C-1):
            ladder[cands[i][0]][cands[i][1]] = 1
            s1 = i+1 if cands[i+1] != (cands[i][0], cands[i][1]+1) else i+2
            for j in range(s1, C):
                ladder[cands[j][0]][cands[j][1]] = 1
                if ladder_down(N, ladder) == start:
                    return 2
                ladder[cands[j][0]][cands[j][1]] = 0
            ladder[cands[i][0]][cands[i][1]] = 0
    # add 3
    if d <= 6:
        for i in range(C-2):
            ladder[cands[i][0]][cands[i][1]] = 1
            s1 = i+1 if cands[i+1] != (cands[i][0], cands[i][1]+1) else i+2
            if s1 == C-1:
                continue
            s2 = s1+1 if cands[s1+1] != (cands[s1][0], cands[s1][1]+1) else s1+2
            for j in range(s1, C-1):
                ladder[cands[j][0]][cands[j][1]] = 1
                for k in range(s2, C):
                    ladder[cands[k][0]][cands[k][1]] = 1
                    if ladder_down(N, ladder) == start:
                        return 3
                    ladder[cands[k][0]][cands[k][1]] = 0
                ladder[cands[j][0]][cands[j][1]] = 0
            ladder[cands[i][0]][cands[i][1]] = 0
    return -1

print(solve())
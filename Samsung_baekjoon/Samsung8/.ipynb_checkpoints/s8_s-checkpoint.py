dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def estimate_sa(ws, b, v, N, M):
    bc = b
    for w in ws:
        bc = bc[:w] + '1' + bc[w+1:]
    q = v.copy()
    while q:
        c = q.pop(0)
        bc = bc[:c] + '2' + bc[c+1:]
        for i in range(4):
            nc = (c//M + dr[i])*M + c%M+dc[i]
            if 0 <= nc < N*M and 0 <= c%M+dc[i] < M:
                if bc[nc] == '0':
                    q.append(nc)
    return len([_ for _ in bc if _ == '0']), bc
        

def solve():
    N, M = map(int, input().split())
    b = ''.join([''.join(input().split()) for _ in range(N)])
    zeros = [i for i in range(N*M) if b[i] == '0']
    virus = [i for i in range(N*M) if b[i] == '2']
    Z = len(zeros)
    max_sa = 0
    es = Z-3
    for i in range(Z-2):
        for j in range(i+1, Z-1):
            for k in range(j+1, Z):
                ws = [zeros[i], zeros[j], zeros[k]]
                sa, bc = estimate_sa(ws, b, virus, N, M)
                if max_sa < sa:
                    max_sa = sa
                    if max_sa == es:
                        print(max_sa)
                        return
    print(max_sa)

solve()
    
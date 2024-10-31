def solve():
    for _ in range(K):
        # 1 moves.
        b.clear()
        for r, c, m, s, d in fb:
            ncrd = (r + dr[d]) % N * N + (c + dc[d]) % N
            if ncrd not in b:
                b[ncrd] = (1, m, s, d%2, d)
            else:
                b[ncrd][0] += 1
                b[ncrd][1] += m
                b[ncrd][2] += s
                b[ncrd][3] += d%2
        # 2 fusion.
        fb.clear()
        for crd, (c, m, s, f, d) in b:
            y, x = divmod(crd, N)
            if c == 1:
                fb.append(x, y, m, s, d)
                continue
            else:
                if m//5:
                    fb.append((y, c, m//5, s//c, d))
    return

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    fb = []
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fb.append((r, c, m, s, d))
    fb = [[int(x) for x in input().split()] for _ in range(M)]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    b = dict()
    solve()
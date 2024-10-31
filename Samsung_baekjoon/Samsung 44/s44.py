fish_dr = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dc = [-1, -1, 0, 1, 1, 1, 0, -1]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def ps(sea):
    # print('#' * 4)
    # for row in sea:
    #     print(' '.join([f'{x}' for x in row]))
    return

# uldr -> 1234
# uuu uul uud uur ulu ull uld ulr udu udl
def dfs(sr, sc, sea):
    max_score = -1
    dump_sea = [row[:] for row in sea]
    for nr1, nc1 in neigh[sr][sc]:
        score1 = len(dump_sea[nr1][nc1])
        dump_sea[nr1][nc1] = []
        for nr2, nc2 in neigh[nr1][nc1]:
            fishes2 = len(dump_sea[nr2][nc2])
            score2 = score1 + fishes2
            dump_sea[nr2][nc2] = []
            for nr3, nc3 in neigh[nr2][nc2]:
                score3 = score2 + len(dump_sea[nr3][nc3])
                if max_score < score3:
                    max_score = score3
                    moves = [(nr1, nc1), (nr2, nc2), (nr3, nc3)]
            dump_sea[nr2][nc2] = [0] * fishes2
        dump_sea[nr1][nc1] = [0] * score1
    return moves, max_score
                

def solve(sea, M, S, sr, sc):
    smell1 = [[0] * 4 for _ in range(4)]
    smell2 = [[0] * 4 for _ in range(4)]
    for _ in range(S):
        ps(sea)
        # 1 take the photo of sea
        sea_image = [row[:] for row in sea]
        dup_M = M
        # 2 fish moves
        next_sea = [[list() for __ in range(4)] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                list_fish = sea[r][c]
                for fish in list_fish:
                    moved = 0
                    for _ in range(8):
                        nr, nc = r + fish_dr[fish], c + fish_dc[fish]
                        if 0 <= nr < 4 and 0 <= nc < 4 and not smell1[nr][nc] and not smell2[nr][nc]:
                            if sr != nr or sc != nc:
                                next_sea[nr][nc].append((fish+8)%8)
                                moved = 1
                                break
                        fish -= 1
                    if not moved:
                        next_sea[r][c].append((fish+8)%8)
        sea = next_sea
        ps(sea)
        # 3 shark moves & 4 smell disapears
        moves, max_score = dfs(sr, sc, sea)
        new_smell = [[0] * 4 for _ in range(4)]
        sr, sc = moves[-1]
        for r, c in moves:
            if sea[r][c]:
                new_smell[r][c] = 1
            sea[r][c] = []
        M -= max_score
        smell2 = smell1
        smell1 = new_smell
        ps(sea)
        # 5 duplicates
        for r in range(4):
            for c in range(4):
                for fish in sea_image[r][c]:
                    sea[r][c].append(fish)
        M += dup_M
    ps(sea)
    print(M)
    return

if __name__ == '__main__':
    M, S = map(int, input().split())
    sea = [[list() for __ in range(4)] for _ in range(4)]
    fishes = [[int(x) for x in input().split()] for _ in range(M)]
    sr, sc = [int(x)-1 for x in input().split()]
    for r, c, d in fishes:
        sea[r-1][c-1].append(d-1)

    neigh = [[None] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            temp = []
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    temp.append((nr, nc))
            neigh[r][c] = temp
    
    solve(sea, M, S, sr, sc)
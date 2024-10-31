dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
ddr = [-1, -1, 1, 1]
ddc = [-1, 1, 1, -1]


def solve(A, winds):
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    
    neigh = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp = []
            for k in range(4):
                nr, nc = r + ddr[k], c + ddc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    temp.append((nr, nc))
            neigh[r][c] = temp
            
    for wind in winds:
        direction, strength = wind
        wdr, wdc = dr[direction-1], dc[direction-1]
        # 1.
        clouds = [y for y in map(lambda x : ((x[0]+wdr*strength)%N, (x[1]+wdc*strength)%N), clouds)]
        clouds_map = [[0] * N for _ in range(N)]
        for r, c in clouds:
            clouds_map[r][c] = 1
        # 2.
        for r, c in clouds:
            A[r][c] += 1
        # 4.
        water_copy_bug = []
        for r, c in clouds:
            temp = 0
            for nr, nc in neigh[r][c]:
                if A[nr][nc]:
                    temp += 1
            water_copy_bug.append(temp)
        for i, (r, c) in enumerate(clouds):
            A[r][c] += water_copy_bug[i]
        # 5.
        next_clouds = []
        for r in range(N):
            for c in range(N):
                if A[r][c] >= 2 and not clouds_map[r][c]:
                    A[r][c] -= 2
                    next_clouds.append((r, c))
        clouds = next_clouds
    print(sum([sum(row) for row in A]))
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    winds = [[int(x) for x in input().split()] for _ in range(M)]
    solve(A, winds)
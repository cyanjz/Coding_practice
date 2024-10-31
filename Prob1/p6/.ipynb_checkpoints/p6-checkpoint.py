dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def pc(cave):
    rev_mapping = {0 : '.', 1 : 'x'}
    for row in cave:
        print(''.join([rev_mapping[x] for x in row]))
    return

def find_cluster(candidates, cave, neigh):
    clusters = []
    visited = [[0] * C for _ in range(R)]
    cluster_found = 0
    for cr, cc in candidates:
        if cluster_found:
            continue
        if visited[cr][cc]:
            continue
        bottom = {cc : cr}
        q = [(cr, cc)]
        visited[cr][cc] = 1
        if cr == R-1:
            landed = 1
            continue
        pivot = 0
        q_len = 1
        landed = 0
        while pivot < q_len:
            cr, cc = q[pivot]
            for nr, nc in neigh[cr][cc]:
                if cave[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    q_len += 1
                    visited[nr][nc] = 1
                    bottom[nc] = max(bottom.get(nc, 0), nr)
                    if nr == R-1:
                        landed = 1
            pivot += 1
        breakpoint()
        if landed == 0:
            cluster_found = 1
    if cluster_found:
        return q, bottom
    else:
        return None, None
    
def solve(R, C, N, cave, sticks, neigh):
    for i in range(N):
        # stick phase
        cr = sticks[i]
        if i % 2:
            move = -1
            cc = C-1
        else:
            move = 1
            cc = 0
        hit = 0
        while cc != -1 and cc != C:
            if cave[cr][cc]:
                cave[cr][cc] = 0
                hit = 1
                break
            cc += move
        # cluster finding
        breakpoint()
        if hit:
            candidates = [(nr, nc) for nr, nc in neigh[cr][cc] if cave[nr][nc]]
            cluster, bottom = find_cluster(candidates, cave, neigh)
            breakpoint()
            # cluster fall
            if cluster:
                min_dist = R
                for k, v in bottom.items():
                    cc, cr = k, v
                    dist = 1
                    while not cave[cr+dist][cc]:
                        dist += 1
                        if cr + dist > R-1:
                            break
                    if dist < min_dist:
                        min_dist = dist
                for r, c in cluster:
                    cave[r][c] = 0
                for r, c in cluster:
                    cave[r+min_dist-1][c] = 1
    pc(cave)
    return

if __name__ == '__main__':
    R, C = map(int, input().split())
    mapping = {'.' : 0, 'x' : 1}
    cave = [[mapping[e] for e in input()] for _ in range(R)]
    N = int(input())
    sticks = [R-int(x) for x in input().split()]
    neigh = [[None] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            temp = []
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < R and 0 <= nc < C:
                    temp.append((nr, nc))
            neigh[r][c] = temp
    solve(R, C, N, cave, sticks, neigh)
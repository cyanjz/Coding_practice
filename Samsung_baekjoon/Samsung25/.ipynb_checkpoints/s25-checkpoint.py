from itertools import combinations

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs_chunk_finder():
    chunks = []
    chunks_v = []
    visited = []
    for r in range(N):
        for c in range(N):
            if (r, c) not in visited and lab[r][c] == 0:
                chunk = [(r, c)]
                visited.append((r, c))
                virus = []
                pivot = 0
                chunk_size = 1
                while pivot < chunk_size:
                    cr, cc = chunk[pivot]
                    for nr, nc in neigh[cr][cc]:
                        if (nr, nc) not in chunk:
                            if lab[nr][nc] == 2:
                                virus.append((nr, nc))
                            visited.append((nr, nc))
                            chunk.append((nr, nc))
                            chunk_size += 1
                    pivot += 1
                chunks.append(chunk)
                chunks_v.append(virus)
    return chunks, chunks_v

def bfs_virus_spread(comb):
    lab_map = [row[:] for row in lab]
    tti = 0
    q = comb[:][:]
    for r, c in comb:
        lab_map[r][c] = 3
    infection = 0
    while infection != num_zeros:
        next_q = []
        for cr, cc in q:
            for nr, nc in neigh[cr][cc]:
                if lab_map[nr][nc] == 0:
                    infection += 1
                    next_q.append((nr, nc))
                    lab_map[nr][nc] = 3
                elif lab_map[nr][nc] == 2:
                    next_q.append((nr, nc))
                    lab_map[nr][nc] = 3
        q = next_q
        tti += 1
    return tti
                    
                        
def spreadable(comb, chunks_v):
    for virus in chunks_v:
        if not any(map(lambda x : x in comb, virus)):
            return False
    return True

def solve():
    chunks, chunks_v = bfs_chunk_finder()
    for v in chunks_v:
        if not v:
            return -1
    if len(chunks_v) > M:
        return -1
    combs = combinations(vi, M)
    min_tti = 2500
    for comb in combs:
        if not spreadable(comb, chunks_v):
            continue
        tti = bfs_virus_spread(comb)
        if tti == 0:
            return tti
        min_tti = min(tti, min_tti)
    return min_tti

if __name__ == '__main__':
    N, M = map(int, input().split())
    lab = [[int(x) for x in input().split()] for _ in range(N)]
    num_zeros = 0
    vi = []
    for r, row in enumerate(lab):
        for c, num in enumerate(row):
            if num == 2:
                vi.append((r, c))
            if num == 0:
                num_zeros += 1
    
    neigh = [[[] for c in range(N)] for r in range(N)]
    for r in range(N):
        for c in range(N):
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                    if lab[nr][nc] != 1:
                        neigh[r][c].append((nr, nc))
    
    print(solve())
        
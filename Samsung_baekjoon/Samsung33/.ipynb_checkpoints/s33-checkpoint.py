# visited -> N * N size list?

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def vailidity_test():
    visited = [[0 for _ in range(N)] for __ in range(N)]
    chunk_index = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                chunk_index += 1
                visited[r][c] = chunk_index
                if city_map[r][c] == 1:
                    continue
                q = [(r, c)]
                while q:
                    cr, cc = q.pop(0)
                    for nr, nc in neigh[cr][cc]:
                        if not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = chunk_index
    if chunk_index == 1:
        return 1
    ti = visited[texi[0]][texi[1]]
    for sr, sc, er, ec in missions:
        si, ei = visited[sr][sc], visited[er][ec]
        if si != ti or ei != ti:
            return 0
    return 1

def search_for_customer():
    global city_map, texi, F
    q = [(texi[0], texi[1], 0)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[texi[0]][texi[1]] = 1
    candidates = []
    while q:
        cr, cc, cost = q.pop(0)
        if city_map[cr][cc] and city_map[cr][cc] >= 2:
            candidates.append((cr, cc))
            break
        else:
            if cost + 1 <= F:
                for nr, nc in neigh[cr][cc]:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc, cost + 1))
    if candidates:
        fuel_cost = cost
        while q:
            cr, cc, cost = q.pop(0)
            if cost != fuel_cost:
                break
            elif city_map[cr][cc] and city_map[cr][cc] >= 2:
                candidates.append((cr, cc))
        candidates.sort(key = lambda x : (x[0], x[1]))
        fr, fc = candidates[0]
        
        F -= fuel_cost
        customer = city_map[fr][fc]
        city_map[fr][fc] = 0
        texi = [fr, fc]
        return customer
    else:
        return 0
    
def transport(customer):
    global city_map, texi, F, M
    q = [(texi[0], texi[1], 0)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[texi[0]][texi[1]] = 1
    target_cords = dests[customer]
    target_found = 0
    while q:
        cr, cc, cost = q.pop(0)
        if cost + 1 <= F:
            for nr, nc in neigh[cr][cc]:
                if not visited[nr][nc]:
                    if (nr, nc) == target_cords:
                        fuel_cost = cost + 1
                        target_found = 1
                        break
                    else:
                        visited[nr][nc] = 1
                        q.append((nr, nc, cost + 1))
            if target_found:
                break
    if target_found:
        F += fuel_cost
        texi = list(target_cords)
        return 1
    else:
        return 0

def solve():
    for _ in range(M):
        customer = search_for_customer()
        if not customer:
            print(-1)
            return
        if not transport(customer):
            print(-1)
            return
    print(F)
    return

if __name__ == '__main__':
    N, M, F = map(int, input().split())
    city_map = [[int(x) for x in input().split()] for _ in range(N)]
    texi = [int(x)-1 for x in input().split()]
    # start r, start c, end r, end c
    # missions -> for validity test
    missions = []
    dests = {}
    for request_number in range(M):
        sr, sc, er, ec = map(int, input().split())
        missions.append((sr-1, sc-1, er-1, ec-1))
        dests[request_number+2] = (er-1, ec-1)
        city_map[sr-1][sc-1] = request_number + 2
    neigh = [[0 for __ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            nei = []
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if city_map[nr][nc] != 1:
                        nei.append((nr, nc))
            neigh[r][c] = nei
    if vailidity_test():
        solve()
    else:
        print(-1)
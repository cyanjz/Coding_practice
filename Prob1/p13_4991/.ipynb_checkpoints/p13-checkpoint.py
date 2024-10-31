dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(room, sr, sc, R, C):
    visited = [[0] * C for _ in range(R)]
    visited[sr][sc] = 1
    q = [(sr, sc, 0)]
    pivot = 0
    q_len = 1
    found = 0
    while pivot < q_len and not found:
        cr, cc, cost = q[pivot]
        for k in range(4):
            nr, nc = cr+dr[k], cc+dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc]:
                    if room[nr][nc] == '*':
                        room[nr][nc] = '.'
                        return room, nr, nc, cost+1
                    elif room[nr][nc] == '.':
                        visited[nr][nc] = 1
                        q.append((nr, nc, cost+1))
                        q_len += 1
        pivot += 1
    return room, False, False, False

def solve():
    C, R = map(int, input().split())
    if C == 0:
        return False
    t_cost = 0
    dusts = 0
    cleaned = 0
    room = []
    for r in range(R):
        row = input()
        for c, s in enumerate(row):
            if s == 'o':
                sr, sc = r, c
            elif s == '*':
                dusts += 1
        room.append([x for x in row])
    room[sr][sc] = '.'
    while cleaned != dusts:
        room, sr, sc, cost = bfs(room, sr, sc, R, C)
        if not cost:
            print(-1)
            return True
        cleaned += 1
        t_cost += cost
    print(t_cost)
    fp = open('output.txt', 'a')
    fp.write(f'{t_cost}\n')
    fp.close()
    return True

if __name__ == '__main__':
    flag = True
    fp = open('output.txt', 'w')
    fp.write('')
    fp.close()
    while flag:
        flag = solve()
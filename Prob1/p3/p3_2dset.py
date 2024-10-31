# 1500 * 1500 메모리가 터질 이유는 없어 보이는데?
# neigh 만드는데 시간 오래 걸림.
import sys


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

def pl(lake):
    for row in lake:
        print(' '.join(f'{x}' for x in row))
    return

def chunk_finder(lake):
    chunk_idx = 3
    chunk_dict = {}
    for r in range(R):
        for c in range(C):
            if lake[r][c] == 0:
                q = [(r, c)]
                lake[r][c] = chunk_idx
                pivot = 0
                qlen = 1
                while pivot < qlen:
                    cr, cc = q[pivot]
                    for k in range(4):
                        nr, nc = cr + dr[k], cc + dc[k]
                        if 0 <= nr < R and 0 <= nc < C:
                            if lake[nr][nc] == 0:
                                lake[nr][nc] = chunk_idx
                                q.append((nr, nc))
                                qlen += 1
                    pivot += 1
                chunk_dict[chunk_idx] = q
                chunk_idx += 1
    return lake, chunk_dict
    
def solve(lake, swan, chunk_dict):
    sc1 = lake[swan[0][0]][swan[0][1]]
    sc2 = lake[swan[1][0]][swan[1][1]]
    day = 0
    if sc1 == sc2:
        print(0)
        return
    while True:
        day += 1
        new_lake = [row[:] for row in lake]
        for r in range(R):
            for c in range(C):
                if lake[r][c] == 1:
                    tmp = []
                    melt = False
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < R and 0 <= nc < C:
                            if new_lake[nr][nc] != 1:
                                tmp.append(new_lake[nr][nc])
                            if lake[nr][nc] != 1:
                                melt = True
                    tmp = list(set(tmp))
                    if melt:
                        if len(tmp) == 1:
                            new_lake[r][c] = tmp[0]
                            chunk_dict[tmp[0]].append((r, c))
                        elif len(tmp) > 1:
                            root = min(tmp)
                            for chunk_idx in tmp:
                                if chunk_idx != root:
                                    for chunk_r, chunk_c in chunk_dict[chunk_idx]:
                                        new_lake[chunk_r][chunk_c] = root
                                    chunk_dict[root].extend(chunk_dict[chunk_idx])
                                    del chunk_dict[chunk_idx]
                            new_lake[r][c] = root
                            chunk_dict[root].append((r, c))
        lake = new_lake
        sc1 = lake[swan[0][0]][swan[0][1]]
        sc2 = lake[swan[1][0]][swan[1][1]]
        if sc1 == sc2:
            print(day)
            return
    return -1

if __name__ == '__main__':
    R, C = map(int, input().split())
    lake = []
    swan = []
    char2int = {'.' : 0, 'X' : 1, 'L' : 2}
    for r in range(R):
        row = [char2int[x] for x in sys.stdin.readline().rstrip('\n')]
        for c, e in enumerate(row):
            if e == 2:
                swan.append([r, c])
                row[c] = 0
        lake.append(row)
    lake, chunk_dict = chunk_finder(lake)
    # pl(lake)
    # print(chunk_dict)
    solve(lake, swan, chunk_dict)
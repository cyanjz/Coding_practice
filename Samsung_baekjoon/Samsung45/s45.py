dr = [-1, 0]
dc = [0, 1]

def build_neigh(col_dim, row_dim):
    neigh_head = [[None] * row_dim for _ in range(col_dim)]
    for r in range(col_dim):
        for c in range(row_dim):
            temp = []
            for k in range(2):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < col_dim and 0 <= nc < row_dim:
                    temp.append((nr, nc))
            neigh_head[r][c] = temp
    return neigh_head

def find_head_size(N):
    # find head size
    col_dim = 2
    while True:
        if col_dim*(col_dim-1) > N:
            col_dim -= 1
            row_dim = col_dim
            break
        elif col_dim**2 > N:
            row_dim = col_dim - 1
            break
        col_dim += 1
    return col_dim, row_dim

def find_head_mapper(N):
    head_mapper = [(0, 0)]
    N -= 1
    col_size = 1
    row_size = 1
    while True:
        if N - row_size < 0:
            break
        #transepose & col_reverse
        head_mapper = [(c, col_size-1-r) for r, c in head_mapper]
        #add new row
        head_mapper = head_mapper + [(col_size, i) for i in range(row_size)]
        N -= row_size
        #row_size increases
        row_size += 1
        # print(head_mapper)
        if N - row_size < 0:
            break
        #transepose & col_reverse
        head_mapper = [(c, col_size-r) for r, c in head_mapper]
        #add new row
        head_mapper = head_mapper + [(col_size, i) for i in range(row_size)]
        N -= row_size
        #col_size increases
        col_size += 1
        # print(head_mapper)
    return head_mapper

def find_block_mapper(N):
    row_order = [2, 1, 0, 3]
    row_dim = N//4
    block_mapper = [(2, row_dim-1-i) for i in range(row_dim)]
    block_mapper += [(1, i) for i in range(row_dim)]
    block_mapper += [(0, row_dim-1-i) for i in range(row_dim)]
    block_mapper += [(3, i) for i in range(row_dim)]
    return block_mapper

def average_tanks(head, tail, col_dim, row_dim, neigh, tail_size):
    new_head = [row[:] for row in head]
    new_tail = tail[:]
    for r in range(col_dim):
        for c in range(row_dim):
            for nr, nc in neigh[r][c]:
                diff = head[r][c] - head[nr][nc]
                if diff > 0:
                    new_head[r][c] -= diff//5
                    new_head[nr][nc] += diff//5
                else:
                    new_head[r][c] += -diff//5
                    new_head[nr][nc] -= -diff//5
    if tail:
        diff = head[col_dim-1][row_dim-1] - tail[0]
        if diff > 0:
            new_head[col_dim-1][row_dim-1] -= diff//5
            new_tail[0] += diff//5
        else:
            new_head[col_dim-1][row_dim-1] += -diff//5
            new_tail[0] -= -diff//5
        for i in range(tail_size-1):
            diff = tail[i] - tail[i+1]
            if diff > 0:
                new_tail[i] -= diff//5
                new_tail[i+1] += diff//5
            else:
                new_tail[i] += -diff//5
                new_tail[i+1] -= -diff//5
    return new_head, new_tail
    

def serialize(head, tail):
    serial = []
    for x in zip(*head):
        serial += x[::-1]
    return serial + tail

def solve(N, K, tanks):
    #build up
    col_dim, row_dim = find_head_size(N)
    head_mapper = find_head_mapper(N)
    tail_size = N - col_dim * row_dim
    neigh_head = build_neigh(col_dim, row_dim)
    block_mapper = find_block_mapper(N)
    neigh_block = build_neigh(4, N//4)

    #main part
    turn = 1
    while True:
        # 0 add fish
        min_idx = []
        min_fish = 10000
        for i, fish in enumerate(tanks):
            if fish < min_fish:
                min_idx = [i]
                min_fish = fish
            elif fish == min_fish:
                min_idx.append(i)
        for i in min_idx:
            tanks[i] += 1
        # 1 head_tail_split & averageing
        head = [[0] * row_dim for _ in range(col_dim)]
        for i, coord in enumerate(head_mapper):
            r, c = coord
            head[r][c] = tanks[i]
        tail = tanks[col_dim * row_dim:]
        head, tail = average_tanks(head, tail, col_dim, row_dim, neigh_head, tail_size)
        # 2 serialize
        tanks = serialize(head, tail)
        # 3 block & averageing
        block = [[0] * (N//4) for _ in range(4)]
        for i, coord in enumerate(block_mapper):
            r, c = coord
            block[r][c] = tanks[i]
        block, tail = average_tanks(block, [], 4, N//4, neigh_block, 0)
        # 4 serialize
        tanks = serialize(block, tail)

        # 5 check up
        if max(tanks) - min(tanks) <= K:
            print(turn)
            return
        turn += 1
    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    tanks = [int(x) for x in input().split()]
    solve(N, K, tanks)
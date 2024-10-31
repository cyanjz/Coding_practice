dr_list, dc_list = [1, -1, 0, 0], [0, 0, 1, -1]

def printb(B):
    print('Printing B...')
    for row in B:
        print(" ".join(['B' if x == -1 else 'n' if x == -2 else f'{x}' for x in row ]))
    return

def largest_chunk(B):
    visited = [[0] * N for _ in range(N)]
    max_chunk_size = 0
    max_rainbows = 0
    max_chunk = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if B[r][c] != 0:
                    visited[r][c] = 1
                chunk_color = B[r][c]
                if chunk_color > 0:
                    q = [(r, c)]
                    chunk_visited = [(r, c)]
                    chunk = [(r, c)]
                    chunk_size = 1
                    number_of_rainbows = 0
                    while q:
                        cr, cc = q.pop(0)
                        for nr, nc in neigh[cr][cc]:
                            if (nr, nc) not in chunk_visited:
                                chunk_visited.append((nr, nc))
                                n_color = B[nr][nc]
                                if n_color == chunk_color:
                                    chunk.append((nr, nc))
                                    q.append((nr, nc))
                                    visited[nr][nc] = 1
                                    chunk_size += 1
                                elif n_color == 0:
                                    chunk.append((nr, nc))
                                    q.append((nr, nc))
                                    number_of_rainbows += 1
                                    chunk_size += 1
                    if chunk_size >= 2:
                        if chunk_size > max_chunk_size:
                            max_chunk_size = chunk_size
                            max_rainbows = number_of_rainbows
                            max_chunk = chunk
                        elif chunk_size == max_chunk_size:
                            if number_of_rainbows >= max_rainbows:
                                max_rainbows = number_of_rainbows
                                max_chunk = chunk
    return max_chunk, max_chunk_size

def gravity(B):
    for c in range(N):
        cr = N-1
        bottom = N-1
        while cr >= 0:
            cur_type = B[cr][c]
            if cur_type >= 0:
                B[cr][c] = -2
                B[bottom][c] = cur_type
                bottom -= 1
            elif cur_type == -1:
                bottom = cr - 1
            cr -= 1
    return

def rotate(B):
    B = [list(row) for row in zip(*B)]
    B = B[::-1]
    return B

def solve(B, N, M):
    score = 0
    while True:
        # print(f'########Turn : {turn}########')
        # printb(B)
        chunk, chunk_size = largest_chunk(B)
        if not chunk:
            print(score)
            return
        score += chunk_size**2
        # print(chunk_size, score)
        for r, c in chunk:
            B[r][c] = -2
        # printb(B)
        gravity(B)
        # printb(B)
        B = rotate(B)
        # printb(B)
        gravity(B)
        # printb(B)
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    B = [[int(x) for x in input().split()] for _ in range(N)]

    neigh = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            nei = []
            for k in range(4):
                nr, nc = r + dr_list[k], c + dc_list[k]
                if 0 <= nr < N and 0 <= nc < N:
                    nei.append((nr, nc))
            neigh[r][c] = nei
    
    # print(largest_chunk(B)[0])
    # printb(B)
    solve(B, N, M)
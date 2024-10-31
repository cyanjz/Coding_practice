dr_list, dc_list = [0, 0, 1, -1], [1, -1, 0, 0]

def printA(A):
    print('Printing A...')
    for row in A:
        print(" ".join([f'{x}' for x in row]))
    return

# row 1 -> col4, row2 -> col3 ... 이런 식인거 같기도 하고?
def rotate_A(Grid_size, Block_size, A):
    
    return

def rotate_A_temp(Grid_size, Block_size, A):
    if Grid_size == 1:
        return A
    for r in range(0, A_size, Grid_size):
        for c in range(0, A_size, Grid_size):
            temp = [[A[r+i][c+j] for j in range(Block_size)] for i in range(Block_size)]
            for dr in range(Block_size):
                for dc in range(Block_size):
                    A[r+dr][c+dc] = A[r+dr+Block_size][c+dc]
                    A[r+dr+Block_size][c+dc] = A[r+dr+Block_size][c+dc+Block_size]
                    A[r+dr+Block_size][c+dc+Block_size] = A[r+dr][c+dc+Block_size]
                    A[r+dr][c+dc+Block_size] = temp[dr][dc]
    return A

def ice_melt(A):
    melting_indicies = []
    global Total_ice
    for r in range(A_size):
        for c in range(A_size):
            frost = 0
            for nr, nc in neigh[r][c]:
                if A[nr][nc]:
                    frost += 1
            if frost <= 2:
                melting_indicies.append((r, c))
                Total_ice -= 1
    for r, c in melting_indicies:
        A[r][c] -= 1
    return A

def biggest_chunk(A):
    visited = []
    max_chunk_size = 0
    for r in range(A_size):
        for c in range(A_size):
            if (r, c) in visited or not A[r][c]:
                continue
            visited.append((r, c))
            q = [(r, c)]
            chunk = [(r, c)]
            chunk_size = 1
            while q:
                cr, cc = q.pop(0)
                for nr, nc in neigh[cr][cc]:
                    if (nr, nc) not in chunk and A[nr][nc]:
                        q.append((nr, nc))
                        chunk.append((nr, nc))
                        visited.append((nr, nc))
                        chunk_size += 1
            if chunk_size > max_chunk_size:
                max_chunk_size = chunk_size
    return max_chunk_size

def solve(A, Grid_list, Block_list, L_list):
    for i in range(Q):
        Grid_size, Block_size, L = Grid_list[i], Block_list[i], L_list[i]
        A = rotate_A(Grid_size, Block_size, A)
        printA(A)
        A = ice_melt(A)
        printA(A)
        if Total_ice == 0:
            print(0)
            print(0)
            return
    print(Total_ice)
    print(biggest_chunk(A))
    print(sum([sum(row) for row in A]))
    return

if __name__ == "__main__":
    N, Q = map(int, input().split())
    A_size = 2**N
    A = [[int(x) for x in input().split()] for _ in range(A_size)]
    L_list = [int(x) for x in input().split()]
    # 90도 회전의 기준이 되는 단위 : 2**L 실제 움직이는 단위 : 2**(L-1), 
    Grid_list = [2**l for l in L_list]
    Block_list = [2**(l-1) for l in L_list]
    
    neigh = [[0] * A_size for _ in range(A_size)]
    for r in range(A_size):
        for c in range(A_size):
            nei = []
            for k in range(4):
                nr, nc = r+dr_list[k], c+dc_list[k]
                if 0 <= nr < A_size and 0 <= nc < A_size:
                    nei.append((nr, nc))
            neigh[r][c] = nei
    Total_ice = sum([sum(row) for row in A])
            
    solve(A, Grid_list, Block_list, L_list)
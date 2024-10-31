# r, l, u, d
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# spread list
list_spread = [((-1, 1), (0, 1), (1, 1)), ((-1, -1), (0, -1), (1, -1)), ((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1))]
# wall checker
list_wall_checker = [([(0, 0, 0), (-1, 0, 1)], [(0, 0, 1)], [(1, 0, 1), (1, 0, 0)]),
                    ([(0, 0, 0), (-1, -1, 1)], [(0, -1, 1)], [(1, 0, 0), (1, -1, 1)]),
                    ([(0, -1, 1), (0, -1, 0)], [(0, 0, 0)], [(0, 0, 1), (0, 1, 0)]),
                    ([(0, -1, 1), (1, -1, 0)], [(1, 0, 0)], [(0, 0, 1), (1, 1, 0)])]


def solve():
    room = [[0] * C for _ in range(R)]
    for choco in range(100):
        # 1 warmer
        for k, v in dict_temp_add.items():
            room[k[0]][k[1]] += v
        # 2 averaging
        next_room = [row[:] for row in room]
        for i in range(R):
            r = R-i-1
            for c in range(C):
                cur_temp = room[r][c]
                if r != 0:
                    if not mat_wall[0][r][c]:
                        up_temp = room[r-1][c]
                        temp_diff = cur_temp - up_temp
                        if temp_diff > 0:
                            change = temp_diff//4
                            next_room[r][c] -= change
                            next_room[r-1][c] += change
                        elif temp_diff < 0:
                            change = (-temp_diff)//4
                            next_room[r][c] += change
                            next_room[r-1][c] -= change
                if c != C-1:
                    if not mat_wall[1][r][c]:
                        right_temp = room[r][c+1]
                        temp_diff = cur_temp - right_temp
                        if temp_diff >= 4:
                            change = temp_diff//4
                            next_room[r][c] -= change
                            next_room[r][c+1] += change
                        elif temp_diff <= -4:
                            change = (-temp_diff)//4
                            next_room[r][c] += change
                            next_room[r][c+1] -= change
        room = next_room
        # 3 boarder - 1
        for i in range(R):
            room[i][0] = max(0, room[i][0] - 1)
            room[i][C-1] = max(0, room[i][C-1] - 1)
        for i in range(1, C-1):
            room[0][i] = max(0, room[0][i] - 1)
            room[R-1][i] = max(0, room[R-1][i] - 1)
        # 5 checkup
        if all([room[r][c] >= K for r, c in pivots]):
            print(choco + 1)
            return
    print(choco + 2)
    return

if __name__ == '__main__':
    R, C, K = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(R)]
    # 0 -> 위, 1 -> 오
    W = int(input())
    walls = [[int(x) for x in input().split()] for _ in range(W)]
    wall_matrix_up = [[0] * C for _ in range(R)]
    wall_matrix_right = [[0] * C for _ in range(R)]
    for r, c, t in walls:
        if t:
            wall_matrix_right[r-1][c-1] = 1
        else:
            wall_matrix_up[r-1][c-1] = 1
    mat_wall = [wall_matrix_up, wall_matrix_right]
    pivots = []
    warmer = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 5:
                pivots.append((r, c))
            elif 1 <= board[r][c] <= 4:
                warmer.append((r, c))

    add_up_matrix = [[0] * C for _ in range(R)]
    for r, c in warmer:
        temp = [[0] * C for _ in range(R)]
        direction = board[r][c] -1
        spread = list_spread[direction]
        cur_list_wall_checker = list_wall_checker[direction]
        nr, nc = r + dr[direction], c + dc[direction]
        q = [(nr, nc)]
        temp[nr][nc] = 5
        pivot = 0
        len_q = 1
        while pivot < len_q:
            cr, cc = q[pivot]
            cur_temp = temp[cr][cc]
            if cur_temp - 1:
                for i in range(3):
                    nr, nc = cr + spread[i][0], cc + spread[i][1]
                    if 0 <= nr < R and 0 <= nc < C:
                        if not temp[nr][nc]:
                            # if spreadable temp[nr][nc] = cur_temp - 1
                            if not any([mat_wall[t][cr+x][cc+y] for x, y, t in cur_list_wall_checker[i]]):
                                temp[nr][nc] = cur_temp - 1
                                q.append((nr, nc))
                                len_q += 1
            pivot += 1
        for r in range(R):
            for c in range(C):
                add_up_matrix[r][c] += temp[r][c]
    # dict_temp_add for better iteration
    dict_temp_add = {}
    for r in range(R):
        for c in range(C):
            if add_up_matrix[r][c]:
                dict_temp_add[(r, c)] = add_up_matrix[r][c]
    solve()

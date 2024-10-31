def ps(sea):
    for row in sea:
        line = [f'{x[2]}' if x else '0' for x in row]
        print(' '.join(line))
    print('##########')
#N S E W
def shark_turn():
    global sea, num_sharks
    next_sea = [[0 for _ in range(C)] for __ in range(R)]
    for r in range(R):
        for c in range(C):
            if sea[r][c]:
                s, d, z = sea[r][c]
                if d == 1:
                    d, cur = shark_move(s, False, R-1, r)
                    next_loc = [cur, c]
                    d = 2 if d else 1
                elif d == 2:
                    d, cur = shark_move(s, True, R-1, r)
                    next_loc = [cur, c]
                    d = 2 if d else 1
                elif d == 3:
                    d, cur = shark_move(s, True, C-1, c)
                    next_loc = [r, cur]
                    d = 3 if d else 4
                elif d == 4:
                    d, cur = shark_move(s, False, C-1, c)
                    next_loc = [r, cur]
                    d = 3 if d else 4
                nr, nc = next_loc
                if not next_sea[nr][nc]:
                    next_sea[nr][nc] = (s, d, z)
                else:
                    num_sharks -= 1
                    if next_sea[nr][nc][2] <= z:
                        next_sea[nr][nc] = (s, d, z)
    sea = next_sea
    return 1
    
def shark_move(s, d, l, cur):
    # d -> T/F
    # N, W
    if not d:
        if s <= cur:
            cur -= s
        else:
            s -= cur
            cur = 0
            d = not d
            # even, same_dir
            if (s//l)%2 == 0:
                cur = s%l
            # odd, opp dir
            else:
                d = not d
                cur = l - s%l
    else:
        if s <= l - cur:
            cur += s
        else:
            s -= (l-cur)
            cur = l
            d = not d
            # even, same_dir
            if (s//l)%2 == 0:
                cur = l - s%l
            # odd, opp dir
            else:
                d = not d
                cur = s%l
    return d, cur

def fisherman_turn(c):
    global sea, num_sharks
    for r in range(R):
        if sea[r][c]:
            catched_size = sea[r][c][2]
            sea[r][c] = 0
            num_sharks -= 1
            return catched_size
    return 0

def solve():
    global num_sharks
    total_catch = 0
    for c in range(C):
        total_catch += fisherman_turn(c)
        shark_turn()
        # ps(sea)
        if num_sharks == 0:
            return total_catch
    return total_catch

if __name__ == '__main__':
    R, C, M = map(int, input().split())
    sea = [[0 for _ in range(C)] for __ in range(R)]
    num_sharks = M
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        # speed, direction, size
        sea[r-1][c-1] = (s, d, z)
    # ps(sea)
    print(solve())
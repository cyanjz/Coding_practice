# 상어 -> 한턴에 n개의 칸을 이동할 수 있음. 이동한 칸에 물고기가 있어야만 함. 물고기를 먹으면 그 물고기의 방향으로 전환.
# 물고기 -> 작은 숫자부터 이동. 빈칸/다른 물고기 칸 이동 가능. 상어가 있거나 경계를 벗어나면 이동 불가.
# 물고기가 이동 못하면 그냥 이동 안하고, 상어가 이동 못하면 끝난다.

ea = 136
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

def fish_turn():
    global sea, fishes
    for k, v in fishes.items():
        if v:
            r, c, d = v
            for i in range(8):
                nd = (d+i)%8
                nr, nc = r + dr[nd], c + dc[nd]
                if 0 <= nr <= 3 and 0 <= nc <= 3:
                    if sea[nr][nc] != 17:
                        if sea[nr][nc]:
                            #swap
                            tmpk = sea[nr][nc]
                            tmpd = fishes[tmpk][2]
                            sea[nr][nc] = k
                            fishes[k] = (nr, nc, nd)
                            sea[r][c] = tmpk
                            fishes[tmpk] = (r, c, tmpd)
                            break
                        else:
                            sea[nr][nc] = k
                            fishes[k] = (nr, nc, nd)
                            sea[r][c] = 0
                            break
    return 1
            
def shark_turn():
    r, c, d = shark_state
    nr, nc = r, c
    candidates = []
    while True:
        nr, nc = nr + dr[d], nc + dc[d]
        if 0 <= nr <= 3 and 0 <= nc <= 3:
            fish = sea[nr][nc]
            if fish:
                candidates.append((nr, nc, fishes[fish][2]))
        else:
            break
    return candidates

def back_tracking(score):
    global sea, fishes, max_score, shark_state
    if max_score == ea:
        return 1
    else:
        pre_sea, pre_fishes = [row[:] for row in sea], {k : v for k, v in fishes.items()}
        fish_turn()
        candidates = shark_turn()
        if candidates:
            cur_shark_state = shark_state
            sea[cur_shark_state[0]][cur_shark_state[1]] = 0
            for cand in candidates:
                next_score = sea[cand[0]][cand[1]]

                sea[cand[0]][cand[1]] = 17
                fishes[next_score] = None
                shark_state = cand
                
                back_tracking(score + next_score)
                
                sea[cand[0]][cand[1]] = next_score
                fishes[next_score] = cand
                shark_state = cur_shark_state
        else:
            if max_score < score:
                max_score = score
        sea, fishes = pre_sea, pre_fishes
        return 1
    
        
def solve():
    back_tracking(start_score)
    print(max_score)
    return 1

if __name__ == '__main__':
    fishes = {k : None for k in range(1, 17)}
    sea = []
    for r in range(4):
        raw_in = input().split()
        row = []
        for c in range(4):
            num = int(raw_in[2 * c])
            d = int(raw_in[2 * c + 1])
            row.append(num)
            fishes[num] = (r, c, d-1)
        sea.append(row)
    
    shark_state = (0, 0, fishes[sea[0][0]][2])
    start_score = sea[0][0]
    fishes[sea[0][0]] = None
    sea[0][0] = 17
    max_score = 0
    solve()
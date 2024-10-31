from sys import stdin

def pl(lake):
    for row in lake:
        print(' '.join(f'{x}' for x in row))
    return 

dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

R, C = map(int, stdin.readline().strip().split())
lake = [list(stdin.readline().strip()) for _ in range(R)]

swan = []
water = []

for r in range(R):
    for c in range(C):
        el = lake[r][c]
        if el == 'L':
            lake[r][c] = '.'
            swan.append((r, c))
            water.append((r, c))
        elif el == '.':
            water.append((r, c))

day = 0
end = swan.pop()
lake[swan[0][0]][swan[0][1]] = 1
# print('#' * C)
# pl(lake)
while True:
    #BFS -> save points where swan meets X
    temp = []
    meet = False
    while swan:
        cr, cc = swan.pop(0)
        for k in range(4):
            nr, nc = cr + dr[k], cc + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if nr == end[0] and nc == end[1]:
                    temp = True
                    break
                if lake[nr][nc] != 1:
                    if lake[nr][nc] == '.':
                        lake[nr][nc] = 1
                        swan.append((nr, nc))
                    else:
                        lake[nr][nc] = 1
                        temp.append((nr, nc))
        if temp == True:
            break
    swan = temp
    # print(day)
    # print(swan)
    # print('#' * C)
    # pl(lake)
    if swan == True:
        print(day)
        break
    #melt
    temp = []
    for r, c in water:
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if lake[nr][nc] == 'X':
                    temp.append((nr, nc))
                    lake[nr][nc] = '.'
    temp.extend(swan)
    water = temp
    # print('#' * C)
    # pl(lake)
    day += 1
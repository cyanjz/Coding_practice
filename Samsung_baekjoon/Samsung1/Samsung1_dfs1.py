import copy
import sys
# left, up, right, down
moves = [0, -1, 0, 1, 0]
sort = [1, 0, 1, 0]
pm = [1, 1, -1, -1]

def pb(b):
    for i in range(len(b)):
        print(*b[i])

def tilt(d, cur_loc, b):
    color = b[cur_loc[0]][cur_loc[1]]
    next_loc = cur_loc.copy()
    while True:
        temp = [next_loc[i] + moves[d + i] for i in range(2)]
        if b[temp[0]][temp[1]] != '.':
            wall_type = b[temp[0]][temp[1]]
            break
        next_loc = temp.copy()
    b[cur_loc[0]][cur_loc[1]] = '.'
    if wall_type == 'O':
        return wall_type, color, next_loc, b
    else:
        b[next_loc[0]][next_loc[1]] = color
        return wall_type, color, next_loc, b



def brute_force(b, cur_locs, count, min_count):
    for i in range(4):
        cur_locs.sort(key = lambda x : pm[i]*x[sort[i]])
        b_copy = copy.deepcopy(b)
        next_locs = [0, 0]
        goals = [0, 0]
        for cur_loc in cur_locs:
            wall_type, color, next_loc, b_copy = tilt(i, cur_loc, b_copy)
            if color == 'R':
                next_locs[0] = next_loc.copy()
                if wall_type == 'O':
                    goals[0] = 1
            elif color == 'B':
                next_locs[1] = next_loc.copy()
                if wall_type == 'O':
                    goals[1] = 1
        if not goals[0] and not goals[1] and count < 10:
            cur_locs.sort(key = lambda x : x[0])
            next_locs.sort(key = lambda x : x[0])
            if cur_locs != next_locs:
                brute_force(b_copy, next_locs, count+1, min_count)
        elif not goals[1] and goals[0]:
            if min_count[0] > count:
                min_count[0] = count
        if min_count[0] == 1:
            break
    return None



M, N = map(int, sys.stdin.readline().rstrip('\n').split())
cur_locs = [0, 0]
b = []
for i in range(M):
    line = [x for x in sys.stdin.readline().rstrip('\n')]
    for k, c in enumerate(line):
        if c == 'R':
            cur_locs[0] = [i, k]
        elif c == 'B':
            cur_locs[1] = [i, k]
    b.append(line)
min_count = [11]
brute_force(b, cur_locs, 1, min_count)
if min_count[0] < 11:
    print(min_count[0])
else:
    print(-1)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# head : N E S W

def pr(room, M):
    print('#' * M)
    for row in room:
        print(' '.join([f'{x}' for x in row]))
    

def solve():
    thres = 0
    # N, M = map(int, file.readline().split())
    # cr, cc, head = map(int, file.readline().split())
    # room = [[int(x) for x in file.readline().split()] for _ in range(N)]
    N, M = map(int, input().split())
    cr, cc, head = map(int, input().split())
    room = [[int(x) for x in input().split()] for _ in range(N)]
    ca = 0
    while True:
        if room[cr][cc] == 0:
            room[cr][cc] = 2
            ca += 1
        # N E S W
        nei = [(room[cr + dr[i]][cc + dc[i]]) for i in range(4)]
        if all(nei):
            if nei[head - 2] == 1:
                print(ca)
                return
            else:
                cr, cc = cr + dr[head-2], cc + dc[head-2]
        else:
            for i in range(1, 5):
                head = (head - 1 + 4) % 4
                if nei[head] == 0:
                    cr, cc = cr + dr[head], cc + dc[head]
                    break

if __name__ == '__main__':
    # file = open('test.txt')
    # T = int(file.readline())
    # for _ in range(T):
    solve()
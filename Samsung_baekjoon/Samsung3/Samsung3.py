from collections import deque
import sys

heads = ['R', 'U', 'L', 'D']
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
rotation = {'L' : 1, 'D' : -1}


def sol():
    time = 0
    snake = deque([(1, 1)])
    head = 0
    N = int(sys.stdin.readline().rstrip('\n'))
    K = int(sys.stdin.readline().rstrip('\n'))
    apples = []
    for i in range(K):
        apples.append(tuple([int(x) for x in sys.stdin.readline().rstrip('\n').split()]))
    L = int(input())
    moves = []
    for i in range(L):
        moves.append(sys.stdin.readline().rstrip('\n').split())
    final_move = moves.pop()
    moves.append(final_move)
    moves.append([int(final_move[0]) + N + 1, 'L'])
    moves = deque(moves)
    while moves:
        end_time, direction = moves.popleft()
        distance = int(end_time) - time
        for i in range(int(distance)):
            time += 1
            cur_head = snake.popleft()
            next_head = (cur_head[0]+dy[head], cur_head[1]+dx[head])
            # early stop
            for cord in next_head:
                if not 1 <= cord or not N >= cord:
                    print(time)
                    return
            if next_head in snake:
                print(time)
                return
            # head moves
            snake.appendleft(cur_head)
            snake.appendleft(next_head)
            tail = snake.pop()
            # apple check
            for apple in apples:
                if apple == next_head:
                    apples.remove(apple)
                    snake.append(tail)
                    break
        head += rotation[direction]
        head += 4
        head %= 4
    print(time)
    return

sol()
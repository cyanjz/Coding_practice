# 11, 
base_line = ['s'] + [2 * i for i in range(1, 21)] + [0]
line1 = [13, 16, 19]
line2 = [22, 24]
line3 = [28, 27, 26]
line4 = [25, 30, 35]
board = [base_line, line1, line2, line3]
line_sizes = [len(row) for row in board]

def find_next_state(cur_state, number):
    cur_score = board[cur_state[0]][cur_state[1]]
    if cur_state[0] == 0:
        if cur_score/10 in range(1, 4):
            if line_sizes[cur_score//10] >= number:
                next_state = [cur_score//10, number-1]
            else:
                # 5 - 3 = 2
                next_state = [4, number - line_sizes[cur_score//10] - 1]
        else:
            next_state = [0, min(line_sizes[0]-1, cur_state[1] + number)]
    else:
        next_state = 

def bf(depth, score):
    global pieces, max_score, sh
    if depth == 10:
        if score > max_score:
            max_score = score
    if depth < 10:
        visited = []
        for i, piece in enumerate(pieces):
            if piece not in visited and board[piece[0]][piece[1]] != 0:
                visited.append(piece)
                cur_state = piece[:]
                if cur_state[0] == 0:
                    if 
                    next_state = [cur_state[0], min(cur_state[1] + numbers[depth], line_sizes[cur_state[0]]-1)]
                
                next_score = board[next_state[0]][next_state[1]]
                if cur_state[0] == 0 and next_score%10 == 0 and next_score//10 != 4:
                    next_state = [next_score//10, 0]
                if next_state not in pieces or line_sizes[next_state[0]] - 1 == next_state[1]:
                    if next_score == 25 or next_score == 40:
                        if next_score not in [board[p[0]][p[1]] for p in pieces]:
                            pieces[i] = next_state
                            bf(depth + 1, score + next_score)
                    else:
                        pieces[i] = next_state
                        bf(depth + 1, score + next_score)
                    pieces[i] = cur_state
    return 1

def solve():
    bf(0, 0)
    print(max_score)
    return 1

if __name__ == '__main__':
    max_score = 0
    pieces = [[0, 0] for _ in range(4)]
    numbers = [int(x) for x in input().split()]
    solve()
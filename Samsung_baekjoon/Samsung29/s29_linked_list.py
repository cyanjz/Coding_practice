class Node:
    def __init__(self, score):
        self.score = score
        self.red = None
        self.blue = None

class Board:
    def __init__(self):
        base_line = [Node(i*2) for i in range(21)]
        self.head = base_line[0]
        for i in range(20):
            base_line[i].red = base_line[i+1]

        cent = Node(25)
        base_line[5].blue = Node(13)
        base_line[5].blue.red = Node(16)
        base_line[5].blue.red.red = Node(19)
        base_line[5].blue.red.red.red = cent

        base_line[10].blue = Node(22)
        base_line[10].blue.red = Node(24)
        base_line[10].blue.red.red = cent

        base_line[15].blue = Node(28)
        base_line[15].blue.red = Node(27)
        base_line[15].blue.red.red = Node(26)
        base_line[15].blue.red.red.red = cent

        cent.red = Node(30)
        cent.red.red = Node(35)
        cent.red.red.red = base_line[20]

        base_line[-1].red = Node(0)
            
def bf(depth, score):
    global pieces, max_score
    if depth == 10:
        if max_score < score:
            max_score = score
        return 1
    visited = []
    for i, piece in enumerate(pieces):
        if piece not in visited and piece.red:
            visited.append(piece)
            cur_state = piece
            next_state = piece
            num = numbers[depth]
            
            if next_state.blue:
                next_state = next_state.blue
                num -= 1
            for _ in range(num):
                if not next_state.red:
                    break
                next_state = next_state.red

            if next_state not in pieces or not next_state.red:
                pieces[i] = next_state
                bf(depth + 1, score + next_state.score)
                pieces[i] = cur_state
    return 0

def solve():
    bf(0, 0)
    print(max_score)
    return 1

if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    board = Board()
    pieces = [board.head for _ in range(4)]
    max_score = 0
    solve()
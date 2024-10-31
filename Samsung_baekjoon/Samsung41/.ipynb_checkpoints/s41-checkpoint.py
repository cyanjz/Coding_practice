dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
d_constants = [7, 3, 1, 5]

class Chunk:
    def __init__(self, start_idx, number):
        self.start = start_idx
        self.end = None
        self.number = number
        self.size = 1

def B_list_change(B_list):
    new_list = []
    new_list_size = 0
    cur_idx = 0
    prev_number = B_list[0]
    chunk_size = 1
    for i in range(1, B_list_size):
        if new_list_size >= B_list_size:
            return new_list
        cur_number = B_list[i]
        if not cur_number:
            new_list.append(chunk_size)
            new_list.append(prev_number)
            new_list_size += 2
            new_list += [0] * (B_list_size - new_list_size)
            break
        if cur_number == prev_number:
            chunk_size += 1
        else:
            new_list.append(chunk_size)
            new_list.append(prev_number)
            new_list_size += 2
            prev_number = cur_number
            chunk_size = 1
    return new_list

def solve(B_list, blizzards):
    score = [0, 0, 0]
    for direction, distance in blizzards:
        constant = d_constants[direction-1]
        for i in range(distance):
            pivot = 4*i**2+3*i+(i+1)*constant-1
            B_list = B_list[:pivot] + B_list[pivot+1:]
        B_list += [0] * distance
        explode = 1
        while explode:
            explode = []
            cur_idx = 1
            cur_number = B_list[0]
            # no stuff
            if cur_number == 0:
                print(score[0] + 2 * score[1] + 3 * score[2])
                return
            chunk = Chunk(0, cur_number)
            while B_list_size > cur_idx:
                cur_number = B_list[cur_idx]
                if chunk.number == cur_number:
                    chunk.end = cur_idx
                    chunk.size += 1
                    cur_idx += 1
                else:
                    if chunk.size >= 4:
                        explode.append(chunk)
                    if cur_number == 0:
                        break
                    chunk = Chunk(cur_idx, cur_number)
                    cur_idx += 1
            if explode:
                s = -1
                temp = []
                total_size = 0
                for chunk in explode:
                    total_size += chunk.size
                    score[chunk.number-1] += chunk.size
                    e = chunk.start
                    temp += B_list[s+1:e]
                    s = chunk.end
                temp += B_list[s+1:]
                temp += [0] * total_size
                B_list = temp
        B_list = B_list_change(B_list)
    print(score[0] + 2 * score[1] + 3 * score[2])
    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    B = [[int(x) for x in input().split()] for _ in range(N)]
    blizzards = [[int(x) for x in input().split()] for _ in range(M)]
    B_list = []
    number_of_cycles = N//2
    cr, cc = number_of_cycles, number_of_cycles
    length = 1
    for __ in range(number_of_cycles):
        for k in range(2):
            for _ in range(length):
                cr += dr[2*k]
                cc += dc[2*k]
                B_list.append(B[cr][cc])
            for _ in range(length):
                cr += dr[2*k+1]
                cc += dc[2*k+1]
                B_list.append((B[cr][cc]))
            length += 1
    for _ in range(length-1):
        cr += dr[0]
        cc += dc[0]
        B_list.append(B[cr][cc])
    B_list_size = N**2-1
    solve(B_list, blizzards)
from collections import defaultdict

def pm(A):
    for row in A:
        print(' '.join([f'{x}' for x in row]))

def satisfy(A):
    R, C = len(A), len(A[0])
    if r-1 < R and c-1 < C:
        if A[r-1][c-1] == k:
            return True, R, C
    return False, R, C

def operateR(A):
    pad = 0
    for i, row in enumerate(A):
        line = []
        dump = defaultdict(int)
        for num in row:
            dump[num] += 1
        dump = [(k, v) for k, v in dump.items() if k != 0]
        dump.sort(key = lambda x : (x[1], x[0]))
        for k, v in dump:
            line.append(k)
            line.append(v)
        A[i] = line
        pad = max(pad, len(line))
    pad = min(100, pad)
    for i, row in enumerate(A):
        A[i] = row[:100] + [0] * (pad - len(row))
    return 0

# def operateC(A, R, C):
#     pad = 0
#     new_A = 
#     for c in range(C):
#         line = []
#         col = [A[r][c] for r in range(R)]
#         dump = defaultdict(int)
#         for num in col:
#             dump[num] += 1
#         dump = [(k, v) for k, v in dump.items()]
#         dump.sort(key = lambda x : (x[1], x[0]))
#         for k, v in dump:
#             line.append(k)
#             line.append(v)
#         for i in range(R):
#             A[i][c] = line[i]
            

def solve(A):
    sat, R, C = satisfy(A)
    if sat:
        return 0
    for t in range(1, 101):
        if R >= C:
            operateR(A)
        else:
            A = [x for x in zip(*A)]
            operateR(A)
            A = [x for x in zip(*A)]
        sat, R, C = satisfy(A)
        if sat:
            # pm(A)
            return t
    return -1
if __name__ == '__main__':
    r, c, k = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(3)]
    print(solve(A))
from collections import deque
from copy import deepcopy

moves = [0, -1, 0, 1, 0]
sort = [1, 0, 1, 0]
pm = [1, 1, -1, -1]


def tilt(ps, d, b):
    ps = sorted(ps, key = lambda x : pm[d] * x[sort[d]])
    n1 = ps[0][0:2]
    while True:
        temp = [n1[i] + moves[d + i] for i in range(2)]
        if b[temp[0]][temp[1]] != '.':
            end_type1 = [b[temp[0]][temp[1]]]
            if end_type1[0] == 'O':
                n1 = [-1, -1]
            break
        else:
            n1 = temp
    n1.append(ps[0][2])
    end_type1.append(ps[0][2])
    
    n2 = ps[1][0:2]
    while True:
        temp = [n2[i] + moves[d + i] for i in range(2)]
        if temp == n1[0:2]:
            end_type2 = ['C']
            break
        elif b[temp[0]][temp[1]] != '.':
            end_type2 = [b[temp[0]][temp[1]]]
            break
        else:
            n2 = temp
    n2.append(ps[1][2])
    end_type2.append(ps[1][2])
    
    return (end_type1, end_type2), (n1, n2)


M, N = map(int, input().split())
b = []
for i in range(M):
    line = [x for x in input()]
    for k, c in enumerate(line):
        if c == 'R':
            pr = [i, k, c]
            line[k] = '.'
        elif c == 'B':
            pb = [i, k, c]
            line[k] = '.'
    b.append(line)

q = deque()
q.append((pr, pb, 0))
min_count = 11
found = 0
while q and not found:
    pr, pb, count = q.popleft()
    for i in range(4):
        end_types, ns = tilt((pr, pb), i, b)
        sorted_end_types = sorted(end_types, key = lambda x : ord(x[1]))
        if sorted_end_types[0][0] != 'O':
            if sorted_end_types[1][0] != 'O':
                if sorted(ns, key = lambda x : x[0]) != sorted((pr, pb), key = lambda x : x[0]) and count < 10:
                    q.append((*ns, count + 1))
            elif sorted_end_types[1][0] == 'O':
                if min_count > count + 1:
                    min_count = count + 1
                    found = 1
if min_count < 11:
    print(min_count)
else:
    print(-1)
            
    
from sys import stdin
from itertools import combinations
input = stdin.readline
def solve():
    blanks = []
    virus = []
    for i in range(length):
        if world[i] == 0:
            blanks.append(i)
        elif world[i] == 2:
            virus.append(i)

    not_wall = len(blanks) + len(virus) - 3
    ans = 0 
    
    for build in combinations(blanks, 3):
        q = virus[:]
        tmp_world = world[:]
        infection = 0
        
        for pos in build:
            tmp_world[pos] = 1
            
        while q:
            idx = q.pop()
            infection += 1
            r, c = idx // M, idx % M
            adj = [
                idx - M if 0 < r else -1, #첫 줄이 아니면 상
                idx + M if r < N - 1 else -1, #마지막 줄이 아니면 하
                idx - 1 if 0 < c else -1, #첫번째가 아니면 좌
                idx + 1 if c < M - 1 else -1 # 마지막이 아니면 우
            ]
            
            for nxt in adj:
                if nxt != -1 and tmp_world[nxt] == 0:
                    tmp_world[nxt] = 2
                    q.append(nxt)

        cur = not_wall - infection
        if ans < cur:
            ans = cur

    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    length = N * M
    world = [0] * length
    
    for i in range(0, length, M): # 1차원 배열
        world[i:i + M] = [*map(int, input().split())]
        
    print(solve())
N, M = map(int, input().split())
hs, cs = [], []
for r in range(N):
    for c, n in enumerate(map(int, input().split())):
        if n == 1:
            hs.append((r, c))
        elif n == 2:
            cs.append((r, c))
C = len(cs)
answer = (2*N)**2
v = [0 for _ in range(C)]

def ham_distance(c, h):
    return abs(c[0]-h[0]) + abs(c[1]-h[1])

# row -> 특정 h에 대한 c 거리들.
ds = [sorted([(i, ham_distance(h, c)) for i, c in enumerate(cs)], key = lambda x : x[1]) for h in hs]

# 바꾸고 싶은 것만 global로 전달.
# 정렬을 미리 해서 for loop 내에서 정렬을 반복하지 않도록 한다.
def dfs(depth, cur_loc):
    global answer, v
    if depth == M:
        tmp = 0
        for hds in ds:
            for i, d in hds:
                if v[i]:
                    tmp += d
                    break
        answer = min(tmp, answer)
    else:
        for i in range(cur_loc, C-M+depth+1):
            v[i] = 1
            dfs(depth+1, i+1)
            v[i] = 0

def solve():
    dfs(0, 0)
    return

solve()
print(answer)
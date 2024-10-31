# year 연산을 skip 하는 방법 생각해보기.
# 지금 당장 year 자체를 최적화 하는 방법은 떠오르지 않는다.
# 5의 배수가 되기 전까지는 연산을 간략화 할 수 있지 않을까?


# 나이가 같은 나무가 굉장히 많이 생길 것이다 -> 따라서 trees dict를 관리할 때 year : count 형태로 관리하는게 좋다.
# 나눈 몫만큼 영양분을 빼내고 year + 1 의 count를 몫만큼 증가시킨다. -> 증가는 year +1을 수행할 때 해야함.
# 이때 

from collections import defaultdict

def year(trees, land, num_trees):
    mature = defaultdict(int)
    # spring & summer & winter
    for r in range(N):
        for c in range(N):
            cur_trees = sorted([x for x in trees[r][c].items()], key = lambda x : x[0])
            next_trees = defaultdict(int)
            soil = land[r][c]
            pivot = 0
            L = len(cur_trees)
            while pivot < L:
                k, v = cur_trees[pivot]
                quin = soil // k
                if quin > v:
                    soil -= k * v
                    next_trees[k+1] += v
                    if (k + 1) % 5 == 0:
                        mature[(r, c)] += v
                    pivot += 1
                else:
                    soil -= k * quin
                    if quin > 0:
                        next_trees[k+1] += quin
                        if (k + 1) % 5 == 0:
                            mature[(r, c)] += quin
                    soil += k//2 * (v-quin)
                    num_trees -= (v-quin)
                    pivot += 1
                    break
            for i in range(pivot, L):
                k, v = cur_trees[i]
                soil += k//2 * v
                num_trees -= v
            land[r][c] = soil
            trees[r][c] = next_trees
            #winter
            land[r][c] += A[r][c]
    # fall
    for k, v in mature.items():
        for ne in neigh[k]:
            trees[ne[0]][ne[1]][1] += v
            num_trees += v
    return num_trees
    
def solve(trees, land, num_trees):
    for _ in range(K):
        num_trees = year(trees, land, num_trees)
        if not num_trees:
            return 0
    return num_trees
        

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    neigh = {}
    for i in range(N):
        for j in range(N):
            tmp = []
            for k in range(8):
                nr, nc = i + dx[k], j + dy[k]
                if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                    tmp.append((nr, nc))
            neigh[(i, j)] = tmp
    
    land = [[5 for _ in range(N)] for __ in range(N)]
    trees = [[defaultdict(int) for _ in range(N)] for __ in range(N)]
    num_trees = 0
    for _ in range(M):
        r, c, o = map(int, input().split())
        trees[r-1][c-1][o] += 1
        num_trees += 1
    print(solve(trees, land, num_trees))
    # for i in range(N):
    #     tmp = [trees[i][j] for j in range(N)]
    #     tmp = [f'{sum(x.values())}' for x in tmp]
    #     print(' '.join(tmp))
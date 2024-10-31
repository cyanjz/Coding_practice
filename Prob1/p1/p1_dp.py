# 2 ** N <= 2 ** 100 iter -> not dp. since there is no memorizing process of recursive solutions.
# it is more like to backtracking with a too weak condition.
def dp_mem(pivot, W, wvlist):
    if pivot < 0:
        return 0
    w, v = wvlist[pivot]
    if W < w:
        return dp_mem(pivot-1, W, wvlist)
    else:
        left = dp_mem(pivot-1, W, wvlist)
        right = dp_mem(pivot-1, W-w, wvlist)
        return max(left, right + v)

# 100 * 100000 iter
def dp_time(wvlist):
    array = [[0 for _ in range(K+1)] for __ in range(N+1)]
    for i in range(1, N+1):
        for k in range(1, K+1):
            w, v = wvlist[i-1]
            if k < w:
                array[i][k] = array[i-1][k]
            else:
                array[i][k] = max(v + array[i-1][k-w], array[i-1][k])
    return array[-1][-1]

def backtracking(pivot, value, weight):
    global best
    w, v = wvlist[pivot]
    value += v
    weight += w
    if value > best:
        best = value
    if promising(pivot, value, weight):
        backtracking(pivot+1, value, weight)
        backtracking(pivot+1, value-v, weight-w)
    return

def promising(pivot, value, weight):
    if pivot == N-1:
        return False
    if weight + wvlist[pivot+1][1] > K:
        return False
    totweight = weight
    benefit = value
    j = pivot + 1
    while j < N-1 and totweight < K:
        w, v = wvlist[j]
        totweight += w
        benefit += v
        j += 1
    wk, vk = wvlist[j+1]
    benefit += (K - totweight) * pk/wk
    return benefit > best

def solve(N, K, wvlist):
    # print(dp_mem(N-1, K, wvlist))
    print(dp_time(wvlist))
    best = 0
    backtracking(0, 0, 0)
    print(best)
    return None

if __name__ == '__main__':
    best = 0 # for backtracking
    N, K = map(int, input().split())
    wvlist = [[int(x) for x in input().split()] for _ in range(N)]
    solve(N, K, wvlist)
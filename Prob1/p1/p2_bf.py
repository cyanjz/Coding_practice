def backtracking(pivot, value, weight):
    global best
    if value > best and weight <= K:
        best = value
    if promising(pivot, value, weight):
        w, v = wvlist[pivot]
        backtracking(pivot+1, value+v, weight+w)
        backtracking(pivot+1, value, weight)
    return

def promising(pivot, value, weight):
    if weight > K or pivot == N:
        return False
    if pivot == N-1:
        return True
    totweight = weight
    benefit = value
    j = pivot + 1
    while j < N-1 and totweight < K:
        w, v = wvlist[j]
        totweight += w
        benefit += v
        j += 1
    wk, vk = wvlist[j]
    benefit += (K - totweight) * vk/wk
    return benefit > best

def solve(N, K, wvlist):
    backtracking(0, 0, 0)
    print(best)
    return

if __name__ == '__main__':
    best = 0 # for backtracking
    N, K = map(int, input().split())
    wvlist = [[int(x) for x in input().split()] for _ in range(N)]
    wvlist = [[w, v, v/w] for w, v in wvlist]
    wvlist.sort(key = lambda x : -x[2])
    wvlist = [[x[0], x[1]] for x in wvlist]
    # print(wvlist)
    solve(N, K, wvlist)
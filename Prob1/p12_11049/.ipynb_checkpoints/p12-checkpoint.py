def solve(N, shapes):
    costs = [[0] * N for _ in range(N)]
    for l in range(1, N):
        for s in range(N-l):
            e = s + l
            costs[s][e] = min([costs[s][s+i] + costs[s+i+1][e] + shapes[s][0]*shapes[e][1]*shapes[s+i][1] for i in range(l)])
    print(costs[0][-1])          
    return

if __name__ == "__main__":
    N = int(input())
    # [(r, c)]
    shapes = [[int(x) for x in input().split()] for _ in range(N)]
    solve(N, shapes)
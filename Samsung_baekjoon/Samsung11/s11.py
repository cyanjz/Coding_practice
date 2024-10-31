from itertools import combinations, chain

def solve():
    N = int(input())
    S = [[int(x) for x in input().split()] for _ in range(N)]
    min_power_diff = sum([sum(row) for row in S])
    start_teams = combinations([_ for _ in range(1, N)], N//2)
    members = set([_ for _ in range(N)])
    for st in start_teams:
        st_power = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                st_power += S[st[i]][st[j]]
                st_power += S[st[j]][st[i]]
        lt = list(members - set(st))
        lt_power = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                lt_power += S[lt[i]][lt[j]]
                lt_power += S[lt[j]][lt[i]]
        power_diff = abs(lt_power - st_power)
        if power_diff < min_power_diff:
            min_power_diff = power_diff
    return min_power_diff

if __name__ == '__main__':
    print(solve())
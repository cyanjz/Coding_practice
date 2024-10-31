from itertools import combinations, chain

def solve():
    N = int(input())
    S = [int(x) for x in input().split()]
    S[0] = sum(S)
    for i in range(1, N):
        temp = [int(x) for x in input().split()]
        for j in range(N):
            S[j] += temp[j]
        S[i] += sum(temp)
    combs = combinations([_ for _ in range(N-1)], N//2)
    total_power = sum(S)
    min_diff = total_power
    for comb in combs:
        st_power = 0
        for mem in comb:
            st_power += S[mem]
        lt_power = total_power - st_power
        power_diff = abs(2 * st_power - total_power)
        if min_diff > power_diff:
            min_diff = power_diff
    return int(min_diff/2)

if __name__ == '__main__':
    print(solve())
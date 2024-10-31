def solve():
    global durabilities, K
    turn = 1
    robots = []
    for _ in range(500):
        # print(f'####{turn}')
        #1 belt rotate phase
        durabilities = durabilities[-1:] + durabilities[:-1]
        robots = [robot + 1 for robot in robots if robot + 1 < N-1]
        # print(durabilities, robots, K)
        
        #2 robot movement phase
        # condition : no robot in target space, positive durability
        # order : queue
        if robots:
            if durabilities[robots[0]+1] != 0:
                robots[0] += 1
                durabilities[robots[0]] -= 1
                if durabilities[robots[0]] == 0:
                    K -= 1
            for i, robot in enumerate(robots[1:]):
                if robots[i] != robot + 1 and durabilities[robot+1] != 0:
                    robots[i+1] += 1
                    durabilities[robot+1] -= 1
                    if durabilities[robot+1] == 0:
                        K -= 1
            if robots[0] == N-1:
                robots = robots[1:]
        # print(durabilities, robots, K)
        
        #3 robot placement phase
        if durabilities[0] != 0:
            robots.append(0)
            durabilities[0] -= 1
            if durabilities[0] == 0:
                K -= 1
        # print(durabilities, robots, K)
        
        #4 end checking phase
        if K <= 0:
            print(turn)
            return
        
        turn += 1
    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    durabilities = [int(x) for x in input().split()]
    solve()
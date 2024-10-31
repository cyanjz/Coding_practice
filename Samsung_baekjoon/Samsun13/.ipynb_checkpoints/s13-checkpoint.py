def rotate(e, r):
    return (e - r + 8) % 8

def solve():
    gears = [[int(x) for x in input()] for _ in range(4)]
    # left ends = [r-2 for r in right_ends]
    res = [2 for _ in range(4)]
    r = int(input())
    # 1 -> clockwise -1 -> counter-clockwise
    # clockwise -> r -= 1 cclockwise -> r += 1
    # same polar -> no rotation, different polar -> opposite rotation
    # score : 2**(i-1) i : gear number
    for _ in range(r):
        gear, clockwise = map(int, input().split())
        gear -= 1
        rotations = [0 for _ in range(4)]
        rotations[gear] += clockwise
        # left
        rg = gear
        # rg = 1
        for i in range(gear):
            lg = rg - 1
            # lg's right end == rg's left end
            if gears[lg][res[lg]] == gears[rg][res[rg] - 4]:
                break
            else:
                rotations[lg] = -rotations[rg]
                rg = lg
        # right
        lg = gear
        for rg in range(gear+1, 4):
            if gears[lg][res[lg]] == gears[rg][res[rg] - 4]:
                break
            else:
                rotations[rg] = -rotations[lg]
            lg = rg
        # print(f'{_} : {rotations}')
        res = [rotate(res[i], r) for i, r in enumerate(rotations)]
        # print(f'{_} : {res}')
    return sum([2**(i) if gears[i][res[i]-2] else 0 for i in range(4)])

if __name__ == '__main__':
    print(solve())
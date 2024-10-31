# 길을 하나씩 보다가, 높이가 변하면...
# 높아짐 -> 이전 L+1개를 참조.
# 낮아짐 -> 다음 L+1개를 참조.
# 벗어나는 경우는 놓지 못함!

def check(line, L, N):
    cl = 0
    length = 1
    while cl != N-1:
        nl = cl + 1
        nh = line[nl]
        ch = line[cl]
        if nh == ch:
            cl += 1
            length += 1
        # 위로 한칸
        elif nh - ch == 1:
            if length >= L:
                cl += 1
                length = 1
            else:
                return 0
        # 아래로 한칸
        elif nh - ch == -1:
            if cl + L < N:
                for i in range(L):
                    if line[nl + i] != nh:
                        return 0
                cl += L
                length = 0
            else:
                return 0

        # 너무 가파름
        elif abs(nh - ch) > 1:
            return 0
        else:
            breakpoint()
    return 1
            
            
        

def solve():
    N, L = map(int, input().split())
    world = [[int(x) for x in input().split()] for _ in range(N)]
    rows = []
    cols = []
    # rows
    for i in range(N):
        rows.append(check(world[i][:], L, N))
    # cols
    for i in range(N):
        cols.append(check([x[i] for x in world], L, N))
    return sum(rows + cols)

if __name__ == '__main__':
    print(solve())
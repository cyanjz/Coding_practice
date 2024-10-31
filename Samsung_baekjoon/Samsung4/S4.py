import sys

def sol():
    N = int(sys.stdin.readline().rstrip('\n'))
    A = [int(_) for _ in sys.stdin.readline().rstrip('\n').split()]
    B, C = map(int, sys.stdin.readline().rstrip('\n').split())
    dic = [0] + [1] * B + [0] * (1000000-B)
    watcher = 0
    for i in A:
        if not dic[i]:
            q0, q1 = divmod(i-B, C)
            dic[i] = q0 + 2 if q1 else q0 + 1
        watcher += dic[i]
        
    print(watcher)
    
sol()
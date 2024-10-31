def solve():
    N = int(input())
    ts, ps = [], []
    for _ in range(N):
        p, t = map(int, input().split())
        ts.append(t)
        ps.append(p)
    max_income = 0
    q = []
    for i in range(N):
        switch = 1
        for j, e in enumerate(q):
            # 날짜가 같은게 존재하면, 이전의 작업을 수행한쪽이 income이 더 크다.1
            # 따라서 같은 날짜가 발견되면 해당 원소를 업데이트 해준다.
            # 업데이트가 이뤄지지 않으면 q에 append.
            if e[0] == i:
                q[j] = (i+ps[i], q[j][1]+ts[i])
                switch = 0
        if switch:
            q.append((i+ps[i], ts[i]))
            
    q = [(i+ps[i], ts[i]) for i in range(N) if i+ps[i] < N+1]
    while q:
        cur_date, cur_income = q.pop(0)
        q.extend([(j+ps[j], cur_income+ts[j]) for j in range(cur_date, N) if j + ps[j] < N+1])
        if cur_income > max_income:
            max_income = cur_income
    print(max_income)

solve()

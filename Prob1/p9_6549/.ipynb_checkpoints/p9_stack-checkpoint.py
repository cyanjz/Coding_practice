from sys import stdin

def solve(chart):
    ans = -1
    N = chart.pop(0)
    stack = []
    for i in range(N):
        while stack:
            if stack[-1][1] > chart[i]:
                cur_idx, height = stack.pop()
                if stack:
                    # left : cur_idx - stack[-1][0]
                    # right : i - cur_idx
                    width = i - stack[-1][0] - 1
                else:
                    width = i
                area = width * height
            else:
                break
            ans = max(area, ans)
        stack.append((i, chart[i]))
    while stack:
        cur_idx, height = stack.pop()
        if stack:
            width = N - stack[-1][0] - 1
        else:
            width = N
        area = height * width
        ans = max(area, ans)
    print(ans)
    return

if __name__ == '__main__':
    while True:
        chart = [int(x) for x in stdin.readline().split()]
        if chart == [0]:
            break
        solve(chart)
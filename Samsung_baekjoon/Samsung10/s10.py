signs = ['+', '-', '*', '/']

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num1 < 0:
            return - ( - num1 // num2)
        else:
            return num1 // num2

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    counts = [int(x) for x in input().split()]
    results = [A.pop(0)]
    css = [counts[:]]
    for _ in range(N-1):
        num2 = A.pop(0)
        R = len(results)
        for __ in range(R):
            num1 = results.pop(0)
            cs = css.pop(0)
            for j in range(4):
                if cs[j] != 0:
                    tc = cs[:]
                    tc[j] -= 1
                    results.append(calculate(num1, num2, signs[j]))
                    css.append(tc)
    return max(results), min(results)

if __name__ == '__main__':
    M, m = solve()
    print(M)
    print(m)
def mat_mul(A, B):
    return [[sum([(row[i] * col[i])%div for i in range(N)])%div for col in zip(*B)] for row in A]

def matrix_power(A, m):
    if m == 1:
        return A
    temp = matrix_power(A, m//2)
    if m%2 == 1:
        return mat_mul(mat_mul(temp, temp), A)
    return mat_mul(temp, temp)

def pm(A):
    for row in A:
        print(' '.join([f'{x}' for x in row]))
    return

def solve(A, B):
    pm(matrix_power(A, B))
    return

if __name__ == '__main__':
    N, B = map(int, input().split())
    div = 1000
    A = [[int(x)%div for x in input().split()] for _ in range(N)]
    solve(A, B)
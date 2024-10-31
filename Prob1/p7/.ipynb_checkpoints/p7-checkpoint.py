N = int(input())
div = 1000000

def mat_mul(A, B):
    return [[sum([(row[i] * col[i])%div for i in range(2)])%div for col in zip(*B)] for row in A]

def mat_power(A, m):
    if m == 0:
        return [[1, 0], [0, 1]]
    temp = mat_power(A, m//2)
    if m%2:
        return mat_mul(mat_mul(temp, temp), A)
    return mat_mul(temp, temp)

# f1 = 0
# f2 = 1
# for i in range(N-1):
#     temp = (f2%div + f1%div)%div
#     f1 = f2
#     f2 = temp
# print(f2%1000000)

P = 1500000
N %= P
if N == 0:
    print(0)
elif N == 1 or N == 2:
    print(1)
else:
    A = [[1, 1], [1, 0]]
    B = mat_power(A, N-1)
    print(B[0][0])
N, K = map(int, input().split())

def divide_power(a, m):
    if m == 0:
        return 1
    temp = divide_power(a, m//2)
    if m % 2:
        return (temp * temp) % div * a % div
    return (temp * temp) % div
# numerator = N * N-1 * N-2 * ... * (N-K+1)
# demoninator = K * K-1 * K-2 ... * 1
div = 1000000007
A = 1
B = 1
for i in range(K):
    A = (A * (N-i)) % div
    B = (B * (i+1)) % div

print(((A%div) * (divide_power(B, div-2)%div)) % div)

# print(int(numerator/denominator)%1000000007)
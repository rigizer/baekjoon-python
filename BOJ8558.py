# https://www.acmicpc.net/problem/8558

n = int(input())

r = 1
for i in range(1, n + 1):
    r *= i

print(r % 10)

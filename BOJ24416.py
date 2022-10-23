# https://www.acmicpc.net/problem/24416

n = int(input())

def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    f = [0 for _ in range(n + 1)]
    f[1], f[2] = 1, 1

    cnt = 0
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return cnt

print(fib(n), fibonacci(n))

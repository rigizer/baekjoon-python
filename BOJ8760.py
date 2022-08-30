# https://www.acmicpc.net/problem/8760

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = a * b // 2
    print(n)

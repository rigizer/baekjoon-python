# https://www.acmicpc.net/problem/11021

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i + 1, a + b))

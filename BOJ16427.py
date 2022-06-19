# https://www.acmicpc.net/problem/16427

n, s = map(int, input().split())
m = map(int, input().split())

print((max(m) * s - 1) // 1000 + 1)

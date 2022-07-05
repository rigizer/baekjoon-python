# https://www.acmicpc.net/problem/9086

n = int(input())

for _ in range(n):
    t = input()
    print(t[0], end='')
    print(t[-1:])

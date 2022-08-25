# https://www.acmicpc.net/problem/4458

n = int(input())
for _ in range(n):
    data = input()
    print(data[0].upper() + data[1:])

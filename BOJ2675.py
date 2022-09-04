# https://www.acmicpc.net/problem/2675

n = int(input())
for _ in range(n):
    r, data = map(str, input().split())
    for d in data:
        for i in range(int(r)):
            print(d, end='')
    print()

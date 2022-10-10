# https://www.acmicpc.net/problem/11170

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for j in range(n, m + 1):
        for k in str(j):
            if k == '0':
                cnt += 1

    print(cnt)

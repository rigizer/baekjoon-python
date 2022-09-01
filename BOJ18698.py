# https://www.acmicpc.net/problem/18698

n = int(input())
for _ in range(n):
    n = input()
    cnt = 0
    for i in n:
        if i == 'D':
            break
        cnt += 1

    print(cnt)

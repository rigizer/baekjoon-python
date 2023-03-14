# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
ball = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        ball[x] = k

print(' '.join(str(ball[i]) for i in range(1, n + 1)))

# https://www.acmicpc.net/problem/11404

import sys

n, m = int(input()), int(input())
g = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j, s = map(int, input().split())
    g[i][j] = min(g[i][j], s)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
              
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if g[i][j] == sys.maxsize else g[i][j], end=' ')
    print()

# https://www.acmicpc.net/problem/12761

from collections import deque

def bfs(a, b, n, m):
    queue = deque()
    visited = [1e9] * 100_001

    queue.append((n, 0))
    visited[n] = 0

    while queue:
        nx, nt = queue.popleft()

        if nx == m:
            return nt
        
        for dx in [nx - 1, nx + 1, nx - a, nx - b, nx + a, nx + b, nx * a, nx * b]:
            if 0 <= dx <= 100_000 and visited[dx] > nt + 1:
                queue.append((dx, nt + 1))
                visited[dx] = nt + 1

a, b, n, m = map(int, input().split())

result = bfs(a, b, n, m)
print(result)

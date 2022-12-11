# https://www.acmicpc.net/problem/6798

from collections import deque

def bfs(sy, sx, ey, ex):
    queue = deque()
    visited = [[False] * 9 for _ in range(9)]

    queue.append((sy, sx, 0))
    visited[sy][sx] = True

    while queue:
        ny, nx, nt = queue.popleft()

        if ny == ey and nx == ex:
            return nt

        for dy, dx in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            y = ny + dy
            x = nx + dx

            if 1 <= y <= 8 and 1 <= x <= 8 and visited[y][x] == False:
                queue.append((y, x, nt + 1))
                visited[y][x] = True

sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

result = bfs(sy, sx, ey, ex)
print(result)

# https://www.acmicpc.net/problem/8061

from collections import deque

def bfs(n, m, board, i, j, result):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((i, j, 0))
    visited[i][j] = True
    result[i][j] = 0

    while queue:
        ny, nx, nt = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < n and 0 <= x < m and visited[y][x] == False and result[y][x] > nt + 1 and board[y][x] == '0':
                queue.append((y, x, nt + 1))
                visited[y][x] = True
                result[y][x] = nt + 1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
result = [[1e9] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            bfs(n, m, board, i, j, result)

print('\n'.join([' '.join([str(result[i][j]) for j in range(m)]) for i in range(n)]))

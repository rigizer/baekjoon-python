# https://www.acmicpc.net/problem/13565

from collections import deque

def bfs(m, n, board):
    queue = deque()
    visited = [[False] * n for _ in range(m)]

    for i in range(n):
        if board[0][i] == '0':
            queue.append((0, i))
            visited[0][i] = True

    while queue:
        ny, nx = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if y >= m:
                print('YES')
                return

            if 0 <= y < m and 0 <= x < n and visited[y][x] == False and board[y][x] == '0':
                queue.append((y, x))
                visited[y][x] = True

    print('NO')

m, n = map(int, input().split())
board = [list(input()) for _ in range(m)]

bfs(m, n, board)

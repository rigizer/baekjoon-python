# https://www.acmicpc.net/problem/25416

from collections import deque

def bfs(size, board, r, c):
    queue = deque()
    visited = [[False] * size for _ in range(size)]

    queue.append((r, c, 0))
    visited[r][c] = True
    
    while queue:
        ny, nx, nt = queue.popleft()

        if board[ny][nx] == 1:
            return nt

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < size and 0 <= x < size and visited[y][x] == False and board[y][x] != -1:
                queue.append((y, x, nt + 1))
                visited[y][x] = True

    return -1

SIZE = 5
board = [list(map(int, input().split())) for _ in range(SIZE)]
r, c = map(int, input().split())

result = bfs(SIZE, board, r, c)
print(result)

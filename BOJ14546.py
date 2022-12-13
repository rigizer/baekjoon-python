# https://www.acmicpc.net/problem/14546

from collections import deque

def bfs(width, height, sx, sy, ex, ey, board):
    standard = board[sy][sx]

    queue = deque()
    visited = [[False] * width for _ in range(height)]

    queue.append((sy, sx))
    visited[sy][sx] = True

    while queue:
        ny, nx = queue.popleft()

        if ny == ey and nx == ex:
            print('YES')
            return
        
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < height and 0 <= x < width and visited[y][x] == False and board[y][x] == standard:
                queue.append((y, x))
                visited[y][x] = True

    print('NO')

for _ in range(int(input())):
    l, w, a, b, c, d = map(int, input().split())
    board = [list(input()) for _ in range(w)]

    bfs(l, w, a - 1, w - b, c - 1, w - d, board)

# https://www.acmicpc.net/problem/4963

from collections import deque

def bfs(w, h, board):
    result = 0

    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < h and 0 <= x < w and visited[y][x] == False and board[y][x] == 1:
                            queue.append((y, x))
                            visited[y][x] = True

                result += 1

    return result

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]

    result = bfs(w, h, board)
    print(result)

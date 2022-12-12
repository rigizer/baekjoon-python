# https://www.acmicpc.net/problem/6080

from collections import deque

def bfs(r, c, board):
    result = 0

    queue = deque()
    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0 and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = False

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < r and 0 <= x < c and visited[y][x] == False and board[y][x] > 0:
                            queue.append((y, x))
                            visited[y][x] = True

                result += 1

    return result

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

result = bfs(r, c, board)
print(result)

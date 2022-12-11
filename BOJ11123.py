# https://www.acmicpc.net/problem/11123

from collections import deque

def bfs(h, w, board):
    result = 0

    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < h and 0 <= x < w and visited[y][x] == False and board[y][x] == '#':
                                queue.append((y, x))
                                visited[y][x] = True
                
                result += 1

    return result

for _ in range(int(input())):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]

    result = bfs(h, w, board)
    print(result)

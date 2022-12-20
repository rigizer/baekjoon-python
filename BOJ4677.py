# https://www.acmicpc.net/problem/4677

from collections import deque

def bfs(m, n, board):
    result = 0

    queue = deque()
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == '@' and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < m and 0 <= x < n and board[y][x] == '@' and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True

                result += 1

    return result

while True:
    m, n = map(int, input().split())
    if (0, 0) == (m, n): break

    board = [list(input()) for _ in range(m)]
    
    result = bfs(m, n, board)
    print(result)

# https://www.acmicpc.net/problem/21938

from collections import deque

def bfs(n, m, board):
    result = 0

    queue = deque()
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == True and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < n and 0 <= x < m and board[y][x] == True and visited[y][x] == False:
                            queue.append((y, x))
                            visited[y][x] = True

                result += 1

    return result

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

board = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        temp = data[i][j * 3 + 0] + data[i][j * 3 + 1] + data[i][j * 3 + 2]
        board[i][j] = True if temp // 3 >= t else False

result = bfs(n, m, board)
print(result)

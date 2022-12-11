# https://www.acmicpc.net/problem/9700

from collections import deque

def bfs(n, board):
    result = 0

    queue = deque()
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == '1' and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < n and 0 <= x < n and visited[y][x] == False and board[y][x] == '1':
                            queue.append((y, x))
                            visited[y][x] = True

                result += 1

    return result

tc = 0
while True:
    try:
        tc += 1

        n = int(input())
        board = [list(input()) for _ in range(n)]

        result = bfs(n, board)
        print('Case #{}: {}'.format(tc, result))
    except:
        break

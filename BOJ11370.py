# https://www.acmicpc.net/problem/11370

from collections import deque

def bfs(w, h, board):
    queue = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == 'S' and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True
    
    while queue:
        ny, nx = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < h and 0 <= x < w and visited[y][x] == False and board[y][x] == 'T':
                queue.append((y, x))
                board[y][x] = 'S'
                visited[y][x] = True

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0): break

    board = [list(input()) for _ in range(h)]

    visited = bfs(w, h, board)

    for i in range(h):
        for j in range(w):
            print(board[i][j], end='')
        print()

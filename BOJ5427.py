# https://www.acmicpc.net/problem/5427

from collections import deque

def fire_init(w, h, board, queue, visited):
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                queue.append((i, j, 0))
                visited[i][j] = 0

    return visited

def bfs_fire(w, h, board):
    queue = deque()
    visited = [[1e9] * w for _ in range(h)]

    fire_init(w, h, board, queue, visited)

    while queue:
        ny, nx, nt = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if 0 <= y < h and 0 <= x < w and visited[y][x] == 1e9 and board[y][x] == '.':
                queue.append((y, x, nt + 1))
                visited[y][x] = nt + 1

    return visited

def sangeun_init(w, h, board, queue, visited):
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                queue.append((i, j, 0))
                visited[i][j] = True
                return

def bfs_sangeun(w, h, board, fire_history):
    queue = deque()
    visited = [[False] * w for _ in range(h)]

    sangeun_init(w, h, board, queue, visited)

    while queue:
        ny, nx, nt = queue.popleft()

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = ny + dy
            x = nx + dx

            if y < 0 or y >= h or x < 0 or x >= w:
                return nt + 1
            
            if visited[y][x] == False and board[y][x] == '.' and (fire_history[y][x] > nt + 1 or fire_history[y][x] == 1e9):
                queue.append((y, x, nt + 1))
                visited[y][x] = True

    return 'IMPOSSIBLE'

def calc(w, h, board):
    fire_history = bfs_fire(w, h, board)
    result = bfs_sangeun(w, h, board, fire_history)

    return result

for _ in range(int(input())):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]

    result = calc(w, h, board)
    print(result)

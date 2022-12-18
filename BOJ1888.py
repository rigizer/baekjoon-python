# https://www.acmicpc.net/problem/1888

from collections import deque

def check_bfs(m, n, board):
    queue = deque()
    visited = [[False] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True
                
                while queue:
                    ny, nx = queue.popleft()

                    for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        y = ny + dy
                        x = nx + dx

                        if 0 <= y < m and 0 <= x < n and visited[y][x] == False and board[y][x] > 0:
                            queue.append((y, x))
                            visited[y][x] = True

                return visited
    
    return visited

def check_board(m, n, board):
    visited = check_bfs(m, n, board)

    for i in range(m):
        for j in range(n):
            if visited[i][j] == False and board[i][j] > 0:
                return False # 추가 계산 필요

    return True  # 추가 계산 필요 없음

def bfs(m, n, board):
    result = 0

    while True:
        if check_board(m, n, board): return result

        result += 1

        queue = deque()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0 and visited[i][j] == False:
                    if visited[i][j] == True: break
                    queue.append((i, j))
                    visited[i][j] = True

                    for y in range(i - board[i][j], i + board[i][j] + 1):
                        for x in range(j - board[i][j], j + board[i][j] + 1):
                            if 0 <= y < m and 0 <= x < n:
                                if board[y][x] < board[i][j]:
                                    queue.append((y, x))
                                    visited[y][x] = True
                                    board[y][x] = board[i][j]

m, n = map(int, input().split())
board = [[int(j) for j in list(input())] for _ in range(m)]

result = bfs(m, n, board)
print(result)

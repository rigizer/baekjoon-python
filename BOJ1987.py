# https://www.acmicpc.net/problem/1987

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

queue = [False for _ in range(26)]
maxSize = 1

def dfs(i, j, size):
    global r, c, maxSize
    maxSize = max(maxSize, size)
    
    for d in range(4):
        y = i + dy[d]
        x = j + dx[d]

        if 0 <= y < r and 0 <= x < c and visited[y][x] == False:
            if queue[ord(board[y][x]) - 65] == False:
                queue[ord(board[y][x]) - 65] = True
                visited[y][x] = True
                dfs(y, x, size + 1)
                queue[ord(board[y][x]) - 65] = False
                visited[y][x] = False

queue[ord(board[0][0]) - 65] = True
visited[0][0] = True
dfs(0, 0, 1)

print(maxSize)

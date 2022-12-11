# https://www.acmicpc.net/problem/9311

from collections import deque

class Node:
    def __init__(self, y, x, t):
        self.y = y
        self.x = x
        self.t = t

    def __str__(self):
        return 'y={}, x={}, t={}'.format(self.y, self.x, self.t)

def init(r, c, board, queue, visited):
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                queue.append(Node(i, j, 0))
                visited[i][j] = True
                return

def bfs(r, c, board):
    queue = deque()
    visited = [[False] * c for _ in range(r)]

    init(r, c, board, queue, visited)

    while queue:
        node = queue.popleft()

        if board[node.y][node.x] == 'G':
            print('Shortest Path: {}'.format(node.t))
            return

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y = node.y + dy
            x = node.x + dx

            if 0 <= y < r and 0 <= x < c and visited[y][x] == False and board[y][x] != 'X':
                queue.append(Node(y, x, node.t + 1))
                visited[y][x] = True
    
    print('No Exit')
    return

for _ in range(int(input())):
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    bfs(r, c, board)

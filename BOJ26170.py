# https://www.acmicpc.net/problem/26170

from collections import deque

class Node:
    def __init__(self, y, x, t, e):
        self.y = y
        self.x = x
        self.t = t
        self.e = e

    def __str__(self):
        return 'y={}, x={}, t={}, e={}'.format(self.y, self.x, self.t, self.e)

stack = deque()
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
r, c = map(int, input().split())

result = 1e9

stack.append(Node(r, c, 0, 0))
visited[r][c] = True

def dfs():
    global result

    if len(stack) == 0: return

    node = stack.pop()

    if node.e == 3:
        result = min(result, node.t)
        return

    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        y = node.y + dy
        x = node.x + dx

        if 0 <= y < 5 and 0 <= x < 5 and visited[y][x] == False and board[y][x] != -1:
            if board[y][x] == 1:
                stack.append(Node(y, x, node.t + 1, node.e + 1))
            elif board[y][x] == 0:
                stack.append(Node(y, x, node.t + 1, node.e))

            visited[y][x] = True
            dfs()
            visited[y][x] = False

dfs()

print(-1 if result == 1e9 else result)

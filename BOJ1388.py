# https://www.acmicpc.net/problem/1388

from queue import deque

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return 'y={}, x={}' % (self.y, self.x)

def bfs(n, m, board):
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == True: continue
            else:
                queue = deque()
                queue.append(Node(i, j))
                visited[i][j] = True

                while queue:
                    node = queue.pop()

                    if board[node.y][node.x] == '-': dir = [(0, -1), (0, 1)]
                    elif board[node.y][node.x] == '|': dir = [(-1, 0), (1, 0)]

                    for dy, dx in dir:
                        y = node.y + dy
                        x = node.x + dx

                        if 0 <= y < n and 0 <= x < m and visited[y][x] == False:
                            if board[node.y][node.x] == board[y][x]:
                                queue.append(Node(y, x))
                                visited[y][x] = True

                cnt += 1

    return cnt

def main():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    result = bfs(n, m, board)
    print(result)

if __name__ == '__main__':
    main()

# https://www.acmicpc.net/problem/4179

from collections import deque

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return 'y={}, x={}'.format(self.y, self.x)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def queue_init(r, c, board, queue, visited, q):
    for i in range(r):
        for j in range(c):
            if board[i][j] == q:
                queue.append(Node(i, j))
                visited[i][j] = 0

def bfs(r, c, board):
    # 불 확산 시뮬레이션    
    f_queue = deque()
    f_visited = [[-1] * c for _ in range(r)]
    queue_init(r, c, board, f_queue, f_visited, 'F')

    while f_queue:
        node = f_queue.popleft()

        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]

            if 0 <= y < r and 0 <= x < c and f_visited[y][x] == -1 and board[y][x] != '#':
                f_queue.append(Node(y, x))
                f_visited[y][x] = f_visited[node.y][node.x] + 1

    # 지훈이 탈출 시뮬레이션
    j_queue = deque()
    j_visited = [[-1] * c for _ in range(c)]
    queue_init(r, c, board, j_queue, j_visited, 'J')

    while j_queue:
        node = j_queue.popleft()

        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]

            if 0 <= y < r and 0 <= x < c:
                # 불이 없거나, 현재시간 이후에 생길 불 위치라면 이동해도 OK, 기존에 불이 생겼던 곳이면 이동 X
                if board[y][x] != '#' and j_visited[y][x] == -1 and (f_visited[y][x] > j_visited[node.y][node.x] + 1 or f_visited[y][x] == -1):
                    j_queue.append(Node(y, x))
                    j_visited[y][x] = j_visited[node.y][node.x] + 1

            else:
                return j_visited[node.y][node.x] + 1

    return 'IMPOSSIBLE'

def main():
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    result = bfs(r, c, board)
    print(result)

if __name__ == '__main__':
    main()

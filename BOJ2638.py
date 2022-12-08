# https://www.acmicpc.net/problem/2638

from collections import deque

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __str__(self):
        return 'y={}, x={}'.format(self.y, self.x)

def bfs(n, m, board):
    t = 0

    while True:
        cnt = 0
        queue = deque()
        visited = [[0] * m for _ in range(n)]

        queue.append(Node(0, 0))
        visited[0][0] = 2

        while queue:
            node = queue.popleft()

            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                y = node.y + dy
                x = node.x + dx

                if 0 <= y < n and 0 <= x < m:
                    if board[y][x] == 0 and visited[y][x] == 0:
                        queue.append(Node(y, x))
                        visited[y][x] = 2

                    elif board[y][x] == 1 and visited[y][x] < 2:
                        if visited[y][x] == 0:  # 한 면만 닿는 경우
                            visited[y][x] = 1

                        elif visited[y][x] == 1:  # 치즈 녹이기
                            board[y][x] = 0
                            visited[y][x] = 2
                            cnt += 1

        if cnt == 0: break

        t += 1

    return t

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = bfs(n, m, board)
    print(result)

if __name__ == '__main__':
    main()

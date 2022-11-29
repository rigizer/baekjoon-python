# https://www.acmicpc.net/problem/16933

from collections import deque

class Node:
    def __init__(self, y, x, t, d, w):
        self.y = y  # 현재 y 좌표
        self.x = x  # 현재 x 좌표
        self.t = t  # 지나온 거리
        self.d = d  # 낮(True), 밤(False) 여부
        self.w = w  # 몇 개의 벽을 앞으로 더 뚫을 수 있는지

    def __str__(self):
        return 'y={}, x={}, t={}'.format(self.y, self.x, self.t)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, k, board):
    result = 1e9
    queue = deque()
    visited = [[[1e9] * m for i in range(n)] for _ in range(k + 1)]

    queue.append(Node(0, 0, 1, True, 0))
    visited[0][0][0] = 0

    while queue:
        node = queue.popleft()

        if node.y == n - 1 and node.x == m - 1:
            result = min(result, node.t)

        # 밤일때 가만히 있는 경우
        if node.d == False:
            queue.append(Node(node.y, node.x, node.t + 1, True, node.w))

        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]

            if 0 <= y < n and 0 <= x < m:
                if node.d == True:    
                    # 낮일때 벽 뚫고 이동하는 경우
                    if node.w < k and visited[node.w + 1][y][x] > node.t + 1 and board[y][x] == 1:
                        queue.append(Node(y, x, node.t + 1, False, node.w + 1))
                        visited[node.w + 1][y][x] = node.t + 1

                # 낮/밤일때 벽 뚫지 않고 이동하는 경우
                if visited[node.w][y][x] > node.t + 1 and board[y][x] == 0:
                        queue.append(Node(y, x, node.t + 1, not node.d, node.w))
                        visited[node.w][y][x] = node.t + 1

    return -1 if result == 1e9 else result

def main():
    n, m, k = map(int, input().split())
    board = [[int(j) for j in input()] for i in range(n)]

    result = bfs(n, m, k, board)
    print(result)

if __name__ == '__main__':
    main()

# https://www.acmicpc.net/problem/2636

from collections import deque

class Node:
    def __init__(self, y, x, t):
        self.y = y  # y 좌표
        self.x = x  # x 좌표
        self.t = t  # 지나온 시간

    def __str__(self):
        return 'y={}, x={}, t={}'.format(self.y, self.x, self.t)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(h, w, board, melt_time, t):
    cnt = 0

    queue = deque()
    visited = [[False] * w for _ in range(h)]

    queue.append(Node(0, 0, -1))
    visited[0][0] = True

    while queue:
        node = queue.popleft()

        for d in range(4):
            y = node.y + dy[d]
            x = node.x + dx[d]

            if 0 <= y < h and 0 <= x < w and visited[y][x] == False:
                if board[y][x] == 0:
                    queue.append(Node(y, x, node.t))
                    visited[y][x] = True

                elif board[y][x] == 1:
                    if melt_time[y][x] != -1:
                        queue.append(Node(y, x, node.t + 1))
                    
                    elif melt_time[y][x] == -1:
                        melt_time[y][x] = t
                        cnt += 1
                    
                    visited[y][x] = True

    return cnt

def search_before(h, w, melt_time, before_time):
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if melt_time[i][j] == before_time:
                cnt += 1

    return cnt

def main():
    h, w = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    melt_time = [[-1] * w for _ in range(h)]

    end = 0
    while True:
        cnt = bfs(h, w, board, melt_time, end)
        if cnt == 0: break

        end += 1

    before_cnt = search_before(h, w, melt_time, end - 1)
    
    print(end)
    print(before_cnt)

if __name__ == '__main__':
    main()
